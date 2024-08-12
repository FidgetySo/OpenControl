import sys

from PySide6.QtWidgets import QApplication
from gui.mainwindow import MainWindow


from db.db import DB
from config import Config
from relay.client_relay import ClientRelay


if __name__ == "__main__":
    config = Config()
    database = DB(config)
    relay = ClientRelay(config, database)

    app = QApplication(sys.argv)
    widget = MainWindow(config, database, relay)
    widget.show()
    sys.exit(app.exec())
