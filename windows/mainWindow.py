from ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from windows.settings import open_settings
from windows.workers import open_workers


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.openSettingsWindow.triggered.connect(lambda :open_settings(self))
        self.ui.openWorkersWindow.triggered.connect(lambda :print("workers"))



