from pyexpat import model

from PySide6.QtGui import QStandardItem, QStandardItemModel
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

    tree = ui_workers.treeView
    tree_model = QStandardItemModel(tree)
    tree_model.setHorizontalHeaderLabels(["Группы и должности"])
    groups = {}
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("select id, name from position_groups order by name")
            for g_id, name in cursor.fetchall():
                group = QStandardItem(name)
                groups[g_id] = group
                tree_model.appendRow(group)
            cursor.execute("select group_id, name from positions order by name")
            for g_id, name in cursor.fetchall():
                groups[g_id].appendRow(QStandardItem(name))
    tree.setModel(tree_model)




    sub_window = QMdiSubWindow()
    sub_window.setObjectName("WorkersWindow")
    sub_window.setWindowTitle("Справочник работников")

    sub_window.setWidget(workers_widget)
    obj.ui.mdiArea.addSubWindow(sub_window)
    sub_window.show()