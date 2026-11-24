from PySide6.QtGui import QStandardItem, QStandardItemModel
from ui_workers import Ui_WorkersWindow
from PySide6.QtWidgets import QMdiSubWindow, QWidget
from PySide6.QtCore import Qt
from database import get_connection

def open_workers(obj):
    if "WorkersWindow" in obj.ui.mdiArea.subWindowList():
        obj.ui.mdiArea.setActiveSubWindow("WorkersWindow")
        return

    workers_widget = QWidget()
    ui_workers = Ui_WorkersWindow()
    ui_workers.setupUi(workers_widget)

    sub_window = QMdiSubWindow()
    sub_window.setObjectName("WorkersWindow")
    sub_window.setWindowTitle("Справочник работников")

    tree = ui_workers.treeView
    tree_model = QStandardItemModel(tree)
    tree_model.setHorizontalHeaderLabels(["Группы и должности"])
    groups = {}
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("select id, name from position_groups order by name")
            for g_id, name in cursor.fetchall():
                group = QStandardItem(name)
                group.setData(g_id, Qt.ItemDataRole.UserRole)
                groups[g_id] = group
                tree_model.appendRow(group)
            cursor.execute("select group_id, name from positions order by name")
            for g_id, name in cursor.fetchall():
                position = QStandardItem(name)
                position.setData(g_id, Qt.ItemDataRole.UserRole)
                groups[g_id].appendRow(position)
    tree.setModel(tree_model)

    table = ui_workers.tableView
    table_model = QStandardItemModel(table)
    table_model.setHorizontalHeaderLabels(["Фамилия", "Имя", "Отчество", "Должность"])
    table.setModel(table_model)
    table.setSortingEnabled(True)

    def show_department_workers(index):
        group_id = index.data(Qt.ItemDataRole.UserRole)
        show_dismissed = ui_workers.is_dismissed.isChecked()

        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    select e.last_name, e.first_name, e.middle_name, p.name
                    from employees e
                    join positions p ON p.id = e.position_id
                    where p.group_id = ?
                      and (? = 1 OR e.status = 'active')
                """, (group_id, int(show_dismissed)))
                workers = cursor.fetchall()

        table_model.setRowCount(0)
        for worker in workers:
            table_model.appendRow([QStandardItem(value or "") for value in worker])
    def show_all_workers():
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                        select e.last_name, e.first_name, e.middle_name, p.name
                        from employees e
                        join positions p on p.id = e.position_id
                        order by e.last_name, e.first_name
                        """)
                workers = cursor.fetchall()
        table_model.setRowCount(0)
        for worker in workers:
            table_model.appendRow([QStandardItem(value or "") for value in worker])

    show_all_workers()

    tree.clicked.connect(show_department_workers)
    ui_workers.is_dismissed.toggled.connect(lambda :show_department_workers(tree.currentIndex()))
    ui_workers.close.clicked.connect(sub_window.close)
    ui_workers.showAll.clicked.connect(show_all_workers)



    sub_window.setWidget(workers_widget)
    obj.ui.mdiArea.addSubWindow(sub_window)
    sub_window.show()