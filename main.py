import sys
import os
from os.path import exists
from pathlib import Path
import mouse  # used to control resize
import json

from PySide6 import QtCore as qtc, QtCore, QtGui, QtWebEngineCore
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtCore import QModelIndex, QSize
from PySide6.QtGui import QPalette, QImageReader, QPixmap, QMouseEvent
from PySide6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery, QSqlQueryModel
import sqlite3
from contextlib import closing

from PySide6.QtWidgets import QLabel, QSizePolicy

import misc
import web
from UI.main_window2 import Ui_w_main
from importer import ImportForm
from instance import InstanceForm
from my_label import MyLabel
from settings import SettingsDialog

import logging
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
logger = logging.getLogger("Main")
sys.argv += ['-platform', 'windows:darkmode=2']
basedir = os.path.dirname(__file__)

db = QSqlDatabase("QSQLITE")
db.setDatabaseName(os.path.join(basedir, "manager"))
db.open()


class MainForm(qtw.QMainWindow, Ui_w_main):  # must match form type!

    def __init__(self):
        super().__init__()
        self._flag = False
        self.mouse_up = True
        self.needs_resize = False
        self.current_image = qtw.QLabel()
        self.old_image = qtw.QLabel()
        self.setupUi(self)

        # build some settings
        qtc.QSettings.setDefaultFormat(qtc.QSettings.Format.IniFormat)
        qtc.QSettings.setPath(qtc.QSettings.Format.IniFormat, qtc.QSettings.SystemScope, basedir)
        qtc.QSettings.setPath(qtc.QSettings.Format.IniFormat, qtc.QSettings.UserScope, basedir)
        self.settings = qtc.QSettings()

        self.show()

        self.model_filter = '"Name - Version" LIKE "%"'
        self.base_filter = '"Model Type" LIKE "%"'
        self.type_filter = '"Base Model" LIKE "%"'
        self.tag_filter = 'Tags LIKE "%"'

        form_font = self.font()
        form_font.setPointSize(12)
        self.setFont(form_font)

        self.setWindowTitle('Smartt Model Manager')
        self.f_instance2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.f_instance1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lb_instance1.setText("No Instance Loaded")
        self.lb_instance2.setText("No Instance Loaded")
        self.sp_verticle.moveSplitter(250, 1)
        self.sp_horizontal.moveSplitter(567, 1)
        self.pb_log.setText("Show Log")
        self.te_log.setMaximumHeight(0)
        self.f_left.setMaximumWidth(0)

        self.actionImport_Models.triggered.connect(self.import_models)
        self.actionAdd_Instance.triggered.connect(self.add_instance)
        self.actionSettings.triggered.connect(self.load_settings)
        self.le_search.textChanged.connect(self.update_filter)
        self.lv_model_type.clicked.connect(self.mt_selected)
        self.lv_base_model.clicked.connect(self.bm_selected)
        self.sp_horizontal.splitterMoved.connect(self.on_resize)
        self.sp_verticle.splitterMoved.connect(self.on_resize)
        self.pb_log.clicked.connect(self.show_hide_log)

        type_query = QSqlQuery('SELECT DISTINCT'
                               ' m."type" AS "Model Type"'
                               ' FROM models m;', db=db)

        base_query = QSqlQuery('SELECT DISTINCT'
                               ' v.basemodel'
                               ' FROM versions v;', db=db)

        self.model_model = QSqlTableModel(db=db)
        self.model_model.setTable('v_models_versions')
        self.tv_models_2.setModel(self.model_model)
        self.model_model.setSort(0, qtc.Qt.AscendingOrder)
        self.model_model.select()
        self.tv_models_2.setColumnHidden(6, True)
        self.tv_models_2.setColumnHidden(7, True)
        self.tv_models_2.setColumnHidden(8, True)
        self.tv_models_2.resizeColumnsToContents()
        self.model_model.modelReset.connect(self.load_images)

        self.type_model = QSqlQueryModel()
        self.lv_model_type.setModel(self.type_model)
        self.type_model.setQuery(type_query)

        self.base_model = QSqlQueryModel()
        self.lv_base_model.setModel(self.base_model)
        self.base_model.setQuery(base_query)

        self.instance_box = qtw.QComboBox()
        self.instance_box.currentTextChanged.connect(self.load_instance)
        self.instance_box.currentIndexChanged.connect(self.load_instance)
        self.instance_model = self.instance_box.model()
        item = qtg.QStandardItem('<none>')
        self.instance_model.appendRow(item)
        self.tv_models_2.setMouseTracking(True)
        self.tv_models_2.entered.connect(self.on_item_entered)
        self.tv_models_2.setContextMenuPolicy(qtc.Qt.CustomContextMenu)
        self.tv_models_2.customContextMenuRequested.connect(self.open_menu)
        self.item_menu = qtw.QMenu()
        self.item_menu.setTitle('Deploy to:')
        self.item_menu_as = qtw.QMenu()
        self.item_menu_as.setTitle('Deploy as:')

        with closing(sqlite3.connect("manager")) as connection:
            with closing(connection.cursor()) as cursor:
                rows = cursor.execute("SELECT * FROM main.instances").fetchall()
                for row in rows:
                    item = qtg.QStandardItem(str(row[0]))
                    item.setBackground(qtg.QColor(row[4]))
                    fore_color = row[4].lstrip('#')
                    fore_color = misc.max_contrasting_text_color(fore_color)
                    fore_color = qtg.QColor.fromString('#' + fore_color)
                    item.setForeground(fore_color)
                    font = item.font()
                    font.setBold(True)
                    item.setFont(font)
                    # add widget to menu to hold instances from https://stackoverflow.com/questions/31190384
                    w_action = qtw.QWidgetAction(self)
                    ql = MyLabel(w_action)
                    ql.setText(item.text())
                    ql.setStyleSheet("background-color: " + row[4] + "; color: " + fore_color.name())
                    w_action.setDefaultWidget(ql)
                    w_action.triggered.connect(
                        lambda triggered=False, qlname=ql.text(): self.item_clicked(triggered, qlname)
                    )
                    self.item_menu.addAction(w_action)
                    w_action2 = qtw.QWidgetAction(self)
                    ql2 = MyLabel(w_action2)
                    ql2.setText(item.text())
                    ql2.setStyleSheet("background-color: " + row[4] + "; color: " + fore_color.name())
                    w_action2.setDefaultWidget(ql2)
                    w_action2.triggered.connect(
                        lambda triggered=True, qlname2=ql2.text(): self.item_clicked(triggered, qlname2)
                    )
                    self.item_menu_as.addAction(w_action2)
                    self.instance_model.appendRow(item)

        self.instance_label = qtw.QLabel()
        self.instance_label.setText('Instances:')
        self.tbar_manager.insertWidget(self.actionAdd_Instance, self.instance_label)
        self.instance_box.setFocusPolicy(qtc.Qt.NoFocus)
        self.tbar_manager.addWidget(self.instance_box)
        self.tbar_manager.addSeparator()
        self.tv_models_2.clicked.connect(self.show_model)
        # self.t_list.currentChanged.connect(self.load_images)

        self.tree_model = qtg.QStandardItemModel()
        self.tv_models_3.setModel(self.tree_model)
        self.tv_models_3.clicked.connect(self.tree_clicked)

        self.tb_forward.clicked.connect(self.we_web.forward)
        self.tb_back.clicked.connect(self.we_web.back)
        self.we_web.urlChanged.connect(self.set_url)
        self.le_navbar.returnPressed.connect(self.navigate_to_url)
        self.tb_go.clicked.connect(self.navigate_to_url)
        self.we_web.page().profile().downloadRequested.connect(self.on_download_requested)
        self.load_tree()
        self.load_images()

    @qtc.Slot()
    def test(self, e):
        print(e)

    @qtc.Slot()
    def load_settings(self):
        form = SettingsDialog()
        # form.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        form.load_settings(self.settings)
        form.exec()

    @qtc.Slot(QtWebEngineCore.QWebEngineDownloadRequest)
    def on_download_requested(self, e):
        download_type = e.mimeType()
        # print(download_type)
        if download_type.split('/')[0] == 'image':
            download_path = self.tv_properties.item(10, 0).text()
            download_file = self.tv_properties.item(11, 0).text() + '.preview.jpeg'
            e.setDownloadDirectory(download_path)
            e.setDownloadFileName(download_file)
            e.accept()

    @qtc.Slot()
    def navigate_to_url(self):
        q = qtc.QUrl(self.le_navbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.we_web.setUrl(q)

    @qtc.Slot()
    def set_url(self, e):
        self.le_navbar.setText(e.toString())
        self.le_navbar.setCursorPosition(0)

    def tree_clicked(self, e):
        print(e)
        tv = e.model()
        tv_name = tv.itemFromIndex(e).text()
        tv_filter = tv.itemFromIndex(e.siblingAtColumn(1)).text()
        self.load_filter(tv_filter)

    def load_tree(self):
        self.tv_models_3.columnCount = 2

        q = qtg.QStandardItem
        self.tree_model.appendRow([q("Model Type"), q("")])
        self.tree_model.appendRow([q("Base Model Type"), q("")])
        self.tree_model.appendRow([q("Tags"), q("")])
        type_root = self.tree_model.item(0, 0)
        base_model_root = self.tree_model.item(1, 0)
        tag_root = self.tree_model.item(2, 0)

        with closing(sqlite3.connect("manager")) as connection:
            with closing(connection.cursor()) as cursor:
                rows = cursor.execute("SELECT * FROM main.v_models_versions").fetchall()
                type_seen = {}
                base_seen = {}
                for row in rows:
                    model_type_root = type_seen.get(row[1], 'None')
                    if model_type_root == 'None':
                        # add Types
                        type_filter = '"Model Type" LIKE "' + row[1] + '"'
                        model_type_root = q(row[1])
                        model_type_root.setToolTip(row[1])
                        type_root.appendRow([model_type_root, q(type_filter)])
                        type_seen.update({row[1]: model_type_root})

                    base_root = type_seen.get(row[1]+row[2], 'None')
                    if base_root == 'None':
                        type_filter = '"Model Type" LIKE "' + row[1] + '" AND "Base Model" LIKE "' + row[2] + '"'
                        base_root = q(row[2])
                        base_root.setToolTip(row[2])
                        # add Base Models
                        model_type_root.appendRow([base_root, q(type_filter)])
                        type_seen.update({row[1]+row[2]: base_root})

                    model_root = type_seen.get(row[1]+row[2]+row[0], 'None')
                    if model_root == 'None':
                        type_filter = ('"Model Type" LIKE "' + row[1] + '" AND "Base Model" LIKE "' + row[2] +
                                       '" AND "Name - Version" LIKE "' + row[0] + '"')
                        model_root = q(row[0])
                        model_root.setToolTip(row[0])
                        # add Models
                        base_root.appendRow([model_root, q(type_filter)])
                        type_seen.update({row[1]+row[2]+row[0]: model_root})

                    base_root = base_seen.get(row[2], 'None')
                    if base_root == 'None':
                        type_filter = ('"Base Model" LIKE "' + row[2] + '"')
                        base_root = q(row[2])
                        base_root.setToolTip(row[2])
                        # add Types
                        base_model_root.appendRow([base_root, q(type_filter)])
                        base_seen.update({row[2]: base_root})

                    model_type_root = base_seen.get(row[1]+row[2], 'None')
                    if model_type_root == 'None':
                        type_filter = ('"Base Model" LIKE "' + row[2] +
                                       '" AND "Model Type" LIKE "' + row[1] + '"')
                        # add Types
                        model_type_root = q(row[1])
                        model_type_root.setToolTip(row[1])
                        base_root.appendRow([model_type_root, q(type_filter)])
                        base_seen.update({row[1]+row[2]: model_type_root})

                    model_root = base_seen.get(row[2] + row[2] + row[0], 'None')
                    if model_root == 'None':
                        type_filter = ('"Model Type" LIKE "' + row[1] + '" AND "Base Model" LIKE "' + row[2] +
                                       '" AND "Name - Version" LIKE "' + row[0] + '"')
                        model_root = q(row[0])
                        model_root.setToolTip(row[0])
                        model_type_root.appendRow([model_root, q(type_filter)])
                        base_seen.update({row[2] + row[2] + row[0]: model_root})

        with closing(sqlite3.connect("manager")) as connection:
            with closing(connection.cursor()) as cursor:
                rows = cursor.execute("SELECT * FROM main.v_models_tags").fetchall()
                tag_seen = {}
                for row in rows:
                    tag = row[2]
                    if not isinstance(tag, str):
                        tag = '<none>'
                    tags_root = tag_seen.get(tag, 'None')
                    if tags_root == 'None':
                        type_filter = 'Tags LIKE "%,' + tag + ',%" OR Tags LIKE "' + tag + ',%"'
                        tags_root = q(tag)
                        tags_root.setToolTip(tag)
                        tag_root.appendRow([tags_root, q(type_filter)])
                        tag_seen.update({tag: tags_root})

                    models_root = type_seen.get(row[0] + tag, 'None')
                    if models_root == 'None':
                        type_filter = '"Name - Version" LIKE "' + row[0] + '%"'
                        models_root = q(row[0])
                        models_root.setToolTip(row[0])
                        tags_root.appendRow([models_root, q(type_filter)])
                        tag_seen.update({row[0] + tag: models_root})

        self.tv_models_3.setColumnHidden(1, True)  # hide column with filter data

    @qtc.Slot()
    def show_model(self, i):
        self.old_image = self.current_image  # set old image to current image
        self.current_image = self.f_images.findChild(QLabel, str(i.row()))  # get current image by name
        self.old_image.setStyleSheet("border: 0px")  # 'unselect' old image
        self.current_image.setStyleSheet("border: 3px solid #1864AB")  # add select box for selected image
        tv_model = self.tv_models_2.model()
        tv_index = tv_model.index(i.row(), 8)
        item = tv_model.data(tv_index)
        self.we_web.load(item)
        v_index = tv_model.index(i.row(), 7)
        v = tv_model.data(v_index)
        self.load_local(v)

    @qtc.Slot()
    def icon_clicked(self, m, i):
        pos = m.globalPosition().toPoint()  # get global mouse position
        self.old_image = self.current_image  # set old image to current image
        self.current_image = qtw.QApplication.widgetAt(pos)  # get current image at mouse position
        try:
            self.old_image.setStyleSheet("border: 0px")  # 'unselect' old image
        except Exception as e:
            logging.debug(e)
        self.current_image.setStyleSheet("border: 3px solid #1864AB")  # add select box for selected image
        self.tv_models_2.selectRow(int(i))  # select proper row in table view
        tv_model = self.tv_models_2.model()
        tv_index = tv_model.index(int(i), 8)
        item = tv_model.data(tv_index)
        self.we_web.load(item)
        v_index = tv_model.index(int(i), 7)
        v = tv_model.data(v_index)
        self.load_local(v)

    @qtc.Slot()
    def load_local(self, version_id):
        path = Path(basedir + '/none.webp')
        version_data = web.get_version(version_id)[0]
        item = str(Path(version_data['version_path'])/Path(version_data['version_file_name']))
        if exists(item + '.preview.jpeg'):
            path = Path(item + '.preview.jpeg')
        gv = self.lb_image
        gv.setBackgroundRole(QPalette.Base)
        gv.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # gv.setScaledContents(True)
        filename = str(path)
        reader = QImageReader(filename)
        newimage = reader.read()
        image = QPixmap.fromImage(newimage)
        gv.setPixmap(image.scaled(gv.size(), qtc.Qt.KeepAspectRatio, qtc.Qt.SmoothTransformation))
        gv.setAlignment(qtc.Qt.AlignCenter)
        self.lb_title.setText(version_data['model_name'] + ' - ' + version_data['version_name'])
        self.te_version.setText(version_data['version_description'])
        self.te_model.setText(version_data['model_description'])
        if isinstance(version_data['tags'], str):
            tags = version_data['tags'].replace(',', ', ')
        else:
            tags = ''
        words = (version_data['training_words'].replace('[', '').replace(']', '')
                 .replace(', ', ',').replace(',', ', ').replace('"', '').rstrip(', '))

        creator_link = '<a href=https://civitai.com/user/' + version_data['creator_name'] + '>' + version_data['creator_name'] + '</a>'
        creator_tooltip = 'https://civitai.com/user/' + version_data['creator_name']

        creator = qtw.QLabel()
        creator.setText(creator_link)
        creator.setToolTip(creator_tooltip)
        creator.linkHovered.connect(self.link_hovered)
        creator.linkActivated.connect(self.link_clicked)

        model_link = '<a href="' + version_data['model_url'] + '">' + version_data['model_name'] + '</a>'
        model_tooltip = version_data['model_url']

        model = qtw.QLabel()
        model.setText(model_link)
        model.setToolTip(model_tooltip)
        model.linkHovered.connect(self.link_hovered)
        model.linkActivated.connect(self.link_clicked)

        version_link = '<a href="' + version_data['version_url'] + '">' + version_data['version_name'] + '</a>'
        version_tooltip = version_data['version_url']

        version = qtw.QLabel()
        version.setText(version_link)
        version.setToolTip(version_tooltip)
        version.linkHovered.connect(self.link_hovered)
        version.linkActivated.connect(self.link_clicked)

        self.tv_properties.setRowCount(13)
        self.tv_properties.setColumnCount(1)
        headers = ['Model Name', 'Model Version', 'Model Type', 'Base Model', 'Trigger Words', 'Tags', 'Creation Date',
                   'Last Updated', 'Date Added', 'Creator', 'Local Path', 'File Name', 'Hash']
        self.tv_properties.setRowCount(headers.__len__())
        self.tv_properties.setVerticalHeaderLabels(headers)

        q = qtw.QTableWidgetItem
        self.tv_properties.setCellWidget(0, 0, model)
        self.tv_properties.setCellWidget(1, 0, version)
        self.tv_properties.setItem(2, 0, q(version_data['model_type']))
        self.tv_properties.setItem(3, 0, q(version_data['base_model']))
        self.tv_properties.setItem(4, 0, q(words))
        self.tv_properties.setItem(5, 0, q(tags))
        self.tv_properties.setItem(6, 0, q(version_data['creation_date']))
        self.tv_properties.setItem(7, 0, q(version_data['updated_date']))
        self.tv_properties.setItem(8, 0, q(version_data['added_date']))
        self.tv_properties.setCellWidget(9, 0, creator)
        self.tv_properties.setItem(10, 0, q(version_data['version_path']))
        self.tv_properties.setItem(11, 0, q(version_data['version_file_name']))
        self.tv_properties.setItem(12, 0, q(version_data['version_hash']))

        html = '<!doctype html><html><head><meta charset=")utf-8"><title>images</title></head><body>'
        if version_data['version_json'] != '':
            v_json = json.loads(version_data['version_json'],)
            i_json = v_json.get('images')
            for image in i_json:
                html += '<img src="' + image.get('url') + '">'
        html += '</body></html>'
        self.we_images.setHtml(html)

        self.we_images.setMinimumHeight(1024)
        self.tv_properties.setFixedWidth(self.t_local.width() - 600)
        self.t_description.setFixedWidth(self.t_local.width() - 600)

    def link_hovered(self, e):
        pass

    def link_clicked(self, e):
        self.t_viewer.setCurrentWidget(self.t_web)
        self.we_web.load(e)

    def item_clicked(self, prompt, instance):
        print(prompt, instance)
        if prompt is True:
            qd = qtw.QInputDialog()
            qd.setTextValue("Test")
            file_name = qd.getText(self, "File Name?", "Input file name for model",
                                   qtw.QLineEdit.Normal,"Test")
        else:
            pass
            # get file name for path from table
        # write to db
            # versionid from table
            # instancename from function
            # filename = path + filename

        # deploy file (option as soft-link?)S
            # misc.safe_move(path,filename)
            # optional
                # os.makedirs(save_path_name + '/' + model_type + '/' + model_base_model + '/_' + tag, exist_ok=True)
                # os.symlink(my_target, my_link)

    def open_menu(self, position):
        """
        Show context menu.
        Originally copied from https://wiki.python.org/moin/PyQt/Handling%20context%20menus as:
        Sometimes, when we do not want to subclass a standard widget or use actions, it is easier to handle the context
        menu in a separate component, so we need a way for the widget to notify us when a context menu has been
        requested. We can do this by changing the policy to CustomContextMenu and connecting the widget's
        customContextMenuRequested() signal to a slot, method or function.

            * requires Widget.setContextMenuPolicy(Qt.CustomContextMenu)
            * and Widget.customContextMenuRequested.connect(open_menu)
            * add Widget to QMenu call (menu = qtw.QMenu(*self.tv_models_2*))
                * from: https://s-nako.work/2020/11/how-to-add-context-menu-into-qtreewidget/
            * https://doc.qt.io/qtforpython-6.2/PySide6/QtWidgets/QMenu.html

        :type position: objPySide6.QtCore.QPoint
        """
        context_menu = self.build_menu(self.tv_models_2)
        action = context_menu.exec(self.tv_models_2.mapToGlobal(position))

    @qtc.Slot()
    def open_image_menu(self, position):
        context_menu = self.build_menu(self.current_image)
        action = context_menu.exec(self.current_image.mapToGlobal(position))

    def build_menu(self, control):
        context_menu = qtw.QMenu(control)
        context_menu.addMenu(self.item_menu)
        context_menu.addMenu(self.item_menu_as)
        requery = context_menu.addAction('Requery CivitAi')
        requery.triggered.connect(self.requery)
        add_image = context_menu.addAction('Add Image')
        add_image.triggered.connect(self.add_image)
        return context_menu

    @qtc.Slot()
    def requery(self):
        pass

    @qtc.Slot()
    def add_image(self):
        pass

    def on_item_entered(self, it):
        """
        Show tooltip based on cell content
        Originally from https://stackoverflow.com/questions/53999740 for QTableWidget as:
        The ItemEntered signal must be used, but to do this, the mouseTracking must be enabled in addition to the item.
        When a row is added it does not imply that the items for each box exist, so I have modified it to create it.

        * ItemEntered needed to be replaced with entered in signal:
            self.tv_models_2.*ItemEntered*.connect(self.on_item_entered)
        * p and r needed to be assigned to actual control.
        * visualItemRect replaced with visualRect

        :param it: item returned from QTableView (QAbstractItemView) as (index – PySide6.QtCore.QModelIndex)
        """
        r = self.tv_models_2.visualRect(it)
        p = self.tv_models_2.viewport().mapToGlobal(qtc.QPoint(r.left(), r.top()))
        tv_model = self.tv_models_2.model()
        qtw.QToolTip.hideText()
        tv_index = tv_model.index(it.row(), it.column())
        item = tv_model.data(tv_index)
        qtw.QToolTip.showText(p, item, self.tv_models_2, r)

    def mousePressEvent(self, e):
        # print mouse position
        self.mouse_up = False
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        # print mouse position
        self.mouse_up = True
        super().mouseReleaseEvent(e)

    def mouseMoveEvent(self, e):
        if self.needs_resize:
            self.load_images()
        super().mouseMoveEvent(e)

    def resizeEvent(self, e):
        self.delay_resize2()
        super().resizeEvent(e)

    def delay_resize2(self):
        if mouse.is_pressed("left") is False:
            self.load_images()
            self.needs_resize = False
        else:
            self.needs_resize = True

    def delay_resize(self):
        if not self._flag:
            self._flag = True
            self.load_images()
            QtCore.QTimer.singleShot(2000, lambda: setattr(self, "_flag", False))

    def clearlayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().close()


    @qtc.Slot()
    def load_instance(self, s):
        if isinstance(s, int):
            if s == 0:
                self.f_instance1.setStyleSheet("background-color: #fff")
                self.f_instance2.setStyleSheet("background-color: #fff")
                self.lb_instance1.setStyleSheet("color: #000")
                self.lb_instance2.setStyleSheet("color: #000")
            else:
                item = self.instance_model.item(s, 0)
                bg_color = item.background().color().name()

                self.f_instance1.setStyleSheet("background-color:" + bg_color)
                self.f_instance2.setStyleSheet("background-color:" + bg_color)
                self.lb_instance1.setStyleSheet("color: #" + misc.max_contrasting_text_color(bg_color.lstrip('#')))
                self.lb_instance2.setStyleSheet("color: #" + misc.max_contrasting_text_color(bg_color.lstrip('#')))
        else:
            if isinstance(s, str) and s != 'No Instance Loaded':
                if s == '<none>':
                    s = 'No Instance Loaded'
                self.lb_instance1.setText(s)
                self.lb_instance2.setText(s)

    @qtc.Slot()
    def import_models(self):
        form = ImportForm()

        form.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        form.show()
        form.load_settings(self.settings)

    @qtc.Slot()
    def add_instance(self):
        form = InstanceForm()
        form.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        # this would not be needed if we did a Dialog
        form.instance_info_set.connect(self.update_instances)
        form.show()

    @qtc.Slot()
    def update_instances(self, n, c):
        item = qtg.QStandardItem(n)
        item.setBackground(qtg.QColor(c))
        fore_color = c.lstrip('#')
        fore_color = misc.max_contrasting_text_color(fore_color)
        fore_color = qtg.QColor.fromString('#' + fore_color)
        item.setForeground(fore_color)
        font = item.font()
        font.setBold(True)
        item.setFont(font)
        self.instance_model.appendRow(item)
        w_action = qtw.QWidgetAction(self)
        ql = MyLabel(w_action)
        ql.setText(item.text())
        ql.setStyleSheet("background-color: " + qtg.QColor(c).name() + "; color: " + fore_color.name())
        w_action.setDefaultWidget(ql)
        w_action.triggered.connect(
            lambda triggered=False, qlname=ql.text(): self.item_clicked(triggered, qlname)
        )
        self.item_menu.addAction(w_action)
        # todo: convert to function!
        # add_menu_item (menu, bgcolor, fgcolor, as, txt)
        w_action2 = qtw.QWidgetAction(self)
        ql2 = MyLabel(w_action2)
        ql2.setText(item.text())
        ql2.setStyleSheet("background-color: " + qtg.QColor(c).name() + "; color: " + fore_color.name())
        w_action2.setDefaultWidget(ql2)
        w_action2.triggered.connect(
            lambda triggered=True, qlname2=ql2.text(): self.item_clicked(triggered, qlname2)
        )
        self.item_menu_as.addAction(w_action2)

    def load_filter(self, s):

        self.model_model.setFilter(s)

    @qtc.Slot()
    def update_filter(self, s):
        if s != '':
            self.model_filter = '"Name - Version" LIKE "%{}%"'.format(s)
        else:
            self.model_filter = '"Name - Version" LIKE "%"'
        filter_str = self.model_filter + 'AND ' + self.type_filter + 'AND ' + self.base_filter
        self.model_model.setFilter(filter_str)

    @qtc.Slot()
    def mt_selected(self, s):
        loop = 0
        for index in self.lv_model_type.selectedIndexes():
            item = self.lv_model_type.model().data(index)
            if loop == 0:
                self.type_filter = '"Model Type" IN ("' + item + '"'
            else:
                self.type_filter = self.type_filter + ', "' + item + '"'
            loop = + 1
        if loop > 0:
            self.type_filter = self.type_filter + ')'
        else:
            self.type_filter = '"Model Type" LIKE "%"'

        filter_str = self.model_filter + 'AND ' + self.type_filter + 'AND ' + self.base_filter

        self.model_model.setFilter(filter_str)

    @qtc.Slot()
    def bm_selected(self, s):
        loop = 0
        for index in self.lv_base_model.selectedIndexes():
            item = self.lv_base_model.model().data(index)
            if loop == 0:
                self.base_filter = '"Base Model" IN ("' + item + '"'
            else:
                self.base_filter = self.base_filter + ', "' + item + '"'
            loop = + 1
        if loop > 0:
            self.base_filter = self.base_filter + ')'
        else:
            self.base_filter = '"Base Model" LIKE "%"'

        filter_str = self.model_filter + 'AND ' + self.type_filter + 'AND ' + self.base_filter

        self.model_model.setFilter(filter_str)

    @qtc.Slot()
    def on_resize(self, p, i):
        self.load_images()

    def show_hide_log(self):
        pass

    @qtc.Slot()
    def load_images(self):
        self.needs_resize = False
        tv_model = self.tv_models_2.model()
        if tv_model is not None:
            self.f_images.setFixedWidth(self.sa_images.width()-20)
            column = 0
            max_column = (self.f_images.width() / 96) - 1

            max_row = (self.f_images.height() / 108) - 1
            self.f_images.setGeometry(0, 0, self.f_images.width(), self.f_images.height() + 108)
            row = 0
            self.clearlayout(self.gl_images)
            for index in range(tv_model.rowCount()):
                tv_index = tv_model.index(index, 5)
                tv_text = tv_model.index(index, 0)
                item = tv_model.data(tv_index)
                tv_text = tv_model.data(tv_text)
                path = Path(basedir + '/none.webp')
                if exists(item + '.preview.jpeg'):
                    path = Path(item + '.preview.jpeg')
                gv = QLabel()
                gv.setAttribute(qtc.Qt.WA_DeleteOnClose)
                iv = QLabel()
                iv.setAttribute(qtc.Qt.WA_DeleteOnClose)
                iv.setText(str(tv_text))
                iv.setToolTip(str(tv_text))
                gv.setToolTip(str(tv_text))
                gv.setObjectName(str(index))
                gv.setStatusTip(str(index))
                iv.setWordWrap(True)
                iv.setMaximumWidth(90)
                iv.setMaximumHeight(40)  # font size *3.4
                iv.setAlignment(qtc.Qt.AlignTop)
                gv.setBackgroundRole(QPalette.Base)
                gv.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
                gv.setAlignment(qtc.Qt.AlignCenter)
                gv.setGeometry(0, 0, 90, 90)
                gv.setMinimumHeight(90)
                gv.setMaximumHeight(90)
                # gv.setAlignment(qtc.Qt.AlignTop)
                gv.setContextMenuPolicy(qtc.Qt.CustomContextMenu)
                gv.customContextMenuRequested.connect(self.open_image_menu)
                filename = str(path)
                reader = QImageReader(filename)
                newimage = reader.read()
                image = QPixmap.fromImage(newimage)
                gv.setPixmap(image.scaled(gv.size(), qtc.Qt.KeepAspectRatio, qtc.Qt.SmoothTransformation))
                self.gl_images.addWidget(gv, row, column)
                self.gl_images.addWidget(iv, row+1, column)
                column += 1
                if column > int(max_column):
                    self.gl_images.setRowMinimumHeight(row, 90)

                    self.gl_images.setRowMinimumHeight(row+1, 12)
                    column = 0
                    row += 2
                if row > int(max_row):
                    pass
                    # self.f_images.setGeometry(0, 0, self.f_images.width(), self.f_images.height()+108)
                self.gl_images.setColumnStretch(self.gl_images.columnCount() - 1, 100)
                self.gl_images.setRowStretch(self.gl_images.rowCount() - 1, 100)
                gv.mouseReleaseEvent = \
                    lambda mouseReleaseEvent, tvrow=gv.statusTip(): self.icon_clicked(mouseReleaseEvent, tvrow)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setOrganizationName("SmarttAii")
    app.setOrganizationDomain("smarttaii.com")
    app.setApplicationName("Smartt Model Manager")
    app.setStyle('Fusion')

    window = MainForm()  # class name
    # window.show()

    sys.exit(app.exec())

# implement Civitai link
#   remote download
#   feedback loop
#   monitor for download
# SQLite db
#   tags
#   model type
#   base model
#   comfyui id
#   description
#   version info
#   urls
#   hashes
#   filenames
# file system manager
#   monitor files currently applied
#   rename
#   preview image
#   optional other files
#   optional folder structure
# GUI
#   local Civitai style layout
#   treeview
#   search/filter/sort
# API?
#   ComfyUI Node?
