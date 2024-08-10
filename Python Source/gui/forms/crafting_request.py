# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crafting_request.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QLabel,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Crafting(object):
    def setupUi(self, Crafting):
        if not Crafting.objectName():
            Crafting.setObjectName(u"Crafting")
        Crafting.resize(400, 104)
        icon = QIcon()
        icon.addFile(u"//media/Eli/Projects/OpenControl/Python Source/gui/OpenComputers.ico", QSize(), QIcon.Normal, QIcon.Off)
        Crafting.setWindowIcon(icon)
        self.formLayout = QFormLayout(Crafting)
        self.formLayout.setObjectName(u"formLayout")
        self.item = QComboBox(Crafting)
        self.item.setObjectName(u"item")
        self.item.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.item)

        self.item_label = QLabel(Crafting)
        self.item_label.setObjectName(u"item_label")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.item_label)

        self.amount = QSpinBox(Crafting)
        self.amount.setObjectName(u"amount")
        self.amount.setMinimumSize(QSize(200, 0))
        self.amount.setMaximum(10000)
        self.amount.setSingleStep(64)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.amount)

        self.amount_label = QLabel(Crafting)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.amount_label)

        self.push = QCheckBox(Crafting)
        self.push.setObjectName(u"push")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.push)

        self.ok_cancel = QDialogButtonBox(Crafting)
        self.ok_cancel.setObjectName(u"ok_cancel")
        self.ok_cancel.setOrientation(Qt.Horizontal)
        self.ok_cancel.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.ok_cancel.setCenterButtons(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ok_cancel)


        self.retranslateUi(Crafting)
        self.ok_cancel.accepted.connect(Crafting.accept)
        self.ok_cancel.rejected.connect(Crafting.reject)

        QMetaObject.connectSlotsByName(Crafting)
    # setupUi

    def retranslateUi(self, Crafting):
        Crafting.setWindowTitle(QCoreApplication.translate("Crafting", u"Crafting Request - OpenControl", None))
        self.item_label.setText(QCoreApplication.translate("Crafting", u"Item", None))
        self.amount_label.setText(QCoreApplication.translate("Crafting", u"Amount", None))
        self.push.setText(QCoreApplication.translate("Crafting", u"Push To Front?", None))
    # retranslateUi

