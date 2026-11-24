from ui_settings import Ui_SettingsWindow
from PySide6.QtWidgets import QMdiSubWindow, QWidget, QDialogButtonBox
from database import get_connection


def save_settings(hours: int, default_fill: str, company_name: str, head_full_name: str, head_position: str,
                  interval_docs: int, interval_reps: int):
    settings = (
        (hours, 'norma'),
        (default_fill, 'status'),
        (company_name, 'company name'),
        (head_full_name, 'director fullname'),
        (head_position, 'director job'),
        (interval_docs, 'document interval'),
        (interval_reps, 'order interval'),
    )
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.executemany("""update settings set settings_value = ? where settings_key = ?""",
                               settings)
        connection.commit()
    print("saved")


def get_settings():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""select settings_key, settings_value from settings""")
            return cursor.fetchall()


def open_settings(obj):
    if "SettingsWindow" in obj.ui.mdiArea.subWindowList():
        obj.ui.mdiArea.setActiveSubWindow("SettingsWindow")
        return

    settings_widget = QWidget()
    ui_settings = Ui_SettingsWindow()
    ui_settings.setupUi(settings_widget)

    settings = get_settings()
    print(settings)
    ui_settings.spinBox.setValue(int(settings[0][1]))
    ui_settings.comboBox.setCurrentText(settings[1][1])
    ui_settings.lineEdit.setText(settings[2][1])
    ui_settings.lineEdit_2.setText(settings[3][1]),
    ui_settings.lineEdit_3.setText(settings[4][1]),
    ui_settings.lineEdit_4.setText(settings[5][1]),
    ui_settings.lineEdit_5.setText(settings[6][1]),
    print("changed")

    sub_window = QMdiSubWindow()
    sub_window.setObjectName("SettingsWindow")
    sub_window.setWindowTitle("Настройка рабочего места")

    ui_settings.buttonBox.accepted.connect(lambda: save_settings(
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
    obj.ui.mdiArea.addSubWindow(sub_window)
    sub_window.show()
    print("started")
