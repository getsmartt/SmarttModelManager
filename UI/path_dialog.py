# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'path_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_d_path(object):
    def setupUi(self, d_path):
        if not d_path.objectName():
            d_path.setObjectName(u"d_path")
        d_path.resize(400, 100)
        self.verticalLayout = QVBoxLayout(d_path)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(d_path)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_name = QLineEdit(self.widget)
        self.le_name.setObjectName(u"le_name")
        font = QFont()
        font.setBold(True)
        self.le_name.setFont(font)

        self.horizontalLayout.addWidget(self.le_name)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(d_path)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(d_path)
        self.buttonBox.accepted.connect(d_path.accept)
        self.buttonBox.rejected.connect(d_path.reject)

        QMetaObject.connectSlotsByName(d_path)
    # setupUi

    def retranslateUi(self, d_path):
        d_path.setWindowTitle(QCoreApplication.translate("d_path", u"Custom Paths", None))
        self.label.setText(QCoreApplication.translate("d_path", u"Name", None))
    # retranslateUi

