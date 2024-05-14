import json
import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QFileDialog, QMessageBox, QColorDialog
from pathlib import Path

from UI.instance_window import Ui_w_instance
from custom_paths import PathDialog
import misc

import sqlite3
from contextlib import closing


class InstanceForm(qtw.QMainWindow, Ui_w_instance):  # must match form type!

    destination_is_set = False
    instance_info_set = qtc.Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        form_font = self.font()
        form_font.setPointSize(12)
        self.setFont(form_font)

        self.color = misc.random_color()
        fore_color = self.color.lstrip('#')
        fore_color = misc.max_contrasting_text_color(fore_color)
        self.le_name.setStyleSheet("color: #" + fore_color + "; background-color:" + self.color)

        headers = ('Model Type', 'Model Path')
        self.lineEdit_16.setColumnCount(2)
        self.lineEdit_16.setHorizontalHeaderLabels(headers)

        #  loop widgets assign checkbox stateChanged signal to unified slot
        cblist = self.groupBox.findChildren(qtw.QCheckBox)

        for cb in cblist:
            cb.stateChanged.connect(
                lambda stateChanged, cbname=cb.objectName(), cbtext=cb.text(): self.toggle_le_enabled(stateChanged, cbname, cbtext)
            )

        tblist = self.groupBox.findChildren(qtw.QToolButton)

        for tb in tblist:
            tb.clicked.connect(
                lambda checked=False, tbname=tb.objectName(): self.tb_clicked(tbname)
            )

        ffont = self.font()
        ffont.setPointSize(12)
        self.setFont(ffont)

        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.accepted.connect(self.save_instance)
        self.pb_destination.clicked.connect(self.set_destination)
        self.pb_color.clicked.connect(self.get_color)
        self.tb_add.clicked.connect(self.add_path)


        self.pform = PathDialog()
        self.pform.path_info_set.connect(self.add_path_returned)


    @qtc.Slot()
    def toggle_le_enabled(self, state, cb, name):
         # get checkbox name
        # parse ending number
        # toggle lineedit enabled based on state
        cb_suffix = cb.removeprefix('checkBox')
        le_name = 'lineEdit'+cb_suffix
        le = self.findChild(qtw.QWidget, le_name)
        le.setStatusTip(name)
        le.setEnabled(bool(state))
        # toggle toolbutton enabled based on state
        tb_name = 'toolButton' + cb_suffix
        tb = self.findChild(qtw.QWidget, tb_name)
        tb.setStatusTip(name)
        tb.setEnabled(bool(state))

    @qtc.Slot()
    def tb_clicked(self, tb):
        print(tb)
        name = self.findChild(qtw.QWidget, tb).statusTip()
        tb_suffix = tb.removeprefix('toolButton')

        if tb.startswith('toolButton'):
            if self.destination_is_set is True:
                dir = self.le_destination.text()
                dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory for " + name, dir)
                dir_name = dir_name.replace(dir, '{destination}')
            else:
                dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory for " + name)
            le_name = 'lineEdit' + tb_suffix
            le = self.findChild(qtw.QWidget, le_name)

            if dir_name:
                path = Path(dir_name)
                # le.setReadOnly(False)
                le.setText(dir_name)
                # le.setReadOnly(True)

    @qtc.Slot()
    def add_path(self):
        self.lineEdit_16.setRowCount(self.lineEdit_16.rowCount() + 1)
        self.pform.default_path = self.le_destination.text()
        self.pform.exec()

    @qtc.Slot()
    def add_path_returned(self, model_type, model_path):
        item_type = qtw.QTableWidgetItem(model_type)
        item_path = qtw.QTableWidgetItem(model_path)
        row = self.lineEdit_16.rowCount() - 1
        self.lineEdit_16.setItem(row, 0, item_type)
        self.lineEdit_16.setItem(row, 1, item_path)


    @qtc.Slot()
    def save_instance(self):
        if self.destination_is_set is True and self.le_name.text() != '':
            # loop enabled le's and create list of paths to save
            # call save function
            lelist = self.groupBox.findChildren(qtw.QLineEdit)
            default_paths = dict()
            custom_paths = dict()

            for le in lelist:
                if le.isEnabled() is True:
                    default_paths[le.statusTip()] = le.text()
            if self.lineEdit_16.isEnabled() is True:
                rows = self.lineEdit_16.rowCount()

                for row in range(rows):

                    custom_paths[self.lineEdit_16.item(row, 0).text()] = self.lineEdit_16.item(row, 1).text()
                default_paths['Custom Paths'] = custom_paths

            instance_parameters = (self.le_name.text(), str(Path(self.le_destination.text())), json.dumps(default_paths)
                                   , self.color)
            try:
                with closing(sqlite3.connect("manager")) as connection:
                    with closing(connection.cursor()) as cursor:
                        query = ("INSERT OR IGNORE INTO main.instances (name, path, custompaths, color) "
                                 "VALUES (?,?,?,?);")
                        cursor.execute(query, instance_parameters)
                        connection.commit()
                self.instance_info_set.emit(self.le_name.text(), self.color)
                self.close()

            except sqlite3.Error as error:
                print("Failed to insert Creator into manager", error)


        else:
            # warn user to provide valid directories
            QMessageBox.warning(self, "Error", "Please set the Destination Path and Instance Name")

    @qtc.Slot()
    def set_destination(self):
        dir_name2 = QFileDialog.getExistingDirectory(self, "Select a Destination Directory")
        if dir_name2:
            path = Path(dir_name2)
            self.destination_is_set = True
            self.le_destination.setText(dir_name2)

    @qtc.Slot()
    def get_color(self):
        color = QColorDialog.getColor()
        self.color = color.name()
        if color.isValid():
            fore_color = color.name().lstrip('#')
            fore_color = misc.max_contrasting_text_color(fore_color)
            self.le_name.setStyleSheet("color: #" + fore_color + "; background-color:" + color.name())

    def mousePressEvent(self, e):

        super().mousePressEvent(e)

    def focusInEvent(self, e):

        super().focusInEvent(e)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = InstanceForm()  # class name
    window.show()

    sys.exit(app.exec())
