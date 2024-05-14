# from https://stackoverflow.com/a/75149586/13510414
# and https://stackoverflow.com/a/60528393/13510414

import logging
from PySide6.QtWidgets import QPlainTextEdit, QApplication
import PySide6.QtCore as QtCore

# Logging handler which receives any log created using the logging module.
# Contains a QPlainTextEdit which is automatically updated with logs.


class QTextEditLogger(logging.Handler):
    class Emitter(QtCore.QObject):
        log = QtCore.Signal(str)

    def __init__(self, parent):
        super().__init__()

        # create text edit widget
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

        # Create a QObject which will emit a signal for each log. This implicitly queues each
        # appendPlainText() call which makes it thread-safe
        self.emitter = QTextEditLogger.Emitter()
        self.emitter.log.connect(self.handle_it)

    def handle_it(self, record):
        self.widget.appendPlainText(record)
        self.widget.verticalScrollBar().setValue(self.widget.verticalScrollBar().maximum())
        QApplication.processEvents()

    # override Handler's emit method (this happens to share a name with Qt's emit method.
    # Don't get confused)
    def emit(self, record):
        msg = self.format(record)
        self.emitter.log.emit(msg)
