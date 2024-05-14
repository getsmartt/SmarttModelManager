import sys
from pathlib import Path

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg


from UI.settings_dialog import Ui_d_settings


class SettingsDialog(qtw.QDialog, Ui_d_settings):  # must match form type!
    settings_set = qtc.Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.accepted.connect(self.save_settings)
        self.settings = ''

    def iterItems(self, root):
        if root is not None:
            stack = [root]
            while stack:
                parent = stack.pop(0)
                for row in range(parent.rowCount()):
                    for column in range(parent.columnCount()):
                        child = parent.child(row, column)
                        yield child
                        if child.hasChildren():
                            stack.append(child)

    @qtc.Slot()
    def save_settings(self):
        # walk tree, look for changed settings and save them
        model = self.tw_settings.model()
        index_list = model.persistentIndexList()
        for index in index_list:
            item = model.itemFromIndex(index)
            data = model.data(index)

            if item.isEditable() is True:  # only editable items are settings
                value = item.text()
                updated = model.itemFromIndex(index.siblingAtColumn(2)).text()
                if updated == "true":  # only save changed settings
                    group = item.parent().text()
                    key = model.itemFromIndex(index.siblingAtColumn(0)).text()
                    self.settings.setValue(group + '/' + key, value)

    @qtc.Slot()
    def change_settings(self, tl, br):
        if tl.column() == 1:
            model = tl.model()
            sibling = model.itemFromIndex(tl.siblingAtColumn(2))
            model.setData(sibling.index(), "true", 0)

    def load_settings(self, settings):
        self.settings = settings
        self.tw_settings.columnCount = 3
        q = qtg.QStandardItem
        model = qtg.QStandardItemModel()
        self.tw_settings.setModel(model)
        model.dataChanged.connect(self.change_settings)
        headers = settings.allKeys()
        group_seen ={}
        for header in headers:
            group, key = header.split('/')
            group_item = group_seen.get(group, "None")
            if group_item == "None":
                group_item = q(group)
                group_item.setEditable(False)
                dummy_value = q()  # dummy value to allow for expansion
                dummy_value.setEditable(False)
                model.appendRow([group_item, dummy_value, q()])
                group_seen.update({group: group_item})
            key_item = q(key)
            key_item.setEditable(False)
            value = settings.value(header)
            value_item = q(value)
            group_item.appendRow([key_item, value_item, q("false")])
            if key in ["import_path", "storage_path", "db_path"]:  # needs button
                i = value_item.index()

                w = qtw.QPushButton()
                w.setObjectName(key)
                # w.setText(value)
                w.setFlat(True)  # make button flat so underlying data is visible
                w.setStyleSheet("text-align:left")
                w.setWhatsThis(str(i.row()))
                w.clicked.connect(
                    lambda checked=False, a=value, k=key, index=i:
                    self.button_clicked(checked, a, k, index)
                )
                # value_item.setText("")
                self.tw_settings.setIndexWidget(i, w)  # works

        self.tw_settings.expandAll()
        self.tw_settings.setColumnHidden(2, True)
        self.tw_settings.resizeColumnToContents(0)

    @qtc.Slot()
    def button_clicked(self, e, value, key, index):
        dir_name = qtw.QFileDialog.getExistingDirectory(self, "Select a " + key.replace("_", " ").capitalize(), value)
        p = Path(dir_name)
        model = index.model()
        model.setData(index, str(p), 0)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = SettingsDialog()  # class name
    window.show()

    sys.exit(app.exec())
