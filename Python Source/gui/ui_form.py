# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

from pyqtgraph import PlotWidget

class Ui_OpenControl(object):
    def setupUi(self, OpenControl):
        if not OpenControl.objectName():
            OpenControl.setObjectName(u"OpenControl")
        OpenControl.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"//media/Eli/Projects/OpenControl/Python Source/gui/OpenComputers.ico", QSize(), QIcon.Normal, QIcon.Off)
        OpenControl.setWindowIcon(icon)
        self.actionConnect_All = QAction(OpenControl)
        self.actionConnect_All.setObjectName(u"actionConnect_All")
        self.actionConnect_to_Game = QAction(OpenControl)
        self.actionConnect_to_Game.setObjectName(u"actionConnect_to_Game")
        self.actionConnect_To_Database = QAction(OpenControl)
        self.actionConnect_To_Database.setObjectName(u"actionConnect_To_Database")
        self.actionConnect_to_Relay_Server = QAction(OpenControl)
        self.actionConnect_to_Relay_Server.setObjectName(u"actionConnect_to_Relay_Server")
        self.actionIP = QAction(OpenControl)
        self.actionIP.setObjectName(u"actionIP")
        self.actionLogin_Credentials = QAction(OpenControl)
        self.actionLogin_Credentials.setObjectName(u"actionLogin_Credentials")
        self.actionAuto_Connect = QAction(OpenControl)
        self.actionAuto_Connect.setObjectName(u"actionAuto_Connect")
        self.actionAuto_Connect.setCheckable(True)
        self.actionName = QAction(OpenControl)
        self.actionName.setObjectName(u"actionName")
        self.centralwidget = QWidget(OpenControl)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.inputPower = QGroupBox(self.centralwidget)
        self.inputPower.setObjectName(u"inputPower")
        font = QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.inputPower.setFont(font)
        self.gridLayout_7 = QGridLayout(self.inputPower)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.inputGraph = PlotWidget(self.inputPower)
        self.inputGraph.setObjectName(u"inputGraph")

        self.gridLayout_7.addWidget(self.inputGraph, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.inputPower, 1, 0, 1, 1)

        self.totalPower = QGroupBox(self.centralwidget)
        self.totalPower.setObjectName(u"totalPower")
        font1 = QFont()
        font1.setPointSize(12)
        self.totalPower.setFont(font1)
        self.gridLayout_9 = QGridLayout(self.totalPower)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.totalGraph = PlotWidget(self.totalPower)
        self.totalGraph.setObjectName(u"totalGraph")

        self.gridLayout_9.addWidget(self.totalGraph, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.totalPower, 2, 0, 1, 1)

        self.applied_energistics = QGroupBox(self.centralwidget)
        self.applied_energistics.setObjectName(u"applied_energistics")
        self.applied_energistics.setFont(font)
        self.gridLayout_6 = QGridLayout(self.applied_energistics)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.storage = QPushButton(self.applied_energistics)
        self.storage.setObjectName(u"storage")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setKerning(True)
        self.storage.setFont(font2)

        self.gridLayout_6.addWidget(self.storage, 0, 0, 1, 1, Qt.AlignVCenter)

        self.craftingRequest = QPushButton(self.applied_energistics)
        self.craftingRequest.setObjectName(u"craftingRequest")
        self.craftingRequest.setFont(font2)

        self.gridLayout_6.addWidget(self.craftingRequest, 0, 1, 1, 1, Qt.AlignVCenter)


        self.gridLayout_8.addWidget(self.applied_energistics, 3, 0, 1, 1)

        OpenControl.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(OpenControl)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuConnect = QMenu(self.menubar)
        self.menuConnect.setObjectName(u"menuConnect")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuConnection_Settings = QMenu(self.menuSettings)
        self.menuConnection_Settings.setObjectName(u"menuConnection_Settings")
        self.menuDatabase = QMenu(self.menuConnection_Settings)
        self.menuDatabase.setObjectName(u"menuDatabase")
        OpenControl.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(OpenControl)
        self.statusbar.setObjectName(u"statusbar")
        OpenControl.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuConnect.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuConnect.addAction(self.actionConnect_All)
        self.menuConnect.addSeparator()
        self.menuConnect.addAction(self.actionConnect_to_Game)
        self.menuConnect.addAction(self.actionConnect_To_Database)
        self.menuConnect.addAction(self.actionConnect_to_Relay_Server)
        self.menuSettings.addAction(self.menuConnection_Settings.menuAction())
        self.menuConnection_Settings.addAction(self.actionIP)
        self.menuConnection_Settings.addAction(self.actionLogin_Credentials)
        self.menuConnection_Settings.addAction(self.menuDatabase.menuAction())
        self.menuConnection_Settings.addAction(self.actionAuto_Connect)
        self.menuDatabase.addAction(self.actionName)

        self.retranslateUi(OpenControl)

        QMetaObject.connectSlotsByName(OpenControl)
    # setupUi

    def retranslateUi(self, OpenControl):
        OpenControl.setWindowTitle(QCoreApplication.translate("OpenControl", u"OpenControl", None))
        self.actionConnect_All.setText(QCoreApplication.translate("OpenControl", u"Connect All", None))
        self.actionConnect_to_Game.setText(QCoreApplication.translate("OpenControl", u"Connect to Game", None))
        self.actionConnect_To_Database.setText(QCoreApplication.translate("OpenControl", u"Connect To Database", None))
        self.actionConnect_to_Relay_Server.setText(QCoreApplication.translate("OpenControl", u"Connect to Relay Server", None))
        self.actionIP.setText(QCoreApplication.translate("OpenControl", u"IP/Port", None))
        self.actionLogin_Credentials.setText(QCoreApplication.translate("OpenControl", u"Login Credentials", None))
        self.actionAuto_Connect.setText(QCoreApplication.translate("OpenControl", u"Auto Connect", None))
        self.actionName.setText(QCoreApplication.translate("OpenControl", u"Name", None))
        self.inputPower.setTitle(QCoreApplication.translate("OpenControl", u"Input Power", None))
        self.totalPower.setTitle(QCoreApplication.translate("OpenControl", u"Total Power", None))
        self.applied_energistics.setTitle(QCoreApplication.translate("OpenControl", u"Applied Energistics 2", None))
        self.storage.setText(QCoreApplication.translate("OpenControl", u"Storage", None))
        self.craftingRequest.setText(QCoreApplication.translate("OpenControl", u"Crafting Request", None))
        self.menuConnect.setTitle(QCoreApplication.translate("OpenControl", u"Connect", None))
        self.menuSettings.setTitle(QCoreApplication.translate("OpenControl", u"Settings", None))
        self.menuConnection_Settings.setTitle(QCoreApplication.translate("OpenControl", u"Connection Settings", None))
        self.menuDatabase.setTitle(QCoreApplication.translate("OpenControl", u"Database", None))
    # retranslateUi

