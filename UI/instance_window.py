# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instance_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialogButtonBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

class Ui_w_instance(object):
    def setupUi(self, w_instance):
        if not w_instance.objectName():
            w_instance.setObjectName(u"w_instance")
        w_instance.resize(717, 708)
        self.centralwidget = QWidget(w_instance)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_destination = QPushButton(self.centralwidget)
        self.pb_destination.setObjectName(u"pb_destination")
        self.pb_destination.setMinimumSize(QSize(0, 0))
        self.pb_destination.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_2.addWidget(self.pb_destination, 1, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.pb_color = QPushButton(self.centralwidget)
        self.pb_color.setObjectName(u"pb_color")
        self.pb_color.setMinimumSize(QSize(0, 0))
        self.pb_color.setMaximumSize(QSize(125, 16777215))

        self.gridLayout_2.addWidget(self.pb_color, 0, 2, 1, 1)

        self.le_destination = QLineEdit(self.centralwidget)
        self.le_destination.setObjectName(u"le_destination")

        self.gridLayout_2.addWidget(self.le_destination, 1, 1, 1, 2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(True)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, -1, 0, 0)
        self.toolButton_15 = QToolButton(self.groupBox)
        self.toolButton_15.setObjectName(u"toolButton_15")
        self.toolButton_15.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_15, 13, 2, 1, 1)

        self.toolButton_10 = QToolButton(self.groupBox)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_10, 8, 2, 1, 1)

        self.toolButton_2 = QToolButton(self.groupBox)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_2, 1, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_3.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 15))

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)

        self.toolButton = QToolButton(self.groupBox)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton, 0, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_5, 4, 1, 1, 1)

        self.checkBox_16 = QCheckBox(self.groupBox)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout_3.addWidget(self.checkBox_16, 15, 0, 1, 1)

        self.toolButton_5 = QToolButton(self.groupBox)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_5, 4, 2, 1, 1)

        self.lineEdit_12 = QLineEdit(self.groupBox)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_12, 10, 1, 1, 1)

        self.checkBox_13 = QCheckBox(self.groupBox)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout_3.addWidget(self.checkBox_13, 11, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.groupBox)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_14, 12, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_3.addWidget(self.checkBox_4, 3, 0, 1, 1)

        self.toolButton_11 = QToolButton(self.groupBox)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_11, 9, 2, 1, 1)

        self.checkBox_14 = QCheckBox(self.groupBox)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout_3.addWidget(self.checkBox_14, 12, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.groupBox)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout_3.addWidget(self.checkBox_12, 10, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.groupBox)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_13, 11, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_3.addWidget(self.checkBox_3, 2, 0, 1, 1)

        self.toolButton_6 = QToolButton(self.groupBox)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_6, 5, 2, 1, 1)

        self.toolButton_14 = QToolButton(self.groupBox)
        self.toolButton_14.setObjectName(u"toolButton_14")
        self.toolButton_14.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_14, 12, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.toolButton_8 = QToolButton(self.groupBox)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_8, 7, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.toolButton_13 = QToolButton(self.groupBox)
        self.toolButton_13.setObjectName(u"toolButton_13")
        self.toolButton_13.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_13, 11, 2, 1, 1)

        self.checkBox_10 = QCheckBox(self.groupBox)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_3.addWidget(self.checkBox_10, 8, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_15, 13, 1, 1, 1)

        self.checkBox_8 = QCheckBox(self.groupBox)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_3.addWidget(self.checkBox_8, 7, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.toolButton_12 = QToolButton(self.groupBox)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_12, 10, 2, 1, 1)

        self.checkBox_7 = QCheckBox(self.groupBox)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_3.addWidget(self.checkBox_7, 6, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_3.addWidget(self.checkBox_6, 5, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.groupBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.gridLayout_3.addWidget(self.buttonBox, 17, 0, 1, 2)

        self.checkBox_11 = QCheckBox(self.groupBox)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_3.addWidget(self.checkBox_11, 9, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_11, 9, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_10, 8, 1, 1, 1)

        self.toolButton_3 = QToolButton(self.groupBox)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_3, 2, 2, 1, 1)

        self.toolButton_7 = QToolButton(self.groupBox)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_7, 6, 2, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_7, 6, 1, 1, 1)

        self.checkBox_15 = QCheckBox(self.groupBox)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout_3.addWidget(self.checkBox_15, 13, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_6, 5, 1, 1, 1)

        self.toolButton_4 = QToolButton(self.groupBox)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setEnabled(False)

        self.gridLayout_3.addWidget(self.toolButton_4, 3, 2, 1, 1)

        self.toolButton_16 = QWidget(self.groupBox)
        self.toolButton_16.setObjectName(u"toolButton_16")
        self.toolButton_16.setEnabled(False)
        self.verticalLayout = QVBoxLayout(self.toolButton_16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tb_add = QToolButton(self.toolButton_16)
        self.tb_add.setObjectName(u"tb_add")

        self.verticalLayout.addWidget(self.tb_add)

        self.tb_edit = QToolButton(self.toolButton_16)
        self.tb_edit.setObjectName(u"tb_edit")

        self.verticalLayout.addWidget(self.tb_edit)

        self.tb_delete = QToolButton(self.toolButton_16)
        self.tb_delete.setObjectName(u"tb_delete")

        self.verticalLayout.addWidget(self.tb_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_3.addWidget(self.toolButton_16, 15, 2, 2, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_8, 7, 1, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_3.addWidget(self.checkBox_5, 4, 0, 1, 1)

        self.lineEdit_16 = QTableWidget(self.groupBox)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setEnabled(False)
        self.lineEdit_16.setDefaultDropAction(Qt.IgnoreAction)
        self.lineEdit_16.setAlternatingRowColors(True)
        self.lineEdit_16.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lineEdit_16.horizontalHeader().setStretchLastSection(True)
        self.lineEdit_16.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.lineEdit_16, 15, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 44))
        self.groupBox_2.setFlat(True)
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 6)
        self.rb_custom = QRadioButton(self.groupBox_2)
        self.rb_custom.setObjectName(u"rb_custom")
        self.rb_custom.setChecked(True)

        self.horizontalLayout.addWidget(self.rb_custom)

        self.rb_a1111 = QRadioButton(self.groupBox_2)
        self.rb_a1111.setObjectName(u"rb_a1111")

        self.horizontalLayout.addWidget(self.rb_a1111)

        self.rb_comfyui = QRadioButton(self.groupBox_2)
        self.rb_comfyui.setObjectName(u"rb_comfyui")

        self.horizontalLayout.addWidget(self.rb_comfyui)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 3)

        self.le_name = QLineEdit(self.centralwidget)
        self.le_name.setObjectName(u"le_name")
        font = QFont()
        font.setBold(True)
        self.le_name.setFont(font)

        self.gridLayout_2.addWidget(self.le_name, 0, 1, 1, 1)

        w_instance.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_instance)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 717, 22))
        w_instance.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(w_instance)
        self.statusBar.setObjectName(u"statusBar")
        w_instance.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.pb_destination, self.le_destination)

        self.retranslateUi(w_instance)

        QMetaObject.connectSlotsByName(w_instance)
    # setupUi

    def retranslateUi(self, w_instance):
        w_instance.setWindowTitle(QCoreApplication.translate("w_instance", u"Add Instance", None))
        self.pb_destination.setText(QCoreApplication.translate("w_instance", u"Destination", None))
        self.label.setText(QCoreApplication.translate("w_instance", u"Name", None))
        self.pb_color.setText(QCoreApplication.translate("w_instance", u"Color", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_instance", u"Set Custom Paths (Optional, but recommended)", None))
        self.toolButton_15.setText(QCoreApplication.translate("w_instance", u"...", None))
        self.toolButton_10.setText(QCoreApplication.translate("w_instance", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("w_instance", u"...", None))
        self.checkBox_2.setText(QCoreApplication.translate("w_instance", u"Checkpoints", None))
#if QT_CONFIG(statustip)
        self.checkBox.setStatusTip(QCoreApplication.translate("w_instance", u"Enable Aesthetic Gradients Path", None))
#endif // QT_CONFIG(statustip)
        self.checkBox.setText(QCoreApplication.translate("w_instance", u"Aesthetic Gradients", None))
#if QT_CONFIG(statustip)
        self.toolButton.setStatusTip(QCoreApplication.translate("w_instance", u"Aesthetic Gradients", None))
#endif // QT_CONFIG(statustip)
        self.toolButton.setText(QCoreApplication.translate("w_instance", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_5.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_5.setText(QCoreApplication.translate("w_instance", u"{destination}\\hypernetworks", None))
        self.checkBox_16.setText(QCoreApplication.translate("w_instance", u"Other Paths?", None))
        self.toolButton_5.setText(QCoreApplication.translate("w_instance", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_12.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_12.setText(QCoreApplication.translate("w_instance", u"{destination}\\upscale_models", None))
        self.checkBox_13.setText(QCoreApplication.translate("w_instance", u"VAEs", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_14.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_14.setText(QCoreApplication.translate("w_instance", u"{destination}\\Wildcards", None))
        self.checkBox_4.setText(QCoreApplication.translate("w_instance", u"DoRas", None))
        self.toolButton_11.setText(QCoreApplication.translate("w_instance", u"...", None))
        self.checkBox_14.setText(QCoreApplication.translate("w_instance", u"Wildcards", None))
        self.checkBox_12.setText(QCoreApplication.translate("w_instance", u"Upscalers", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_13.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_13.setText(QCoreApplication.translate("w_instance", u"{destination}\\VAE", None))
        self.checkBox_3.setText(QCoreApplication.translate("w_instance", u"Controlnets", None))
        self.toolButton_6.setText(QCoreApplication.translate("w_instance", u"...", None))
        self.toolButton_14.setText(QCoreApplication.translate("w_instance", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_4.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_4.setText(QCoreApplication.translate("w_instance", u"{destination}\\loras", None))
        self.toolButton_8.setText(QCoreApplication.translate("w_instance", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_3.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_3.setText(QCoreApplication.translate("w_instance", u"{destination}\\ControlNet", None))
        self.toolButton_13.setText(QCoreApplication.translate("w_instance", u"...", None))
        self.checkBox_10.setText(QCoreApplication.translate("w_instance", u"Poses", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_15.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_15.setText(QCoreApplication.translate("w_instance", u"{destination}\\Workflows", None))
        self.checkBox_8.setText(QCoreApplication.translate("w_instance", u"Motions", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setText(QCoreApplication.translate("w_instance", u"{destination}\\Aesthetic gradients", None))
        self.toolButton_12.setText(QCoreApplication.translate("w_instance", u"...", None))
        self.checkBox_7.setText(QCoreApplication.translate("w_instance", u"LyCORISs", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setText(QCoreApplication.translate("w_instance", u"{destination}\\checkpoints", None))
        self.checkBox_6.setText(QCoreApplication.translate("w_instance", u"LoRas", None))
        self.checkBox_11.setText(QCoreApplication.translate("w_instance", u"Embeddings", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_11.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_11.setText(QCoreApplication.translate("w_instance", u"{destination}\\embeddings", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_10.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_10.setText(QCoreApplication.translate("w_instance", u"{destination}\\poses", None))
        self.toolButton_3.setText(QCoreApplication.translate("w_instance", u"...", None))
        self.toolButton_7.setText(QCoreApplication.translate("w_instance", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_7.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_7.setText(QCoreApplication.translate("w_instance", u"{destination}\\loras", None))
        self.checkBox_15.setText(QCoreApplication.translate("w_instance", u"Workflows", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_6.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_6.setText(QCoreApplication.translate("w_instance", u"{destination}\\loras", None))
        self.toolButton_4.setText(QCoreApplication.translate("w_instance", u"...", None))
        self.tb_add.setText(QCoreApplication.translate("w_instance", u"Add", None))
        self.tb_edit.setText(QCoreApplication.translate("w_instance", u"Edit", None))
        self.tb_delete.setText(QCoreApplication.translate("w_instance", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_8.setToolTip(QCoreApplication.translate("w_instance", u"<html><head/><body><p>Activate this path with checkbox to the left, change path with button to the right.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_8.setText(QCoreApplication.translate("w_instance", u"{destination}\\MotionModule", None))
        self.checkBox_5.setText(QCoreApplication.translate("w_instance", u"Hypernetworks", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("w_instance", u"Default Settings", None))
        self.rb_custom.setText(QCoreApplication.translate("w_instance", u"Custom", None))
        self.rb_a1111.setText(QCoreApplication.translate("w_instance", u"A1111", None))
        self.rb_comfyui.setText(QCoreApplication.translate("w_instance", u"ComfyUI", None))
    # retranslateUi

