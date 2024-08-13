# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'storage.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Storage(object):
    def setupUi(self, Storage):
        if not Storage.objectName():
            Storage.setObjectName(u"Storage")
        Storage.resize(631, 687)
        icon = QIcon()
        icon.addFile(u"//media/Eli/Projects/OpenControl/Python Source/gui/OpenComputers.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Storage.setWindowIcon(icon)
        self.gridLayout_3 = QGridLayout(Storage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.queueGroup = QGroupBox(Storage)
        self.queueGroup.setObjectName(u"queueGroup")
        font = QFont()
        font.setPointSize(12)
        self.queueGroup.setFont(font)
        self.gridLayout_5 = QGridLayout(self.queueGroup)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.queueTable = QTableWidget(self.queueGroup)
        if (self.queueTable.columnCount() < 5):
            self.queueTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.queueTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.queueTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.queueTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.queueTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.queueTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.queueTable.setObjectName(u"queueTable")

        self.gridLayout_5.addWidget(self.queueTable, 0, 0, 1, 1)

        self.showPastRequests = QCheckBox(self.queueGroup)
        self.showPastRequests.setObjectName(u"showPastRequests")

        self.gridLayout_5.addWidget(self.showPastRequests, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.queueGroup, 2, 0, 1, 1)

        self.storageGroup = QGroupBox(Storage)
        self.storageGroup.setObjectName(u"storageGroup")
        self.storageGroup.setFont(font)
        self.gridLayout_4 = QGridLayout(self.storageGroup)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.storageTable = QTableWidget(self.storageGroup)
        if (self.storageTable.columnCount() < 3):
            self.storageTable.setColumnCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.storageTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.storageTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setText(u"Data");
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.storageTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        self.storageTable.setObjectName(u"storageTable")
        self.storageTable.setSortingEnabled(True)
        self.storageTable.setColumnCount(3)

        self.gridLayout_4.addWidget(self.storageTable, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.storageGroup, 1, 0, 1, 1)


        self.retranslateUi(Storage)

        QMetaObject.connectSlotsByName(Storage)
    # setupUi

    def retranslateUi(self, Storage):
        Storage.setWindowTitle(QCoreApplication.translate("Storage", u"Storage - OpenControl", None))
        self.queueGroup.setTitle(QCoreApplication.translate("Storage", u"Queue", None))
        ___qtablewidgetitem = self.queueTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Storage", u"Item", None));
        ___qtablewidgetitem1 = self.queueTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Storage", u"Requested", None));
        ___qtablewidgetitem2 = self.queueTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Storage", u"Remaining", None));
        ___qtablewidgetitem3 = self.queueTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Storage", u"Processors", None));
        ___qtablewidgetitem4 = self.queueTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Storage", u"Date Time", None));
        self.showPastRequests.setText(QCoreApplication.translate("Storage", u"Show Past Crafting Requests", None))
        self.storageGroup.setTitle(QCoreApplication.translate("Storage", u"Storage", None))
        ___qtablewidgetitem5 = self.storageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Storage", u"Item", None));
        ___qtablewidgetitem6 = self.storageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Storage", u"Amount", None));
    # retranslateUi

