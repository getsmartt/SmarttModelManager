# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,
    QFrame, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_w_import(object):
    def setupUi(self, w_import):
        if not w_import.objectName():
            w_import.setObjectName(u"w_import")
        w_import.resize(777, 864)
        self.centralwidget = QWidget(w_import)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.le_destination = QLineEdit(self.centralwidget)
        self.le_destination.setObjectName(u"le_destination")

        self.gridLayout_2.addWidget(self.le_destination, 1, 1, 1, 1)

        self.le_source = QLineEdit(self.centralwidget)
        self.le_source.setObjectName(u"le_source")

        self.gridLayout_2.addWidget(self.le_source, 0, 1, 1, 1)

        self.pb_source = QPushButton(self.centralwidget)
        self.pb_source.setObjectName(u"pb_source")
        self.pb_source.setMinimumSize(QSize(0, 0))
        self.pb_source.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_2.addWidget(self.pb_source, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 560))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, 0, 0)
        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_3.addWidget(self.checkBox_3, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_11, 9, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_7, 6, 1, 1, 1)

        self.checkBox_15 = QCheckBox(self.groupBox)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout_3.addWidget(self.checkBox_15, 13, 0, 1, 1)

        self.checkBox_13 = QCheckBox(self.groupBox)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout_3.addWidget(self.checkBox_13, 11, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_12, 10, 1, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_3.addWidget(self.checkBox_5, 4, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_3.addWidget(self.checkBox_4, 3, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_3.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.groupBox)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_3.addWidget(self.checkBox_7, 6, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_15, 13, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.groupBox)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_14, 12, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 15))

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.groupBox)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_13, 11, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_3.addWidget(self.checkBox_6, 5, 0, 1, 1)

        self.checkBox_16 = QCheckBox(self.groupBox)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout_3.addWidget(self.checkBox_16, 14, 0, 1, 1)

        self.lineEdit_16 = QPlainTextEdit(self.groupBox)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_16, 14, 1, 2, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_10, 8, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_8, 7, 1, 1, 1)

        self.checkBox_14 = QCheckBox(self.groupBox)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout_3.addWidget(self.checkBox_14, 12, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_6, 5, 1, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.checkBox_8 = QCheckBox(self.groupBox)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_3.addWidget(self.checkBox_8, 7, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.checkBox_10 = QCheckBox(self.groupBox)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_3.addWidget(self.checkBox_10, 8, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.groupBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 16, 1, 1, 1)

        self.checkBox_11 = QCheckBox(self.groupBox)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_3.addWidget(self.checkBox_11, 9, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.groupBox)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout_3.addWidget(self.checkBox_12, 10, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 2)

        self.pb_destination = QPushButton(self.centralwidget)
        self.pb_destination.setObjectName(u"pb_destination")
        self.pb_destination.setMinimumSize(QSize(0, 0))
        self.pb_destination.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_2.addWidget(self.pb_destination, 1, 0, 1, 1)

        self.w_logger = QWidget(self.centralwidget)
        self.w_logger.setObjectName(u"w_logger")
        self.verticalLayout = QVBoxLayout(self.w_logger)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.w_logger)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.gridLayout_2.addWidget(self.w_logger, 3, 0, 1, 2)

        w_import.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_import)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 777, 22))
        w_import.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(w_import)
        self.statusbar.setObjectName(u"statusbar")
        w_import.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pb_source, self.pb_destination)
        QWidget.setTabOrder(self.pb_destination, self.le_destination)
        QWidget.setTabOrder(self.le_destination, self.le_source)

        self.retranslateUi(w_import)

        QMetaObject.connectSlotsByName(w_import)
    # setupUi

    def retranslateUi(self, w_import):
        w_import.setWindowTitle(QCoreApplication.translate("w_import", u"Import Models", None))
        self.pb_source.setText(QCoreApplication.translate("w_import", u"Source", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_import", u"Model Types and folders to import!", None))
        self.checkBox_3.setText(QCoreApplication.translate("w_import", u"Controlnet", None))
        self.lineEdit_5.setText(QCoreApplication.translate("w_import", u"\\hypernetworks", None))
        self.lineEdit_11.setText(QCoreApplication.translate("w_import", u"\\embeddings", None))
        self.lineEdit_2.setText(QCoreApplication.translate("w_import", u"\\checkpoints", None))
        self.lineEdit_7.setText(QCoreApplication.translate("w_import", u"\\loras", None))
        self.checkBox_15.setText(QCoreApplication.translate("w_import", u"Workflows", None))
        self.checkBox_13.setText(QCoreApplication.translate("w_import", u"VAE", None))
        self.lineEdit_12.setText(QCoreApplication.translate("w_import", u"\\upscale_models", None))
        self.checkBox_5.setText(QCoreApplication.translate("w_import", u"Hypernetwork", None))
        self.checkBox_4.setText(QCoreApplication.translate("w_import", u"DoRa", None))
        self.checkBox_2.setText(QCoreApplication.translate("w_import", u"Checkpoint", None))
        self.checkBox_7.setText(QCoreApplication.translate("w_import", u"LoCon", None))
        self.lineEdit_15.setText(QCoreApplication.translate("w_import", u"\\Workflows", None))
        self.lineEdit_14.setText(QCoreApplication.translate("w_import", u"\\Wildcards", None))
        self.lineEdit_3.setText(QCoreApplication.translate("w_import", u"\\ControlNet", None))
        self.checkBox.setText(QCoreApplication.translate("w_import", u"Aesthetic Gradient", None))
        self.lineEdit_13.setText(QCoreApplication.translate("w_import", u"\\VAE", None))
        self.checkBox_6.setText(QCoreApplication.translate("w_import", u"LoRa", None))
        self.checkBox_16.setText(QCoreApplication.translate("w_import", u"Other Paths?", None))
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("w_import", u"Add Additional Paths one per line", None))
        self.lineEdit_10.setText(QCoreApplication.translate("w_import", u"\\poses", None))
        self.lineEdit_8.setText(QCoreApplication.translate("w_import", u"\\MotionModule", None))
        self.checkBox_14.setText(QCoreApplication.translate("w_import", u"Wildcards", None))
        self.lineEdit_6.setText(QCoreApplication.translate("w_import", u"\\loras", None))
        self.lineEdit.setText(QCoreApplication.translate("w_import", u"\\Aesthetic gradients", None))
        self.checkBox_8.setText(QCoreApplication.translate("w_import", u"Motion Module", None))
        self.lineEdit_4.setText(QCoreApplication.translate("w_import", u"\\loras", None))
        self.checkBox_10.setText(QCoreApplication.translate("w_import", u"Poses", None))
        self.checkBox_11.setText(QCoreApplication.translate("w_import", u"Textual Inversion", None))
        self.checkBox_12.setText(QCoreApplication.translate("w_import", u"Upscaler", None))
        self.pb_destination.setText(QCoreApplication.translate("w_import", u"Destination", None))
        self.label.setText(QCoreApplication.translate("w_import", u"Logging", None))
    # retranslateUi

