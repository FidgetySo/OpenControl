# This Python file uses the following encoding: utf-8
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

        self.offline = self.config['Debug']['OfflineMode']
        if self.offline:
            print('Running in Offline Debug Mode')

        self.ui = Ui_OpenControl()
        self.ui.setupUi(self)

        self.max_power_len = self.config['GUI']['MaxPowerLen']
        self.power_update_frequency = self.config['Power']['UpdateFrequency']

        self.resize(self.config['GUI']['StartWidth'], self.config['GUI']['StartHeight'])

        self.start_power_update()
        self.input_power_graph()
        self.total_power_graph()

        self.ui.craftingRequest.clicked.connect(self.setup_crafting_dialog)
        self.ui.storage.clicked.connect(self.setup_storage_widget)

    def start_power_update(self):
        self.power_timer = QtCore.QTimer()
        self.power_timer.setInterval(self.power_update_frequency / 2)
        self.power_timer.timeout.connect(self.power_update)
        self.power_timer.start()

    def power_update(self):
        if self.offline:
            self.total_pwoer = randint(0, 100)
            self.input_power = randint(0, 100)
        else:
            self.total_power, self.input_power = self.db.get_power()
    def input_power_graph(self):
        # Set Maximium Data Points for Graph
        self.input_x = list(range(self.max_power_len))
        if self.offline:
            self.input_y = [randint(0, 100) for _ in range(self.max_power_len)]
        else:
            self.input_y = [0 for _ in range(self.max_power_len)]

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
        self.input_timer.setInterval(self.power_update_frequency)
        self.input_timer.timeout.connect(self.update_input_power_graph)
        self.input_timer.start()

    def update_input_power_graph(self):
        del self.input_x[:1]
        self.input_x.append(self.input_x[-1] + 1)

        del self.input_y[:1]
        self.input_y.append(self.input_power)

        self.input_line.setData(self.input_x, self.input_y)

    def total_power_graph(self):
        # Set Maximium Data Points for Graph
        self.total_x = list(range(self.max_power_len))
        if self.offline:
            self.total_y = [randint(0, 100) for _ in range(self.max_power_len)]
        else:
            self.total_y = [0 for _ in range(self.max_power_len)]

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
        self.total_timer.setInterval(self.power_update_frequency)
        self.total_timer.timeout.connect(self.update_total_power_graph)
        self.total_timer.start()

    def update_total_power_graph(self):
        del self.total_x[:1]
        self.total_x.append(self.total_x[-1] + 1)

        del self.total_y[:1]
        self.total_y.append(self.total_power)

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
                method='c_new_crafting',
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

        #Disable Editing of Tables from GUI
        self.storage.storageTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.storage.queueTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.update_storage_widget()
        self.update_crafting_widget()

        self.storage_timer = QtCore.QTimer()

        self.StorageUpdateIntervalInMinutes =  self.config['Storage']['UpdateIntervalInMinutes']
        self.storage_update_interval = self.StorageUpdateIntervalInMinutes * 60000
        self.storage_timer.setInterval(self.storage_update_interval)
        
        self.storage_timer.timeout.connect(self.update_storage_widget)
        self.storage_timer.start()


        self.crafting_timer = QtCore.QTimer()
        self.crafting_timer.setInterval(60000) # refresh crafting queue every 1 minute
        
        self.crafting_timer.timeout.connect(self.update_crafting_widget)
        self.crafting_timer.start()

    def update_storage_widget(self):
        # Updates Storage Table
        storage_query = self.db.get_table_data(enums.TABLES.STORAGE)

        storageIndex = 0
        for i in storage_query:
            self.storage.storageTable.setRowCount(storageIndex + 1)

            # Item
            self.storage.storageTable.setItem(
                storageIndex,
                0,
                QTableWidgetItem(i[0])
            )
            # Amount
            self.storage.storageTable.setItem(
                storageIndex,
                1,
                QTableWidgetItem(str(i[1]))
            )
            # Data
            self.storage.storageTable.setItem(
                storageIndex,
                2,
                QTableWidgetItem(i[2])
            )
            storageIndex += 1
        print('Updated Storage Table')

    def update_crafting_widget(self):
        # Updates Crafting Queue Table
        crafting_query = self.db.get_table_data(enums.TABLES.CRAFTING)

        craftingIndex = 0
        for i in crafting_query:
            self.storage.queueTable.setRowCount(craftingIndex + 1)

            # Item
            self.storage.queueTable.setItem(
                craftingIndex,
                0,
                QTableWidgetItem(i[0])
            )
            # Requested Amount
            self.storage.queueTable.setItem(
                craftingIndex,
                1,
                QTableWidgetItem(str(i[1]))
            )
            # Remaining Amount
            self.storage.queueTable.setItem(
                craftingIndex,
                2,
                QTableWidgetItem(str(i[2]))
            )
            # Number of Processors
            self.storage.queueTable.setItem(
                craftingIndex,
                3,
                QTableWidgetItem(str(i[3]))
            )
            # Date time
            self.storage.queueTable.setItem(
                craftingIndex,
                4,
                QTableWidgetItem(i[4])
            )
            craftingIndex += 1
        print('Updated Crafting Queue')
