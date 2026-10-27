# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(653, 503)
        self.verticalLayout = QVBoxLayout(SettingsWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(SettingsWindow)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.spinBox = QSpinBox(SettingsWindow)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(50, 16777215))
        self.spinBox.setValue(8)

        self.horizontalLayout_2.addWidget(self.spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(SettingsWindow)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.comboBox = QComboBox(SettingsWindow)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_7.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(SettingsWindow)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lineEdit = QLineEdit(SettingsWindow)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_6.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(SettingsWindow)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(SettingsWindow)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(SettingsWindow)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(SettingsWindow)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(SettingsWindow)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(SettingsWindow)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(SettingsWindow)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(SettingsWindow)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(SettingsWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(True)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Close|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"\u041d\u043e\u0440\u043c\u0430 \u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u0434\u043d\u044f (\u0447)", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SettingsWindow", u"\u041f\u0443\u0441\u0442\u043e", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("SettingsWindow", u"\u0411\u044b\u043b", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("SettingsWindow", u"\u0412 \u043e\u0442\u043f\u0443\u0441\u043a\u0435", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("SettingsWindow", u"\u0411\u043e\u043b\u0435\u043d", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("SettingsWindow", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0438\u0440\u043e\u0432\u043a\u0430", None))

        self.label_3.setText(QCoreApplication.translate("SettingsWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0438\u0440\u043c\u044b", None))
        self.lineEdit.setText(QCoreApplication.translate("SettingsWindow", u"\u041e\u041e\u041e \"\u041b\u0430\u0441\u0442\u043e\u0447\u043a\u0430\"", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWindow", u"\u0424\u0418\u041e \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.lineEdit_2.setText(QCoreApplication.translate("SettingsWindow", u"\u0418\u0432\u0430\u043d\u043e\u0432 \u0418.\u0418.", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.lineEdit_3.setText(QCoreApplication.translate("SettingsWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0439 \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440", None))
        self.label_6.setText(QCoreApplication.translate("SettingsWindow", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u0434\u043b\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432 (\u0434\u043d\u0435\u0439)", None))
        self.lineEdit_4.setText(QCoreApplication.translate("SettingsWindow", u"100", None))
        self.label_7.setText(QCoreApplication.translate("SettingsWindow", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u0434\u043b\u044f \u043e\u0442\u0447\u0435\u0442\u043e\u0432 (\u0434\u043d\u0435\u0439)", None))
        self.lineEdit_5.setText(QCoreApplication.translate("SettingsWindow", u"100", None))
    # retranslateUi

