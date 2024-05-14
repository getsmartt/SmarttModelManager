# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
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
    QGridLayout, QHeaderView, QSizePolicy, QTreeView,
    QWidget)

class Ui_d_settings(object):
    def setupUi(self, d_settings):
        if not d_settings.objectName():
            d_settings.setObjectName(u"d_settings")
        d_settings.resize(667, 474)
        self.gridLayout = QGridLayout(d_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(d_settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.tw_settings = QTreeView(d_settings)
        self.tw_settings.setObjectName(u"tw_settings")
        self.tw_settings.setAlternatingRowColors(True)

        self.gridLayout.addWidget(self.tw_settings, 0, 0, 1, 1)


        self.retranslateUi(d_settings)
        self.buttonBox.accepted.connect(d_settings.accept)
        self.buttonBox.rejected.connect(d_settings.reject)

        QMetaObject.connectSlotsByName(d_settings)
    # setupUi

    def retranslateUi(self, d_settings):
        d_settings.setWindowTitle(QCoreApplication.translate("d_settings", u"Settings", None))
    # retranslateUi

