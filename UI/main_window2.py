# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window2.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QTabWidget,
    QTableView, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBar, QToolButton, QTreeView, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_w_main(object):
    def setupUi(self, w_main):
        if not w_main.objectName():
            w_main.setObjectName(u"w_main")
        w_main.resize(1543, 1447)
        self.actionImport_Models = QAction(w_main)
        self.actionImport_Models.setObjectName(u"actionImport_Models")
        self.actionSettings = QAction(w_main)
        self.actionSettings.setObjectName(u"actionSettings")
        icon = QIcon()
        icon.addFile(u":/tools/icons/application-form.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon)
        self.actionAdd_Instance = QAction(w_main)
        self.actionAdd_Instance.setObjectName(u"actionAdd_Instance")
        icon1 = QIcon()
        icon1.addFile(u":/tools/icons/plus-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd_Instance.setIcon(icon1)
        self.actionEdit_Instance = QAction(w_main)
        self.actionEdit_Instance.setObjectName(u"actionEdit_Instance")
        self.actionEdit_Instance.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/tools/icons/pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEdit_Instance.setIcon(icon2)
        self.w_central = QWidget(w_main)
        self.w_central.setObjectName(u"w_central")
        self.gridLayout = QGridLayout(self.w_central)
        self.gridLayout.setObjectName(u"gridLayout")
        self.f_search = QFrame(self.w_central)
        self.f_search.setObjectName(u"f_search")
        self.f_search.setMaximumSize(QSize(16777215, 25))
        self.f_search.setFrameShape(QFrame.StyledPanel)
        self.f_search.setFrameShadow(QFrame.Raised)
        self.hl_search = QHBoxLayout(self.f_search)
        self.hl_search.setObjectName(u"hl_search")
        self.hl_search.setContentsMargins(0, 0, 0, 0)
        self.le_search = QLineEdit(self.f_search)
        self.le_search.setObjectName(u"le_search")

        self.hl_search.addWidget(self.le_search)


        self.gridLayout.addWidget(self.f_search, 1, 0, 1, 1)

        self.te_log = QTextEdit(self.w_central)
        self.te_log.setObjectName(u"te_log")
        self.te_log.setMaximumSize(QSize(16777215, 100))

        self.gridLayout.addWidget(self.te_log, 4, 0, 1, 1)

        self.f_instance2 = QFrame(self.w_central)
        self.f_instance2.setObjectName(u"f_instance2")
        self.f_instance2.setMinimumSize(QSize(0, 20))
        self.f_instance2.setMaximumSize(QSize(16777215, 20))
        self.f_instance2.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.f_instance2.setFrameShape(QFrame.StyledPanel)
        self.f_instance2.setFrameShadow(QFrame.Raised)
        self.gl_instance2 = QGridLayout(self.f_instance2)
        self.gl_instance2.setSpacing(6)
        self.gl_instance2.setObjectName(u"gl_instance2")
        self.gl_instance2.setContentsMargins(0, 0, 0, 0)
        self.lb_instance2 = QLabel(self.f_instance2)
        self.lb_instance2.setObjectName(u"lb_instance2")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.lb_instance2.setFont(font)
        self.lb_instance2.setAlignment(Qt.AlignCenter)

        self.gl_instance2.addWidget(self.lb_instance2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.f_instance2, 0, 0, 1, 1)

        self.f_main = QFrame(self.w_central)
        self.f_main.setObjectName(u"f_main")
        self.f_main.setFrameShape(QFrame.NoFrame)
        self.f_main.setFrameShadow(QFrame.Raised)
        self.hl_main = QHBoxLayout(self.f_main)
        self.hl_main.setObjectName(u"hl_main")
        self.hl_main.setContentsMargins(0, 0, 0, 0)
        self.sp_verticle = QSplitter(self.f_main)
        self.sp_verticle.setObjectName(u"sp_verticle")
        self.sp_verticle.setOrientation(Qt.Horizontal)
        self.sa_left = QScrollArea(self.sp_verticle)
        self.sa_left.setObjectName(u"sa_left")
        self.sa_left.setMaximumSize(QSize(350, 16777215))
        self.sa_left.setFrameShape(QFrame.NoFrame)
        self.sa_left.setWidgetResizable(True)
        self.sac_left = QWidget()
        self.sac_left.setObjectName(u"sac_left")
        self.sac_left.setGeometry(QRect(0, 0, 350, 1122))
        self.horizontalLayout_2 = QHBoxLayout(self.sac_left)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.w_left = QWidget(self.sac_left)
        self.w_left.setObjectName(u"w_left")
        self.horizontalLayout = QHBoxLayout(self.w_left)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.t_tree = QTabWidget(self.w_left)
        self.t_tree.setObjectName(u"t_tree")
        self.t_models = QWidget()
        self.t_models.setObjectName(u"t_models")
        self.horizontalLayout_4 = QHBoxLayout(self.t_models)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tv_models_3 = QTreeView(self.t_models)
        self.tv_models_3.setObjectName(u"tv_models_3")
        self.tv_models_3.header().setVisible(False)

        self.horizontalLayout_4.addWidget(self.tv_models_3)

        self.t_tree.addTab(self.t_models, "")

        self.horizontalLayout.addWidget(self.t_tree)

        self.f_left = QFrame(self.w_left)
        self.f_left.setObjectName(u"f_left")
        self.f_left.setFrameShape(QFrame.StyledPanel)
        self.f_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_left)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gb_base = QGroupBox(self.f_left)
        self.gb_base.setObjectName(u"gb_base")
        self.gb_base.setFlat(True)
        self.vl_base = QVBoxLayout(self.gb_base)
        self.vl_base.setObjectName(u"vl_base")
        self.vl_base.setContentsMargins(0, 0, 0, 0)
        self.lv_base_model = QListView(self.gb_base)
        self.lv_base_model.setObjectName(u"lv_base_model")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lv_base_model.sizePolicy().hasHeightForWidth())
        self.lv_base_model.setSizePolicy(sizePolicy)
        self.lv_base_model.setSelectionMode(QAbstractItemView.MultiSelection)

        self.vl_base.addWidget(self.lv_base_model)


        self.verticalLayout_2.addWidget(self.gb_base)

        self.gb_model = QGroupBox(self.f_left)
        self.gb_model.setObjectName(u"gb_model")
        self.gb_model.setFlat(True)
        self.vl_model = QVBoxLayout(self.gb_model)
        self.vl_model.setObjectName(u"vl_model")
        self.vl_model.setContentsMargins(0, 0, 0, 0)
        self.lv_model_type = QListView(self.gb_model)
        self.lv_model_type.setObjectName(u"lv_model_type")
        self.lv_model_type.setAlternatingRowColors(False)
        self.lv_model_type.setSelectionMode(QAbstractItemView.MultiSelection)
        self.lv_model_type.setSelectionRectVisible(True)

        self.vl_model.addWidget(self.lv_model_type)


        self.verticalLayout_2.addWidget(self.gb_model)

        self.gb_creator = QGroupBox(self.f_left)
        self.gb_creator.setObjectName(u"gb_creator")
        self.gb_creator.setFlat(True)
        self.vl_creator = QVBoxLayout(self.gb_creator)
        self.vl_creator.setObjectName(u"vl_creator")
        self.vl_creator.setContentsMargins(0, 0, 0, 0)
        self.lv_creator = QListView(self.gb_creator)
        self.lv_creator.setObjectName(u"lv_creator")

        self.vl_creator.addWidget(self.lv_creator)


        self.verticalLayout_2.addWidget(self.gb_creator)

        self.gb_tags = QGroupBox(self.f_left)
        self.gb_tags.setObjectName(u"gb_tags")
        self.gb_tags.setFlat(True)
        self.vl_tags = QVBoxLayout(self.gb_tags)
        self.vl_tags.setObjectName(u"vl_tags")
        self.vl_tags.setContentsMargins(0, 0, 0, 0)
        self.lv_tags = QListView(self.gb_tags)
        self.lv_tags.setObjectName(u"lv_tags")

        self.vl_tags.addWidget(self.lv_tags)


        self.verticalLayout_2.addWidget(self.gb_tags)


        self.horizontalLayout.addWidget(self.f_left)


        self.horizontalLayout_2.addWidget(self.w_left)

        self.sa_left.setWidget(self.sac_left)
        self.sp_verticle.addWidget(self.sa_left)
        self.f_right = QFrame(self.sp_verticle)
        self.f_right.setObjectName(u"f_right")
        self.f_right.setFrameShape(QFrame.NoFrame)
        self.f_right.setFrameShadow(QFrame.Raised)
        self.vl_f_right = QVBoxLayout(self.f_right)
        self.vl_f_right.setObjectName(u"vl_f_right")
        self.vl_f_right.setContentsMargins(0, 0, 0, 0)
        self.sp_horizontal = QSplitter(self.f_right)
        self.sp_horizontal.setObjectName(u"sp_horizontal")
        self.sp_horizontal.setOrientation(Qt.Vertical)
        self.t_list = QTabWidget(self.sp_horizontal)
        self.t_list.setObjectName(u"t_list")
        self.t_listview = QWidget()
        self.t_listview.setObjectName(u"t_listview")
        self.vl_listview = QVBoxLayout(self.t_listview)
        self.vl_listview.setObjectName(u"vl_listview")
        self.vl_listview.setContentsMargins(0, 0, 0, 0)
        self.tv_models_2 = QTableView(self.t_listview)
        self.tv_models_2.setObjectName(u"tv_models_2")
        self.tv_models_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tv_models_2.setAlternatingRowColors(True)
        self.tv_models_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tv_models_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_models_2.setShowGrid(False)
        self.tv_models_2.setSortingEnabled(True)
        self.tv_models_2.setCornerButtonEnabled(False)
        self.tv_models_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tv_models_2.horizontalHeader().setDefaultSectionSize(200)
        self.tv_models_2.horizontalHeader().setStretchLastSection(True)
        self.tv_models_2.verticalHeader().setVisible(False)

        self.vl_listview.addWidget(self.tv_models_2)

        self.t_list.addTab(self.t_listview, "")
        self.t_images = QWidget()
        self.t_images.setObjectName(u"t_images")
        self.vl_images = QVBoxLayout(self.t_images)
        self.vl_images.setObjectName(u"vl_images")
        self.vl_images.setContentsMargins(0, 0, 0, 0)
        self.sa_images = QScrollArea(self.t_images)
        self.sa_images.setObjectName(u"sa_images")
        self.sa_images.setFrameShape(QFrame.NoFrame)
        self.sa_images.setWidgetResizable(True)
        self.sac_images = QWidget()
        self.sac_images.setObjectName(u"sac_images")
        self.sac_images.setGeometry(QRect(0, 0, 1164, 551))
        self.hl_images = QHBoxLayout(self.sac_images)
        self.hl_images.setObjectName(u"hl_images")
        self.hl_images.setContentsMargins(0, 0, 0, 0)
        self.f_images = QFrame(self.sac_images)
        self.f_images.setObjectName(u"f_images")
        self.f_images.setFrameShape(QFrame.NoFrame)
        self.f_images.setFrameShadow(QFrame.Raised)
        self.gl_images = QGridLayout(self.f_images)
        self.gl_images.setObjectName(u"gl_images")
        self.gl_images.setVerticalSpacing(6)
        self.gl_images.setContentsMargins(0, 0, 0, 6)

        self.hl_images.addWidget(self.f_images)

        self.sa_images.setWidget(self.sac_images)

        self.vl_images.addWidget(self.sa_images)

        self.t_list.addTab(self.t_images, "")
        self.sp_horizontal.addWidget(self.t_list)
        self.sa_viewer = QScrollArea(self.sp_horizontal)
        self.sa_viewer.setObjectName(u"sa_viewer")
        self.sa_viewer.setFrameShape(QFrame.NoFrame)
        self.sa_viewer.setWidgetResizable(True)
        self.sac_viewer = QWidget()
        self.sac_viewer.setObjectName(u"sac_viewer")
        self.sac_viewer.setGeometry(QRect(0, 0, 1170, 537))
        self.vl_viewer = QVBoxLayout(self.sac_viewer)
        self.vl_viewer.setObjectName(u"vl_viewer")
        self.vl_viewer.setContentsMargins(0, 0, 0, 0)
        self.t_viewer = QTabWidget(self.sac_viewer)
        self.t_viewer.setObjectName(u"t_viewer")
        self.t_local = QWidget()
        self.t_local.setObjectName(u"t_local")
        self.vl_t_local = QVBoxLayout(self.t_local)
        self.vl_t_local.setObjectName(u"vl_t_local")
        self.vl_t_local.setContentsMargins(0, 0, 0, 0)
        self.w_local = QWidget(self.t_local)
        self.w_local.setObjectName(u"w_local")
        self.gl_local = QGridLayout(self.w_local)
        self.gl_local.setObjectName(u"gl_local")
        self.gl_local.setContentsMargins(0, 0, 0, 0)
        self.s_local = QScrollArea(self.w_local)
        self.s_local.setObjectName(u"s_local")
        self.s_local.setWidgetResizable(True)
        self.sa_local = QWidget()
        self.sa_local.setObjectName(u"sa_local")
        self.sa_local.setGeometry(QRect(0, 0, 1145, 870))
        self.gl_local_2 = QGridLayout(self.sa_local)
        self.gl_local_2.setObjectName(u"gl_local_2")
        self.gl_local_2.setContentsMargins(0, 0, 0, 0)
        self.lb_image = QLabel(self.sa_local)
        self.lb_image.setObjectName(u"lb_image")
        self.lb_image.setMinimumSize(QSize(600, 600))
        self.lb_image.setMaximumSize(QSize(1024, 1024))
        self.lb_image.setSizeIncrement(QSize(0, 0))

        self.gl_local_2.addWidget(self.lb_image, 1, 1, 2, 1)

        self.lb_title = QLabel(self.sa_local)
        self.lb_title.setObjectName(u"lb_title")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.lb_title.setFont(font1)
        self.lb_title.setAlignment(Qt.AlignCenter)

        self.gl_local_2.addWidget(self.lb_title, 0, 0, 1, 2)

        self.t_description = QTabWidget(self.sa_local)
        self.t_description.setObjectName(u"t_description")
        self.t_version = QWidget()
        self.t_version.setObjectName(u"t_version")
        self.gl_version = QGridLayout(self.t_version)
        self.gl_version.setObjectName(u"gl_version")
        self.gl_version.setContentsMargins(0, 0, 0, 0)
        self.te_version = QTextEdit(self.t_version)
        self.te_version.setObjectName(u"te_version")

        self.gl_version.addWidget(self.te_version, 0, 0, 1, 1)

        self.t_description.addTab(self.t_version, "")
        self.t_model = QWidget()
        self.t_model.setObjectName(u"t_model")
        self.gl_model = QGridLayout(self.t_model)
        self.gl_model.setObjectName(u"gl_model")
        self.gl_model.setContentsMargins(0, 0, 0, 0)
        self.te_model = QTextEdit(self.t_model)
        self.te_model.setObjectName(u"te_model")

        self.gl_model.addWidget(self.te_model, 0, 0, 1, 1)

        self.t_description.addTab(self.t_model, "")

        self.gl_local_2.addWidget(self.t_description, 2, 0, 1, 1)

        self.w_images = QWidget(self.sa_local)
        self.w_images.setObjectName(u"w_images")
        self.verticalLayout = QVBoxLayout(self.w_images)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_images = QLabel(self.w_images)
        self.lb_images.setObjectName(u"lb_images")
        self.lb_images.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_images)

        self.we_images = QWebEngineView(self.w_images)
        self.we_images.setObjectName(u"we_images")
        self.we_images.setMinimumSize(QSize(0, 200))
        self.we_images.setBaseSize(QSize(0, 200))
        self.we_images.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.we_images)


        self.gl_local_2.addWidget(self.w_images, 3, 0, 1, 2)

        self.tv_properties = QTableWidget(self.sa_local)
        self.tv_properties.setObjectName(u"tv_properties")
        self.tv_properties.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tv_properties.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tv_properties.setCornerButtonEnabled(False)
        self.tv_properties.horizontalHeader().setVisible(False)
        self.tv_properties.horizontalHeader().setStretchLastSection(True)

        self.gl_local_2.addWidget(self.tv_properties, 1, 0, 1, 1)

        self.s_local.setWidget(self.sa_local)

        self.gl_local.addWidget(self.s_local, 0, 0, 1, 1)


        self.vl_t_local.addWidget(self.w_local)

        self.t_viewer.addTab(self.t_local, "")
        self.t_web = QWidget()
        self.t_web.setObjectName(u"t_web")
        self.vl_t_web = QVBoxLayout(self.t_web)
        self.vl_t_web.setObjectName(u"vl_t_web")
        self.vl_t_web.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.t_web)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tb_back = QToolButton(self.widget)
        self.tb_back.setObjectName(u"tb_back")

        self.horizontalLayout_3.addWidget(self.tb_back)

        self.le_navbar = QLineEdit(self.widget)
        self.le_navbar.setObjectName(u"le_navbar")

        self.horizontalLayout_3.addWidget(self.le_navbar)

        self.tb_go = QToolButton(self.widget)
        self.tb_go.setObjectName(u"tb_go")

        self.horizontalLayout_3.addWidget(self.tb_go)

        self.tb_forward = QToolButton(self.widget)
        self.tb_forward.setObjectName(u"tb_forward")

        self.horizontalLayout_3.addWidget(self.tb_forward)


        self.vl_t_web.addWidget(self.widget)

        self.we_web = QWebEngineView(self.t_web)
        self.we_web.setObjectName(u"we_web")
        self.we_web.setUrl(QUrl(u"about:blank"))

        self.vl_t_web.addWidget(self.we_web)

        self.t_viewer.addTab(self.t_web, "")

        self.vl_viewer.addWidget(self.t_viewer)

        self.sa_viewer.setWidget(self.sac_viewer)
        self.sp_horizontal.addWidget(self.sa_viewer)

        self.vl_f_right.addWidget(self.sp_horizontal)

        self.sp_verticle.addWidget(self.f_right)

        self.hl_main.addWidget(self.sp_verticle)


        self.gridLayout.addWidget(self.f_main, 2, 0, 1, 1)

        self.f_log_button = QFrame(self.w_central)
        self.f_log_button.setObjectName(u"f_log_button")
        self.f_log_button.setMaximumSize(QSize(16777215, 35))
        self.f_log_button.setFrameShape(QFrame.StyledPanel)
        self.f_log_button.setFrameShadow(QFrame.Raised)
        self.hl_log_button = QHBoxLayout(self.f_log_button)
        self.hl_log_button.setObjectName(u"hl_log_button")
        self.hl_log_button.setContentsMargins(0, 0, 0, 0)
        self.pb_log = QPushButton(self.f_log_button)
        self.pb_log.setObjectName(u"pb_log")

        self.hl_log_button.addWidget(self.pb_log)

        self.hs_log_button = QSpacerItem(313, 21, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_log_button.addItem(self.hs_log_button)


        self.gridLayout.addWidget(self.f_log_button, 3, 0, 1, 1)

        self.f_instance1 = QFrame(self.w_central)
        self.f_instance1.setObjectName(u"f_instance1")
        self.f_instance1.setMinimumSize(QSize(0, 20))
        self.f_instance1.setMaximumSize(QSize(16777215, 20))
        self.f_instance1.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.f_instance1.setFrameShape(QFrame.StyledPanel)
        self.f_instance1.setFrameShadow(QFrame.Raised)
        self.gl_instance1 = QGridLayout(self.f_instance1)
        self.gl_instance1.setSpacing(6)
        self.gl_instance1.setObjectName(u"gl_instance1")
        self.gl_instance1.setContentsMargins(0, 0, 0, 0)
        self.lb_instance1 = QLabel(self.f_instance1)
        self.lb_instance1.setObjectName(u"lb_instance1")
        self.lb_instance1.setFont(font)
        self.lb_instance1.setAlignment(Qt.AlignCenter)

        self.gl_instance1.addWidget(self.lb_instance1, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.f_instance1, 5, 0, 1, 1)

        w_main.setCentralWidget(self.w_central)
        self.m_bar = QMenuBar(w_main)
        self.m_bar.setObjectName(u"m_bar")
        self.m_bar.setGeometry(QRect(0, 0, 1543, 22))
        self.menuFile = QMenu(self.m_bar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInstances = QMenu(self.m_bar)
        self.menuInstances.setObjectName(u"menuInstances")
        w_main.setMenuBar(self.m_bar)
        self.s_bar = QStatusBar(w_main)
        self.s_bar.setObjectName(u"s_bar")
        w_main.setStatusBar(self.s_bar)
        self.tbar_manager = QToolBar(w_main)
        self.tbar_manager.setObjectName(u"tbar_manager")
        w_main.addToolBar(Qt.TopToolBarArea, self.tbar_manager)
        self.tbar_downloader = QToolBar(w_main)
        self.tbar_downloader.setObjectName(u"tbar_downloader")
        w_main.addToolBar(Qt.TopToolBarArea, self.tbar_downloader)

        self.m_bar.addAction(self.menuFile.menuAction())
        self.m_bar.addAction(self.menuInstances.menuAction())
        self.menuFile.addAction(self.actionImport_Models)
        self.menuFile.addAction(self.actionSettings)
        self.menuInstances.addAction(self.actionAdd_Instance)
        self.menuInstances.addAction(self.actionEdit_Instance)
        self.tbar_manager.addAction(self.actionAdd_Instance)
        self.tbar_manager.addAction(self.actionEdit_Instance)

        self.retranslateUi(w_main)

        self.t_tree.setCurrentIndex(0)
        self.t_list.setCurrentIndex(1)
        self.t_viewer.setCurrentIndex(1)
        self.t_description.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(w_main)
    # setupUi

    def retranslateUi(self, w_main):
        w_main.setWindowTitle(QCoreApplication.translate("w_main", u"MainWindow", None))
        self.actionImport_Models.setText(QCoreApplication.translate("w_main", u"Import Models", None))
        self.actionSettings.setText(QCoreApplication.translate("w_main", u"Settings", None))
        self.actionAdd_Instance.setText(QCoreApplication.translate("w_main", u"Add Instance", None))
        self.actionEdit_Instance.setText(QCoreApplication.translate("w_main", u"Edit Instance", None))
        self.lb_instance2.setText(QCoreApplication.translate("w_main", u"TextLabel", None))
        self.t_tree.setTabText(self.t_tree.indexOf(self.t_models), QCoreApplication.translate("w_main", u"Models", None))
        self.gb_base.setTitle(QCoreApplication.translate("w_main", u"Base Model", None))
        self.gb_model.setTitle(QCoreApplication.translate("w_main", u"Model Type", None))
        self.gb_creator.setTitle(QCoreApplication.translate("w_main", u"Creator", None))
        self.gb_tags.setTitle(QCoreApplication.translate("w_main", u"Tags", None))
        self.t_list.setTabText(self.t_list.indexOf(self.t_listview), QCoreApplication.translate("w_main", u"List", None))
        self.t_list.setTabText(self.t_list.indexOf(self.t_images), QCoreApplication.translate("w_main", u"Images", None))
        self.lb_image.setText(QCoreApplication.translate("w_main", u"TextLabel", None))
        self.lb_title.setText(QCoreApplication.translate("w_main", u"Model - Version Title", None))
        self.t_description.setTabText(self.t_description.indexOf(self.t_version), QCoreApplication.translate("w_main", u"Version Info", None))
        self.t_description.setTabText(self.t_description.indexOf(self.t_model), QCoreApplication.translate("w_main", u"Model Info", None))
        self.lb_images.setText(QCoreApplication.translate("w_main", u"Additional Images", None))
        self.t_viewer.setTabText(self.t_viewer.indexOf(self.t_local), QCoreApplication.translate("w_main", u"Local View", None))
        self.tb_back.setText(QCoreApplication.translate("w_main", u"<", None))
        self.tb_go.setText(QCoreApplication.translate("w_main", u"Go", None))
        self.tb_forward.setText(QCoreApplication.translate("w_main", u">", None))
        self.t_viewer.setTabText(self.t_viewer.indexOf(self.t_web), QCoreApplication.translate("w_main", u"Web View", None))
        self.pb_log.setText(QCoreApplication.translate("w_main", u"Hide Log", None))
        self.lb_instance1.setText(QCoreApplication.translate("w_main", u"TextLabel", None))
        self.menuFile.setTitle(QCoreApplication.translate("w_main", u"File", None))
        self.menuInstances.setTitle(QCoreApplication.translate("w_main", u"Instances", None))
        self.tbar_manager.setWindowTitle(QCoreApplication.translate("w_main", u"toolBar", None))
        self.tbar_downloader.setWindowTitle(QCoreApplication.translate("w_main", u"toolBar", None))
    # retranslateUi

