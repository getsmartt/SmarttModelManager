# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QStatusBar,
    QTableView, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_w_main(object):
    def setupUi(self, w_main):
        if not w_main.objectName():
            w_main.setObjectName(u"w_main")
        w_main.resize(800, 1434)
        self.actionImport_Models = QAction(w_main)
        self.actionImport_Models.setObjectName(u"actionImport_Models")
        self.actionSettings = QAction(w_main)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionNew_Instance = QAction(w_main)
        self.actionNew_Instance.setObjectName(u"actionNew_Instance")
        self.actionNew_Instance.setEnabled(True)
        icon = QIcon()
        icon.addFile(u":/tools/icons/plus-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_Instance.setIcon(icon)
        self.actionEdit_Instance = QAction(w_main)
        self.actionEdit_Instance.setObjectName(u"actionEdit_Instance")
        self.actionEdit_Instance.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u":/tools/icons/pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEdit_Instance.setIcon(icon1)
        self.centralwidget = QWidget(w_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 20))
        self.frame_5.setMaximumSize(QSize(16777215, 20))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.fsearch = QFrame(self.centralwidget)
        self.fsearch.setObjectName(u"fsearch")
        self.fsearch.setMaximumSize(QSize(16777215, 25))
        self.fsearch.setFrameShape(QFrame.StyledPanel)
        self.fsearch.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fsearch)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.le_search = QLineEdit(self.fsearch)
        self.le_search.setObjectName(u"le_search")

        self.horizontalLayout.addWidget(self.le_search)


        self.verticalLayout_5.addWidget(self.fsearch)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.frame_2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setBaseSize(QSize(0, 0))
        self.splitter_2.setLineWidth(1)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setOpaqueResize(False)
        self.sasort = QScrollArea(self.splitter_2)
        self.sasort.setObjectName(u"sasort")
        self.sasort.setMaximumSize(QSize(16777215, 16777215))
        self.sasort.setBaseSize(QSize(200, 0))
        self.sasort.setFrameShape(QFrame.NoFrame)
        self.sasort.setFrameShadow(QFrame.Plain)
        self.sasort.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sasort.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.sasort.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 386, 1148))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gbbase = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gbbase.setObjectName(u"gbbase")
        self.gbbase.setFlat(True)
        self.verticalLayout_8 = QVBoxLayout(self.gbbase)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lv_base_model = QListView(self.gbbase)
        self.lv_base_model.setObjectName(u"lv_base_model")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lv_base_model.sizePolicy().hasHeightForWidth())
        self.lv_base_model.setSizePolicy(sizePolicy)
        self.lv_base_model.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_8.addWidget(self.lv_base_model)


        self.verticalLayout_9.addWidget(self.gbbase)

        self.gbmodel = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gbmodel.setObjectName(u"gbmodel")
        self.gbmodel.setFlat(True)
        self.verticalLayout_7 = QVBoxLayout(self.gbmodel)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lv_model_type = QListView(self.gbmodel)
        self.lv_model_type.setObjectName(u"lv_model_type")
        self.lv_model_type.setAlternatingRowColors(True)
        self.lv_model_type.setSelectionMode(QAbstractItemView.MultiSelection)
        self.lv_model_type.setSelectionRectVisible(True)

        self.verticalLayout_7.addWidget(self.lv_model_type)


        self.verticalLayout_9.addWidget(self.gbmodel)

        self.gbcreator = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gbcreator.setObjectName(u"gbcreator")
        self.gbcreator.setFlat(True)
        self.verticalLayout_4 = QVBoxLayout(self.gbcreator)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lv_creator = QListView(self.gbcreator)
        self.lv_creator.setObjectName(u"lv_creator")

        self.verticalLayout_4.addWidget(self.lv_creator)


        self.verticalLayout_9.addWidget(self.gbcreator)

        self.gbtags = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gbtags.setObjectName(u"gbtags")
        self.gbtags.setFlat(True)
        self.verticalLayout_2 = QVBoxLayout(self.gbtags)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lv_tags = QListView(self.gbtags)
        self.lv_tags.setObjectName(u"lv_tags")

        self.verticalLayout_2.addWidget(self.lv_tags)


        self.verticalLayout_9.addWidget(self.gbtags)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pb_log = QPushButton(self.frame_3)
        self.pb_log.setObjectName(u"pb_log")

        self.horizontalLayout_3.addWidget(self.pb_log)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addWidget(self.frame_3)

        self.sasort.setWidget(self.scrollAreaWidgetContents_2)
        self.splitter_2.addWidget(self.sasort)
        self.frame_6 = QFrame(self.splitter_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(-3)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.frame_6)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setAutoFillBackground(False)
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setLineWidth(1)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.frame_7 = QFrame(self.splitter)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tv_models = QTableView(self.frame_7)
        self.tv_models.setObjectName(u"tv_models")
        self.tv_models.setAlternatingRowColors(True)
        self.tv_models.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_models.setShowGrid(False)
        self.tv_models.setSortingEnabled(True)
        self.tv_models.setCornerButtonEnabled(False)
        self.tv_models.horizontalHeader().setDefaultSectionSize(200)
        self.tv_models.horizontalHeader().setStretchLastSection(True)
        self.tv_models.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tv_models)

        self.splitter.addWidget(self.frame_7)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 385, 69))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_2.addWidget(self.frame_6)

        self.horizontalLayout_2.addWidget(self.splitter_2)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.te_log = QTextEdit(self.centralwidget)
        self.te_log.setObjectName(u"te_log")
        self.te_log.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_5.addWidget(self.te_log)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 20))
        self.frame_4.setMaximumSize(QSize(16777215, 20))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_4)

        w_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(w_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInstances = QMenu(self.menubar)
        self.menuInstances.setObjectName(u"menuInstances")
        w_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(w_main)
        self.statusbar.setObjectName(u"statusbar")
        w_main.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(w_main)
        self.toolBar.setObjectName(u"toolBar")
        w_main.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInstances.menuAction())
        self.menuFile.addAction(self.actionImport_Models)
        self.menuFile.addAction(self.actionSettings)
        self.menuInstances.addAction(self.actionNew_Instance)
        self.toolBar.addAction(self.actionNew_Instance)
        self.toolBar.addAction(self.actionEdit_Instance)

        self.retranslateUi(w_main)

        QMetaObject.connectSlotsByName(w_main)
    # setupUi

    def retranslateUi(self, w_main):
        w_main.setWindowTitle(QCoreApplication.translate("w_main", u"MainWindow", None))
        self.actionImport_Models.setText(QCoreApplication.translate("w_main", u"Import Models", None))
        self.actionSettings.setText(QCoreApplication.translate("w_main", u"Settings", None))
        self.actionNew_Instance.setText(QCoreApplication.translate("w_main", u"New Instance", None))
        self.actionEdit_Instance.setText(QCoreApplication.translate("w_main", u"Edit Instance", None))
        self.label_3.setText(QCoreApplication.translate("w_main", u"TextLabel", None))
        self.gbbase.setTitle(QCoreApplication.translate("w_main", u"Base Model", None))
        self.gbmodel.setTitle(QCoreApplication.translate("w_main", u"Model Type", None))
        self.gbcreator.setTitle(QCoreApplication.translate("w_main", u"Creator", None))
        self.gbtags.setTitle(QCoreApplication.translate("w_main", u"Tags", None))
        self.pb_log.setText(QCoreApplication.translate("w_main", u"Hide Log", None))
        self.label.setText(QCoreApplication.translate("w_main", u"TextLabel", None))
        self.menuFile.setTitle(QCoreApplication.translate("w_main", u"File", None))
        self.menuInstances.setTitle(QCoreApplication.translate("w_main", u"Instances", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("w_main", u"toolBar", None))
    # retranslateUi

