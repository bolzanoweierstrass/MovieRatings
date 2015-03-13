# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Feb 21 13:56:29 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(769, 609)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/drop.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lne_url = QtGui.QLineEdit(self.layoutWidget)
        self.lne_url.setMaxLength(90)
        self.lne_url.setObjectName(_fromUtf8("lne_url"))
        self.horizontalLayout.addWidget(self.lne_url)
        self.cmb_input = QtGui.QComboBox(self.layoutWidget)
        self.cmb_input.setObjectName(_fromUtf8("cmb_input"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/eye.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmb_input.addItem(icon1, _fromUtf8(""))
        self.cmb_input.addItem(icon1, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmb_input)
        self.tBn_search = QtGui.QToolButton(self.layoutWidget)
        self.tBn_search.setIcon(icon1)
        self.tBn_search.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.tBn_search.setObjectName(_fromUtf8("tBn_search"))
        self.horizontalLayout.addWidget(self.tBn_search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.txtB_title = QtGui.QTextBrowser(self.layoutWidget)
        self.txtB_title.setObjectName(_fromUtf8("txtB_title"))
        self.horizontalLayout_3.addWidget(self.txtB_title)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.lbl_pic = QtGui.QLabel(self.splitter)
        self.lbl_pic.setMinimumSize(QtCore.QSize(300, 445))
        self.lbl_pic.setMaximumSize(QtCore.QSize(300, 445))
        self.lbl_pic.setText(_fromUtf8(""))
        self.lbl_pic.setPixmap(QtGui.QPixmap(_fromUtf8("../Pictures/head.jpg")))
        self.lbl_pic.setObjectName(_fromUtf8("lbl_pic"))
        self.verticalLayout_2.addWidget(self.splitter)
        self.txtB_plot = QtGui.QTextBrowser(self.centralwidget)
        self.txtB_plot.setObjectName(_fromUtf8("txtB_plot"))
        self.verticalLayout_2.addWidget(self.txtB_plot)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionPreference = QtGui.QAction(MainWindow)
        self.actionPreference.setObjectName(_fromUtf8("actionPreference"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreference)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionPaste, QtCore.SIGNAL(_fromUtf8("triggered()")), self.lne_url.paste)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Ratings viewer", None))
        self.lne_url.setStatusTip(_translate("MainWindow", "type the name of the move", None))
        self.cmb_input.setItemText(0, _translate("MainWindow", "title", None))
        self.cmb_input.setItemText(1, _translate("MainWindow", "search", None))
        self.tBn_search.setText(_translate("MainWindow", "search", None))
        self.tBn_search.setShortcut(_translate("MainWindow", "Return", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.menuEdit.setTitle(_translate("MainWindow", "edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.actionPaste.setText(_translate("MainWindow", "paste", None))
        self.actionPreference.setText(_translate("MainWindow", "preference", None))
        self.actionAbout.setText(_translate("MainWindow", "about", None))
        self.actionClose.setText(_translate("MainWindow", "close", None))

import resource
