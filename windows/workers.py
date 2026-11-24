from PySide6.QtCore import QStringListModel

from ui_workers import Ui_WorkersWindow
from PySide6.QtWidgets import QMdiSubWindow, QWidget, QDialogButtonBox
from database import get_connection

def open_workers(obj):
    if "WorkersWindow" in obj.ui.mdiArea.subWindowList():
        obj.ui.mdiArea.setActiveSubWindow("WorkersWindow")
        return

    workers_widget = QWidget()
    ui_workers = Ui_WorkersWindow()
    ui_workers.setupUi(workers_widget)

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("select name from position_groups order by name")
            group_names = [name for (name,) in cursor.fetchall()]
    ui_workers.listView.setModel(QStringListModel(group_names, ui_workers.listView))

    sub_window = QMdiSubWindow()
    sub_window.setObjectName("WorkersWindow")
    sub_window.setWindowTitle("Справочник работников")

    sub_window.setWidget(workers_widget)
    obj.ui.mdiArea.addSubWindow(sub_window)
    sub_window.show()