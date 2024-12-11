# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(320, 440)
        Widget.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(Widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.groupBox)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.getu = QTextEdit(self.tab)
        self.getu.setObjectName(u"getu")

        self.verticalLayout.addWidget(self.getu)

        self.download = QPushButton(self.tab)
        self.download.setObjectName(u"download")
        self.download.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.download)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gets = QTextEdit(self.tab_2)
        self.gets.setObjectName(u"gets")

        self.verticalLayout_2.addWidget(self.gets)

        self.search = QPushButton(self.tab_2)
        self.search.setObjectName(u"search")

        self.verticalLayout_2.addWidget(self.search)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit = QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit.setFrame(True)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.download_2 = QPushButton(self.tab_3)
        self.download_2.setObjectName(u"download_2")
        self.download_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.download_2)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.lineEdit_2)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_6.addWidget(self.groupBox_2)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"YT Downloader", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Configuraci\u00f3n de descarga", None))
        self.download.setText(QCoreApplication.translate("Widget", u"Descargar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"url", None))
        self.search.setText(QCoreApplication.translate("Widget", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Buscar", None))
        self.download_2.setText(QCoreApplication.translate("Widget", u"Descargar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"csv", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Configuraci\u00f3n de guardado", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Carpeta:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Formato:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"m4a", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"best*", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"bestvideo*", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Widget", u"bestaudio*", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Widget", u"3gp", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Widget", u"aac", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Widget", u"flv", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Widget", u"mp4", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Widget", u"mp3", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Widget", u"ogg", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Widget", u"wav", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("Widget", u"webm", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("Widget", u"worst*", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("Widget", u"worstvideo*", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("Widget", u"worstaudio*", None))

    # retranslateUi

