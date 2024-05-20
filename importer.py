import logging
import sys
import json
import datetime
import os
import time
import hashlib
import requests
from io import BytesIO
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6.QtWidgets import QApplication
from pathlib import Path
from os.path import exists
from zipfile import ZipFile
from PIL import Image, UnidentifiedImageError
import shortuuid
import misc
from UI.import_window import Ui_w_import
import my_logger
import models, tags, versions, creators
from mover import ProgressDialog
from civitai import models
from civitai import creators


class WorkerSignals(qtc.QObject):
    """  Defines the signals available from a running worker thread. """
    finished = qtc.Signal()
    error = qtc.Signal(tuple)
    result = qtc.Signal(object)


class Worker(qtc.QRunnable):
    """  Worker thread  """
    def __init__(self, destination, model):
        super(Worker, self).__init__()
        self.signals = WorkerSignals()
        self.destination = destination
        self.model = model

    def run(self):
        BUF_SIZE = 65536  # let's read stuff in 64kb chunks!
        sha256 = hashlib.sha256()
        with open(self.model, 'rb') as h:
            while True:
                data = h.read(BUF_SIZE)
                if not data:
                    break
                sha256.update(data)
        self.signals.result.emit(sha256.hexdigest())
        self.signals.finished.emit()


class ImportForm(qtw.QMainWindow, Ui_w_import):  # must match form type!

    destination_is_set = False
    source_is_set = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.threadpool = qtc.QThreadPool()
        self.logger = my_logger.QTextEditLogger(self)
        placeholder = self.verticalLayout
        placeholder.addWidget(self.logger.widget)
        self.finished = False
        self.my_hash = ''


        # log to text box
        self.logger.setFormatter(
            logging.Formatter(
                '%(levelname)s: %(module)s %(funcName)s; %(message)s'))
        logging.getLogger().addHandler(self.logger)
        logging.getLogger().setLevel(logging.INFO)

        # log to file
        fh = logging.FileHandler('logs/import.log', mode='a', encoding='utf-8')
        fh.setLevel(logging.INFO)
        fh.setFormatter(
            logging.Formatter(
                '%(asctime)s -  %(levelname)s: %(module)s %(funcName)s; %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p'))
        logging.getLogger().addHandler(fh)

        self.settings = ''

        form_font = self.font()
        form_font.setPointSize(12)
        self.setFont(form_font)

        #  loop widgets assign checkbox stateChanged signal to unified slot
        cblist = self.groupBox.findChildren(qtw.QCheckBox)

        for cb in cblist:
            cb.stateChanged.connect(
                lambda stateChanged, cbname = cb.objectName(): self.toggle_le_enabled(stateChanged, cbname)
            )

        ffont = self.font()
        ffont.setPointSize(12)
        self.setFont(ffont)

        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.accepted.connect(self.process_import)
        self.pb_source.clicked.connect(self.set_source)
        self.pb_destination.clicked.connect(self.set_destination)

    def move_models(self, model, destination, model_path, model_file, model_hash):

        b_size = Path(model).stat().st_size
        kb_size = b_size / 1024
        mb_size = kb_size / 1024
        gb_size = mb_size / 1024

        if mb_size > 500:  # only use thread for large files
            prog = ProgressDialog(self, model, destination, model_file, True)
            prog.finished.connect(lambda: setattr(self, 'finished', True))
            prog.start()
            self.finished = False
            while not self.finished:
                time.sleep(.1)
                QApplication.processEvents()
        else:
            file = qtc.QFile(model)
            file.rename(destination)

        logging.info(f"zipping old files for {model_file}")
        zip_files = list(misc.list_matches_recursively(model_path, model_file))
        with ZipFile(destination + '.zip',
                     'w') as my_zip:  # zip old accompanying files
            # writing each file one by one
            for file in zip_files:
                my_zip.write(file)
                os.remove(file)  # delete old files
        try:  # remove old folder if empty
            Path(model_path).rmdir()
        except FileNotFoundError:
            logging.debug("FileNotFoundError")
        except NotADirectoryError:
            logging.debug("NotADirectoryError")
        except OSError as error:
            logging.info(error)
        # save.hash model_hash
        with open(destination + '.' + 'sha256', "w") as hfile:
            hfile.write(model_hash)
            hfile.close()
            logging.info(f"hash file created for {model_file}")

    def return_value(self, value):
        self.my_hash = value

    def get_models(self, source, destination, model_type, api_key):
        model_list = list(misc.list_files_recursively(source))
        model_count = len(model_list)
        if model_count > 0:
            logging.info(f"Found {model_count} models")
            current_count = 0
            progress = qtw.QProgressDialog("Importing models...", "", 0, model_count, self)
            progress.setMinimumDuration(10)
            progress.setCancelButton(None)
            progress.setWindowModality(qtc.Qt.WindowModal)
            for model in model_list:
                QApplication.processEvents()

                current_count += 1
                progress.setLabelText(f"Importing model: {model} ")
                logging.info(f"Processing model {current_count} of {model_count}")
                try:
                    logging.info(f"Processing model {model}")
                except Exception as e:
                    logging.debug("Error: {e}")
                QApplication.processEvents()
                # set initial variables
                model_path = str(Path(model).parent)
                target_name = Path(model).name
                model_file = Path(target_name).stem

                # get hash of model
                logging.info(f"Hashing {model_file}")
                self.finished = False
                worker = Worker(destination, model)
                worker.signals.result.connect(self.return_value)
                worker.signals.finished.connect(lambda: setattr(self, 'finished', True))
                self.threadpool.start(worker)

                while not self.finished:
                    time.sleep(.1)
                    QApplication.processEvents()
                model_hash = self.my_hash
                logging.info(f"Hash: {model_hash}")

                # get data from civitai api (or files where available)
                # use api to get version info by hash
                hash_endpoint = f"https://civitai.com/api/v1/model-versions/by-hash/{model_hash}"
                version_json = misc.fetch_json(hash_endpoint)
                version = models.get_by_hash(model_hash)
                load_path = str(Path(model_path) / model_file)
                if not isinstance(version_json, dict):  # File no longer (or never was on civit)
                    logging.warning(
                        f"Unknown File - {model} Trying other methods to get info. Status returned: {version_json}")
                    load = False
                    # try -version.json
                    user_file = ''
                    if exists(load_path + '-version.json'):
                        with open(load_path + '-version.json', errors="ignore") as user_file:
                            version_json = json.load(user_file)
                            load = True
                            logging.info("loaded version json")
                    # try civit.info - missing Model type
                    elif exists(load_path + '.civit.info'):
                        with open(load_path + '.civit.info', errors="ignore") as user_file:
                            version_json = json.load(user_file)
                            load = True
                            logging.info("loaded civit.info")
                    # try civitai.info
                    elif exists(load_path + '.civitai.info'):
                        with open(load_path + '.civitai.info', errors="ignore") as user_file:
                            version_json = json.load(user_file)
                            load = True
                            logging.info("loaded civitai info")

                    if load :
                        version = models.get_modelVersion_from_file(user_file)

                    if load is True and version_json.get('id') == '':  # nothing on civit and nothing in the file system
                        version_json = 'empty'

                if isinstance(version_json, dict):
                    # collect version Information
                    model_id = str(version_json.get('modelId'))  # Base Model ID
                    model_id = version.modelId
                    version_id = str(version_json.get('id'))
                    version_id = version.id
                    version_url = f"https://civitai.com/models/{model_id}?modelVersionId={version_id}"
                    version_files = version_json.get('files')  # list
                    version_files = version.files  # list
                    version_files = version_files[0]  # dict
                    version_stats = version_json.get('stats')
                    version_stats = version.stats
                    version_filename = version_files.get('name')  # probably should query this by hash?
                    model_data = version_json.get('model', {})
                    model_data = version.model  # dict
                    version_images = version_json.get('images')
                    version_images = version.images

                    if not model_data.get('type') is None:  # use model type from Civit if available
                        model_type = model_data.get('type')

                    version_image = ""
                    for image in version_images:  # maybe add option to get additional images?
                        for items in image:
                            if version_image == "":
                                version_image = image['url']

                    # pass modelId to https://civitai.com/api/v1/models/:modelId or parse json from above
                    model_endpoint = f"https://civitai.com/api/v1/models/{model_id}"
                    model_json = misc.fetch_json(model_endpoint)
                    model = models.get_model(model_id)

                    version_localpath = str(
                        destination / model_type / model_id / version_id)  # append additional pathing information?

                    if not isinstance(model_json, dict):  # model not on civit
                        # try civit.full.info
                        if exists(load_path + '.civit.full.info'):
                            with open(load_path + '.civit.full.info', errors="ignore") as user_file:
                                model_json = json.load(user_file)
                                model = models.get_model_from_file(user_file)
                                logging.info("loaded civit.full.info")
                        # try .json
                        elif exists(load_path + '.json'):
                            with open(load_path + '.json', errors="ignore") as user_file:
                                model_json = json.load(user_file)
                                model = models.get_model_from_file(user_file)
                                logging.info("loaded .json")


                    if isinstance(model_json, dict):
                        model_creators = model_json.get('creator')  # dict
                        model_creators = model.creator  # dict
                        creator_id = model_creators.get('username')
                        model_source = f"https://civitai.com/models/{model_id}"

                        # return  modelTags
                        try:
                            if model_json.get('tags') is None:
                                model_json = model_json.get("items")
                                if model_json.get('tags') is None:
                                    model_tags = []
                                model_tags = model_json.get('tags')
                            model_tags = model_json.get('tags')
                            model_tags = model.tags
                        except:
                            model_tags = []
                    else:
                        model_tags = []

                    # pass creator to https://civitai.com/api/v1/creators
                    creator_endpoint = f"https://civitai.com/api/v1/creators?query={creator_id}"
                    creator_json = misc.fetch_json(creator_endpoint)
                    creator = creators.get(creator_id)

                    if isinstance(creator_json, dict):
                        creator_json = creator_json.get('items')  # list
                        if creator_json:
                            creator_json = creator_json[0]
                            creator_url = creator_json.get('link')
                            creator_url = creator.link
                        else:
                            creator_json = {}
                            creator_url = ''
                    else:
                        creator_json = {}
                        creator_url = ''
                    # set and create directories
                    new_dir = Path(version_localpath)

                    # check for existing file
                    if not exists(new_dir / version_filename):
                        new_dir.mkdir(parents=True, exist_ok=True)
                        # Save to DB
                        # Save Model
                        model_db = models.add_model(str(version.modelId),
                                                    model.name.title(),
                                                    model.description,
                                                    model_type,
                                                    model.nsfw,
                                                    '',
                                                    json.dumps(model_json),
                                                    model_source,
                                                    creator_id,
                                                    datetime.datetime.now(),
                                                    '')
                        if model_db == 'Success':
                            logging.info(f"Model {model_id} added to DB")
                        else:
                            logging.error(model_db)

                        # Save Version
                        version_parameters = (str(version.id),
                                              version.name.title(),
                                              version.description,
                                              str(version.modelId),
                                              version.createdAt,
                                              version_url,
                                              json.dumps(version.trainedWords),
                                              model_hash,
                                              version_stats.get('downloadCount',0),
                                              version_stats.get('ratingCount',0),
                                              version_stats.get('rating',0),
                                              version.updatedAt,
                                              version.baseModel,
                                              json.dumps(version_json),
                                              '', '',
                                              version_localpath,
                                              version_filename,
                                              datetime.datetime.now(),
                                              version_files.get('name'),
                                              version.status,
                                              '',
                                              version.publishedAt,
                                              datetime.datetime.now(),
                                              '',
                                              '',
                                              version_stats.get('thumbsUpCount',0),
                                              '',
                                              target_name,
                                              model_path)
                        version_db = versions.add_version(version_parameters)
                        if version_db == 'Success':
                            logging.info(f"Version {version_id} added to DB")
                        else:
                            logging.error(version_db)
                        # Save Creator
                        creator_parameters = (creator_id,
                                              creator_id,
                                              creator_url,
                                              model_creators.get('image'),
                                              json.dumps(creator_json))
                        creator_db = creators.add_creator(creator_parameters)
                        if creator_db == 'Success':
                            logging.info(f"Model {creator_id} added to DB")
                        else:
                            logging.error(creator_db)
                        # write tags and link to models
                        for tag in model_tags:
                            tag_parameters = (tag,)
                            tag_id = tags.add_tag(tag_parameters)  # add tag to db
                            tag_db = tags.add_tag2model(tag_id, model_id)  # link tag to model
                            if tag_db == 'Success':
                                logging.info(f"Tag {tag} added to DB")
                            else:
                                logging.error(tag_db)
                        # move files and rename (if needed)
                        logging.info(f"Moving {model} to {new_dir}")
                        self.move_models(model, str(new_dir) + '/' + version_filename,
                                         model_path, model_file, model_hash)

                        # get image

                        url_extension = misc.get_url_extension(version_image)
                        url_filename = str(new_dir) + '/' + version_filename + '.preview' + url_extension

                        try:
                            image_response = requests.get(version_image, timeout=0.5)
                            logging.info(f"Getting image from URL: {version_image}")

                            if image_response.status_code == 200:
                                logging.info(f"Saving image to {url_filename}")
                                with open(url_filename, 'wb') as f:
                                    f.write(image_response.content)
                            else:
                                logging.info(f"Failed to get the image from URL: {version_image}")

                            # img = Image.open(BytesIO(image_response.content))
                            # img.save(url_filename)

                        except Exception as e:
                            logging.info(f"Failed to get the image from URL: {version_image}. Error: {e}")
                    else:
                        logging.info("possible duplicate of " + model)
                        logging.warning("Duplicate file found at " + str(new_dir) + '\\' + version_filename)

                else:
                    logging.info(f"Unknown File - {model}")
                    my_hash = (model_hash,)
                    check_hash = versions.get_path_by_hash(my_hash)
                    if check_hash is not False:
                        logging.info(f"Duplicate File found at {check_hash}")
                    else:
                        model_id = shortuuid.uuid()
                        version_id = shortuuid.uuid()
                        version_localpath = str(
                            destination / model_type / model_id / version_id)  # append additional pathing information
                        model_source = "unknown"
                        # Save to DB generate minimal information to catalog file
                        # Save Model
                        model_db = models.add_model(model_id,
                                                    model_file.title(),
                                                    '',
                                                    model_type,
                                                    '',
                                                    '',
                                                    '',
                                                    "unknown",
                                                    "unknown",
                                                    '',
                                                    datetime.datetime.now()
                                                    )
                        if model_db == 'Success':
                            logging.info(f"Model {model_id} added to DB")
                        else:
                            logging.error(model_db)
                        # Save Version
                        version_parameters = (
                            version_id,
                            model_file.title(),
                            '',  # description
                            model_id,
                            '',  # created
                            'unknown',
                            '',  # words
                            model_hash,
                            '', '', '',  # downloads, ratings, rating
                            '',  # updated
                            'unknown',  # baseModel
                            '', '', '',  # json, deployed, vault
                            version_localpath,
                            target_name,
                            datetime.datetime.now(),
                            target_name,
                            '', '', '',
                            datetime.datetime.now(),
                            '', '', '', '',
                            target_name,
                            model_path)
                        version_db = versions.add_version(version_parameters)
                        if version_db == 'Success':
                            logging.info(f"Version {version_id} added to DB")
                        else:
                            logging.error(version_db)

                        # send to currentRootFolder
                        new_dir = Path(version_localpath)
                        os.makedirs(str(new_dir), exist_ok=True)
                        self.move_models(model, str(new_dir) + '/' + target_name, model_path, model_file, model_hash)
                progress.setValue(current_count)
    @qtc.Slot()
    def toggle_le_enabled(self, state, cb):
        # get checkbox name
        # parse ending number
        # toggle enabled based on state
        le_suffix = cb.removeprefix('checkBox')
        le_name = 'lineEdit'+le_suffix
        le = self.findChild(qtw.QWidget, le_name)
        le.setEnabled(bool(state))

    @qtc.Slot()
    def process_import(self):

        if self.source_is_set is True and self.destination_is_set is True:
            QApplication.setOverrideCursor(qtc.Qt.WaitCursor)
            # loop enabled le's and create list of paths to process
            # call import function
            source = Path(self.le_source.text())
            destination = Path(self.le_destination.text())
            # loop checkboxes to see which models to import
            cblist = self.groupBox.findChildren(qtw.QCheckBox)

            for cb in cblist:
                if cb.isChecked() is True:
                    cb_name = cb.objectName()
                    le_suffix = cb_name.removeprefix('checkBox')
                    le_name = 'lineEdit' + le_suffix
                    le = self.groupBox.findChild(qtw.QWidget, le_name)
                    if le.text().startswith('\\') is True:
                        le_path = Path(le.text().strip('\\'))
                        new_path = source/le_path
                        # source = new_path
                    else:
                        new_path = Path(le.text())
                    logging.info(f"Importing {cb.text()} from {str(new_path)}")
                    self.get_models(new_path, destination, cb.text().replace(' ', ''), self.settings.value('civitai_settings/API_key'))
            logging.info("Import Complete")
            QApplication.restoreOverrideCursor()
        else:
            # warn user to provide valid directories
            qtw.QMessageBox.warning(self, "Error", "Please set the Source and Destination Paths")

    @qtc.Slot()
    def set_source(self):
        dir_name = qtw.QFileDialog.getExistingDirectory(self, "Select a Source Directory")
        if dir_name:
            path = Path(dir_name)
            self.source_is_set = True
            self.le_source.setText(dir_name)

    @qtc.Slot()
    def set_destination(self):
        dir_name2 = qtw.QFileDialog.getExistingDirectory(self, "Select a Destination Directory")
        if dir_name2:
            path = Path(dir_name2)
            self.destination_is_set = True
            self.le_destination.setText(dir_name2)

    def load_settings(self, settings):
        self.settings = settings        # get default settings from settings file
        self.lineEdit.setText(self.settings.value('default_import_paths/AestheticGradient', ''))
        self.lineEdit_2.setText(self.settings.value('default_import_paths/Checkpoint', ''))
        self.lineEdit_3.setText(self.settings.value('default_import_paths/Controlnet', ''))
        self.lineEdit_4.setText(self.settings.value('default_import_paths/Dora', ''))
        self.lineEdit_5.setText(self.settings.value('default_import_paths/Hypernetwork', ''))
        self.lineEdit_6.setText(self.settings.value('default_import_paths/LORA', ''))
        self.lineEdit_7.setText(self.settings.value('default_import_paths/loCon', ''))
        self.lineEdit_8.setText(self.settings.value('default_import_paths/MotionModule', ''))
        self.lineEdit_10.setText(self.settings.value('default_import_paths/Pose', ''))
        self.lineEdit_11.setText(self.settings.value('default_import_paths/TextualInversion', ''))
        self.lineEdit_12.setText(self.settings.value('default_import_paths/Upscaler', ''))
        self.lineEdit_13.setText(self.settings.value('default_import_paths/VAE', ''))
        self.lineEdit_14.setText(self.settings.value('default_import_paths/Wildcard', ''))
        self.lineEdit_15.setText(self.settings.value('default_import_paths/Workflow', ''))
        self.le_source.setText(self.settings.value('main_settings/import_path', ''))
        self.le_destination.setText(self.settings.value('main_settings/storage_path', ''))
        if self.le_source.text() != '':
            self.source_is_set = True
        if self.le_destination.text() != '':
            self.destination_is_set = True
        logging.info("Settings loaded")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = ImportForm()  # class name
    window.show()

    sys.exit(app.exec())
