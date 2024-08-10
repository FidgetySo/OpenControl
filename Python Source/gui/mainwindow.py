# This Python file uses the following encoding: utf-8
import sys
import asyncio

from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QWidget,
    QTableWidgetItem,
    QAbstractItemView
)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from gui.ui_form import Ui_OpenControl
from gui.forms.crafting_request import Ui_Crafting
from gui.widgets.storage import Ui_Storage

import pyqtgraph as pg
from random import randint

import enums

class MainWindow(QMainWindow):
    def __init__(self, config, database, relay, parent=None, logic=True):
        super().__init__(parent)
        self.write_config = config.write
        self.config = config.yaml_data
        self.db = database
        self.logic = logic
        self.relay = relay

        self.ui = Ui_OpenControl()
        self.ui.setupUi(self)

        self.input_power_graph()
        self.total_power_graph()

        self.ui.craftingRequest.clicked.connect(self.setup_crafting_dialog)
        self.ui.storage.clicked.connect(self.setup_storage_widget)

    def input_power_graph(self):
        self.input_x = list(range(100))
        self.input_y = [randint(0, 100) for _ in range(100)]

        self.ui.inputGraph.setBackground('w')

        if not self.logic:
            return
        self.pen = pg.mkPen(color=(0, 255, 0), width=2)
        self.input_line = self.ui.inputGraph.plot(
            self.input_x,
            self.input_y,
            pen=self.pen
        )

        self.input_timer = QtCore.QTimer()
        self.InputUpdateFrequnecy = self.config['Power']['InputUpdateFrequnecy']
        self.input_timer.setInterval(self.InputUpdateFrequnecy)
        self.input_timer.timeout.connect(self.update_input_power_graph)
        self.input_timer.start()

    def update_input_power_graph(self):
        del self.input_x[:1]
        self.input_x.append(self.input_x[-1] + 1)

        del self.input_y[:1]
        self.input_y.append(randint(0, 100))

        self.input_line.setData(self.input_x, self.input_y)

    def total_power_graph(self):
        self.total_x = list(range(100))
        self.total_y = [randint(0, 100) for _ in range(100)]

        self.ui.totalGraph.setBackground('w')

        if not self.logic:
            return
        self.pen = pg.mkPen(color=(0, 255, 0), width=2)
        self.total_line = self.ui.totalGraph.plot(
            self.total_x,
            self.total_y,
            pen=self.pen
        )

        self.total_timer = QtCore.QTimer()
        self.TotalUpdateFrequnecy = self.config['Power']['TotalUpdateFrequency']
        self.total_timer.setInterval(self.TotalUpdateFrequnecy)
        self.total_timer.timeout.connect(self.update_total_power_graph)
        self.total_timer.start()

    def update_total_power_graph(self):
        del self.total_x[:1]
        self.total_x.append(self.total_x[-1] + 1)

        del self.total_y[:1]
        self.total_y.append(randint(0, 100))

        self.total_line.setData(self.total_x, self.total_y)

    def setup_crafting_dialog(self):
        self.crafting = QDialog()
        self.crafting.ui = Ui_Crafting()
        self.crafting.ui.setupUi(self.crafting)
        self.setup_craftables()
        self.crafting.ui.ok_cancel.accepted.connect(self.sumbit_crafting_request)
        self.crafting.exec_()
        

    def setup_craftables(self):
        craftables = self.db.get_craftables()
        self.crafting.ui.item.addItems(craftables)

    def sumbit_crafting_request(self):
        asyncio.run(
            self.relay.send(dict(
                method='new_crafting',
                item=self.crafting.ui.item.currentText(),
                amount=self.crafting.ui.amount.value(),
                push=self.crafting.ui.push.isChecked()
                )
            )
        )
    
    def setup_storage_widget(self):
        self.storage_widget = QWidget()
        self.storage = Ui_Storage()
        self.storage.setupUi(self.storage_widget)
        self.storage_widget.show()

        self.storage.storageTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.update_storage_widget()

        self.storage_timer = QtCore.QTimer()

        self.StorageUpdateIntervalInMinutes =  self.config['Storage']['UpdateIntervalInMinutes']
        self.storage_update_interval = self.StorageUpdateIntervalInMinutes * 60000
        self.storage_timer.setInterval(self.storage_update_interval)
        
        self.storage_timer.timeout.connect(self.update_storage_widget)
        self.storage_timer.start()

    def update_storage_widget(self):
        storage_query = self.db.get_table_data(enums.TABLES.STORAGE)

        storageIndex = 0
        for i in storage_query:
            self.storage.storageTable.setRowCount(storageIndex + 1)
            self.storage.storageTable.setItem(
                storageIndex,
                0,
                QTableWidgetItem(i[0])
            )
            self.storage.storageTable.setItem(
                storageIndex,
                1,
                QTableWidgetItem(i[1])
            )
            self.storage.storageTable.setItem(
                storageIndex,
                2,
                QTableWidgetItem(i[2])
            )
            storageIndex += 1
        print('Updated Storage Table')
