import sys

from PySide6.QtWidgets import QApplication
from gui.mainwindow import MainWindow

import enums

from db.db import DB
from config import Config


if __name__ == "__main__":
    config = Config()
    database = DB(config)

    app = QApplication(sys.argv)
    widget = MainWindow(config, database)
    widget.show()
    sys.exit(app.exec())
