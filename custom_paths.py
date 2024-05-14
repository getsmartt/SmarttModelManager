import sys
from pathlib import Path

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.path_dialog import Ui_d_path


class PathDialog(qtw.QDialog, Ui_d_path):  # must match form type!

    path_info_set = qtc.Signal(str,str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.default_path = str(Path.home())

        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.accepted.connect(self.add_path)

    @qtc.Slot()
    def add_path(self):
        model_type = self.le_name.text()
        model_path = qtw.QFileDialog.getExistingDirectory(self, "Select a Directory for " + model_type)
        self.path_info_set.emit(model_type, model_path)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = PathDialog()  # class name
    window.show()

    sys.exit(app.exec())
