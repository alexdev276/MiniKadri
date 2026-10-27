from PySide6 import QtWidgets

from ui_mainwindow import Ui_MainWindow
from ui_settings import Ui_SettingsWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QWidget, QDialogButtonBox


def save_settings(hours: int, default_fill: str, company_name: str, head_full_name: str, head_position: str,
                  interval_docs: int, interval_reps: int):
    print("Saved seetings:}", hours, default_fill, company_name, head_full_name, head_position, interval_docs,
          interval_reps, sep='\n')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.openSettingsWindow.triggered.connect(self.open_settings)

    def open_settings(self):
        if "SettingsWindow" in self.ui.mdiArea.subWindowList():
            self.ui.mdiArea.setActiveSubWindow("SettingsWindow")
            return

        settings_widget = QWidget()
        ui_settings = Ui_SettingsWindow()
        ui_settings.setupUi(settings_widget)

        sub_window = QMdiSubWindow()
        sub_window.setObjectName("SettingsWindow")
        sub_window.setWindowTitle("Настройка рабочего места")

        ui_settings.buttonBox.accepted.connect(lambda: self.saveSettings(
            ui_settings.spinBox.value(),
            ui_settings.comboBox.currentText(),
            ui_settings.lineEdit.text(),
            ui_settings.lineEdit_2.text(),
            ui_settings.lineEdit_3.text(),
            ui_settings.lineEdit_4.text(),
            ui_settings.lineEdit_5.text(),
        ))
        ui_settings.buttonBox.rejected.connect(sub_window.close)
        close_btn = ui_settings.buttonBox.button(QDialogButtonBox.Close)
        close_btn.clicked.connect(sub_window.close)

        sub_window.setWidget(settings_widget)
        self.ui.mdiArea.addSubWindow(sub_window)
        sub_window.show()

    
