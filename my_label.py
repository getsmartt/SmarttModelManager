import sys
from PySide6 import QtWidgets


class MyLabel(QtWidgets.QLabel):
    def __init__(self, action):
        super(MyLabel, self).__init__()
        self.action = action

    def mouseReleaseEvent(self, e):
        self.action.trigger()
