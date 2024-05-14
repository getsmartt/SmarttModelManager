import sys
import os
from os.path import exists
from pathlib import Path
import mouse  # used to control resize

from PySide6 import QtCore as qtc, QtCore, QtGui
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QPalette, QImageReader, QPixmap, QMouseEvent
from PySide6.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery, QSqlQueryModel
import sqlite3
from contextlib import closing

from PySide6.QtWidgets import QLabel, QSizePolicy

import misc
from UI.main_window2 import Ui_w_main
from importer import ImportForm
from instance import InstanceForm
from my_label import MyLabel

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
        self.setupUi(self)

        self.show()

        self.model_filter = '"Name - Version" LIKE "%"'
        self.base_filter = '"Model Type" LIKE "%"'
        self.type_filter = '"Base Model" LIKE "%"'
        self.tag_filter = 'Tags LIKE "%"'

        form_font = self.font()
        form_font.setPointSize(12)
        self.setFont(form_font)

        self.setWindowTitle('Smartt Model Manager')
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("No Instance Loaded")
        self.label_3.setText("No Instance Loaded")
        self.splitter_2.moveSplitter(119, 1)
        self.splitter.moveSplitter(567, 1)
        self.actionImport_Models.triggered.connect(self.import_models)
        self.actionNew_Instance.triggered.connect(self.add_instance)
        self.le_search.textChanged.connect(self.update_filter)
        self.lv_model_type.clicked.connect(self.mt_selected)
        self.lv_base_model.clicked.connect(self.bm_selected)
        self.splitter.splitterMoved.connect(self.on_resize)
        self.splitter_2.splitterMoved.connect(self.on_resize)

        type_query = QSqlQuery('SELECT DISTINCT'
                               ' m."type" AS "Model Type"'
                               ' FROM models m;', db=db)

        base_query = QSqlQuery('SELECT DISTINCT'
                               ' v.basemodel'
                               ' FROM versions v;', db=db)

        self.model_model = QSqlTableModel(db=db)
        self.model_model.setTable('v_models_versions')
        self.tv_models.setModel(self.model_model)
        self.model_model.select()
        self.tv_models.setColumnHidden(6, True)
        self.tv_models.setColumnHidden(7, True)
        self.tv_models.resizeColumnsToContents()
        self.model_model.modelReset.connect(self.load_images)

        self.type_model = QSqlQueryModel()
        self.lv_model_type.setModel(self.type_model)
        self.type_model.setQuery(type_query)

        self.base_model = QSqlQueryModel()
        self.lv_base_model.setModel(self.base_model)
        self.base_model.setQuery(base_query)
        self.load_images()

        self.instance_box = qtw.QComboBox()
        self.instance_box.currentTextChanged.connect(self.load_instance)
        self.instance_box.currentIndexChanged.connect(self.load_instance)
        self.instance_model = self.instance_box.model()
        item = qtg.QStandardItem('<none>')
        self.instance_model.appendRow(item)
        self.tv_models.setMouseTracking(True)
        self.tv_models.entered.connect(self.on_item_entered)
        self.tv_models.setContextMenuPolicy(qtc.Qt.CustomContextMenu)
        self.tv_models.customContextMenuRequested.connect(self.open_menu)
        self.item_menu = qtw.QMenu(self.tv_models)
        self.item_menu.setTitle('Deploy to:')
        self.item_menu_as = qtw.QMenu(self.tv_models)
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
        self.toolBar.insertWidget(self.actionNew_Instance, self.instance_label)
        self.instance_box.setFocusPolicy(qtc.Qt.NoFocus)
        self.toolBar.addWidget(self.instance_box)
        self.toolBar.addSeparator()

    def item_clicked(self, prompt, instance):
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
            * add Widget to QMenu call (menu = qtw.QMenu(*self.tv_models*))
                * from: https://s-nako.work/2020/11/how-to-add-context-menu-into-qtreewidget/
            * https://doc.qt.io/qtforpython-6.2/PySide6/QtWidgets/QMenu.html

        :type position: objPySide6.QtCore.QPoint
        """
        context_menu = qtw.QMenu(self.tv_models)
        context_menu.addMenu(self.item_menu)
        context_menu.addMenu(self.item_menu_as)
        action = context_menu.exec(self.tv_models.mapToGlobal(position))
        print(action)

    def on_item_entered(self, it):
        """
        Show tooltip based on cell content
        Originally from https://stackoverflow.com/questions/53999740 for QTableWidget as:
        The ItemEntered signal must be used, but to do this, the mouseTracking must be enabled in addition to the item.
        When a row is added it does not imply that the items for each box exist, so I have modified it to create it.

        * ItemEntered needed to be replaced with entered in signal:
            self.tv_models.*ItemEntered*.connect(self.on_item_entered)
        * p and r needed to be assigned to actual control.
        * visualItemRect replaced with visualRect

        :param it: item returned from QTableView (QAbstractItemView) as (index – PySide6.QtCore.QModelIndex)
        """
        r = self.tv_models.visualRect(it)
        p = self.tv_models.viewport().mapToGlobal(qtc.QPoint(r.left(), r.top()))
        tv_model = self.tv_models.model()
        qtw.QToolTip.hideText()
        tv_index = tv_model.index(it.row(), it.column())
        item = tv_model.data(tv_index)
        qtw.QToolTip.showText(p, item, self.tv_models, r)

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
                self.frame_4.setStyleSheet("background-color: #fff")
                self.frame_5.setStyleSheet("background-color: #fff")
                self.label.setStyleSheet("color: #000")
                self.label_3.setStyleSheet("color: #000")
            else:
                item = self.instance_model.item(s, 0)
                bg_color = item.background().color().name()

                self.frame_4.setStyleSheet("background-color:" + bg_color)
                self.frame_5.setStyleSheet("background-color:" + bg_color)
                self.label.setStyleSheet("color: #" + misc.max_contrasting_text_color(bg_color.lstrip('#')))
                self.label_3.setStyleSheet("color: #" + misc.max_contrasting_text_color(bg_color.lstrip('#')))
        else:
            if isinstance(s, str) and s != 'No Instance Loaded':
                if s == '<none>':
                    s = 'No Instance Loaded'
                self.label.setText(s)
                self.label_3.setText(s)

    @qtc.Slot()
    def import_models(self):
        self.form = ImportForm()
        self.form.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        # this would not be needed if we did a Dialog
        self.form.show()

    @qtc.Slot()
    def add_instance(self):
        self.form = InstanceForm()
        self.form.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        # this would not be needed if we did a Dialog
        self.form.instance_info_set.connect(self.update_instances)
        self.form.show()

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

    @qtc.Slot()
    def load_images(self):
        self.needs_resize = False
        tv_model = self.tv_models.model()
        if tv_model is not None:
            self.frame.setFixedWidth(self.scrollArea.width()-20)
            column = 0
            max_column = (self.frame.width() / 96) - 1

            max_row = (self.frame.height() / 108) - 1
            self.frame.setGeometry(0, 0, self.frame.width(), self.frame.height() + 108)
            row = 0
            self.clearlayout(self.gridLayout_8)
            for index in range(tv_model.rowCount()):
                tv_index = tv_model.index(index, 5)
                tv_text = tv_model.index(index, 0)
                item = tv_model.data(tv_index)
                tv_text = tv_model.data(tv_text)
                path = Path(basedir + '/none.jpg')
                if exists(item + '.preview.jpeg'):
                    path = Path(item + '.preview.jpeg')
                gv = QLabel()
                iv = QLabel()
                iv.setText(str(tv_text))
                iv.setToolTip(str(tv_text))
                gv.setToolTip(str(tv_text))
                iv.setWordWrap(True)
                iv.setMaximumWidth(90)
                iv.setMaximumHeight(40)  # font size *3.4
                iv.setAlignment(qtc.Qt.AlignTop)
                gv.setBackgroundRole(QPalette.Base)
                gv.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
                gv.setScaledContents(True)
                gv.setGeometry(0, 0, 90, 90)
                gv.setMinimumHeight(90)
                filename = str(path)
                reader = QImageReader(filename)
                newimage = reader.read()
                gv.setPixmap(QPixmap.fromImage(newimage))
                self.gridLayout_8.addWidget(gv, row, column)
                self.gridLayout_8.addWidget(iv, row+1, column)
                column += 1
                if column > int(max_column):
                    self.gridLayout_8.setRowMinimumHeight(row, 90)
                    self.gridLayout_8.setRowMinimumHeight(row+1, 12)
                    column = 0
                    row += 2
                if row > int(max_row):
                    self.frame.setGeometry(0, 0, self.frame.width(), self.frame.height()+108)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

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
