#!/usr/bin/python3

import os
import sys
from PySide6.QtWidgets import QProgressBar, QApplication, QDialog, QMainWindow, QPushButton
from PySide6.QtCore import QThread, Signal, Slot
import PySide6.QtCore as QtCore

class ProgressDialog(QDialog):
    move_done = Signal(bool)

    def __init__(self, parent, source, destination, file_name, move=False):
        QDialog.__init__(self, parent)

        self.resize(400, 50)
        if move:
            self.setWindowTitle(f"Moving file {file_name}...")
        else:
            self.setWindowTitle(f"Copying file {file_name}...")
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.parent = parent
        self.source = source
        self.destination = destination
        self.file_name = file_name
        self.move = move

        self.prog = QProgressBar(self)
        self.prog.setGeometry(10, 10, 380, 30)
        self.prog.setMaximum(100)
        self.prog.setMinimum(0)
        self.prog.setFormat("%p%")

    def start(self):
        self.show()
        self.copy()

    def copy(self):
        self.move_done.emit(False)
        copy_thread = CopyThread(self, self.source, self.destination)
        copy_thread.procPartDone.connect(self.update_progress)
        copy_thread.procDone.connect(self.finished_copy)
        copy_thread.start()

    def update_progress(self, progress):
        self.prog.setValue(progress)

    def finished_copy(self, state):
        self.move_done.emit(True)
        if self.move:
            os.remove(self.source)
        self.close()


class CopyThread(QThread):
    procDone = Signal(bool)
    procPartDone = Signal(int)

    def __init__(self, parent, source: str, destination: str):
        QThread.__init__(self, parent)

        self.source = source
        self.destination = destination

    def run(self):
        self.copy()
        self.procDone.emit(True)

    def copy(self):
        source_size = os.stat(self.source).st_size
        copied = 0

        with open(self.source, "rb") as source, open(self.destination, "wb") as target:
            while True:
                chunk = source.read(1024)
                if not chunk:
                    break

                target.write(chunk)
                copied += len(chunk)

                self.procPartDone.emit(copied * 100 / source_size)
