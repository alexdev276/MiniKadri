# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'workers.ui'
##
## Created by: Qt User Interface Compiler version 6.10.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QHeaderView,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QTreeView, QVBoxLayout, QWidget)

class Ui_WorkersWindow(object):
    def setupUi(self, WorkersWindow):
        if not WorkersWindow.objectName():
            WorkersWindow.setObjectName(u"WorkersWindow")
        WorkersWindow.resize(651, 521)
        self.verticalLayout_2 = QVBoxLayout(WorkersWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.groups = QPushButton(WorkersWindow)
        self.groups.setObjectName(u"groups")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groups.sizePolicy().hasHeightForWidth())
        self.groups.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.groups)

        self.showAll = QPushButton(WorkersWindow)
        self.showAll.setObjectName(u"showAll")

        self.horizontalLayout.addWidget(self.showAll)

        self.is_dismissed = QCheckBox(WorkersWindow)
        self.is_dismissed.setObjectName(u"is_dismissed")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.is_dismissed.sizePolicy().hasHeightForWidth())
        self.is_dismissed.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.is_dismissed)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.treeView = QTreeView(WorkersWindow)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.treeView)

        self.tableView = QTableView(WorkersWindow)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_3.addWidget(self.tableView)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_6 = QPushButton(WorkersWindow)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(WorkersWindow)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_7 = QPushButton(WorkersWindow)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(WorkersWindow)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.close = QPushButton(WorkersWindow)
        self.close.setObjectName(u"close")

        self.verticalLayout_3.addWidget(self.close)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(WorkersWindow)

        QMetaObject.connectSlotsByName(WorkersWindow)
    # setupUi

    def retranslateUi(self, WorkersWindow):
        WorkersWindow.setWindowTitle(QCoreApplication.translate("WorkersWindow", u"Form", None))
        self.groups.setText(QCoreApplication.translate("WorkersWindow", u"\u0413\u0440\u0443\u043f\u043f\u044b", None))
        self.showAll.setText(QCoreApplication.translate("WorkersWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0441\u0435\u0445", None))
        self.is_dismissed.setText(QCoreApplication.translate("WorkersWindow", u"\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0443\u0432\u043e\u043b\u0435\u043d\u043d\u044b\u0445", None))
        self.pushButton_6.setText(QCoreApplication.translate("WorkersWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_5.setText(QCoreApplication.translate("WorkersWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_7.setText(QCoreApplication.translate("WorkersWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_8.setText(QCoreApplication.translate("WorkersWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.close.setText(QCoreApplication.translate("WorkersWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

