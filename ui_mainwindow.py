# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMdiArea,
    QMenu, QMenuBar, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.openSettingsWindow = QAction(MainWindow)
        self.openSettingsWindow.setObjectName(u"openSettingsWindow")
        self.openSettingsWindow.setEnabled(True)
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.action_9 = QAction(MainWindow)
        self.action_9.setObjectName(u"action_9")
        self.action_11 = QAction(MainWindow)
        self.action_11.setObjectName(u"action_11")
        self.action_13 = QAction(MainWindow)
        self.action_13.setObjectName(u"action_13")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")

        self.horizontalLayout.addWidget(self.mdiArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 33))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menuBar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menuBar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu_2.addAction(self.openSettingsWindow)
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_8)
        self.menu_3.addAction(self.action_9)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_11)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_13)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043a\u0430\u0434\u0440\u044b", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0438", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043a\u0430\u0437\u044b", None))
        self.openSettingsWindow.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u043c\u0435\u0441\u0442\u0430", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u0438", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441\u044b \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u043e\u0432", None))
        self.action_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u043e\u0432(\u0434\u043b\u044f \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044f)", None))
        self.action_11.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u043e\u0441\u0442\u0440\u0430\u043d\u043d\u044b\u0435 \u044f\u0437\u044b\u043a\u0438", None))
        self.action_13.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f\u044b \u043f\u0440\u0438\u043a\u0430\u0437\u043e\u0432", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0434\u0440\u044b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0438", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

