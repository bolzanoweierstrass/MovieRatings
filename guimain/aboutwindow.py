# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Sat Jan 17 10:59:44 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(560, 353)
        Form.setMinimumSize(QtCore.QSize(560, 353))
        Form.setMaximumSize(QtCore.QSize(560, 353))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_about = QtGui.QWidget()
        self.page_about.setObjectName(_fromUtf8("page_about"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_about)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.page_about)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/ico/video.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label, QtCore.Qt.AlignHCenter)
        self.label_2 = QtGui.QLabel(self.page_about)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 80))
        self.label_2.setMaximumSize(QtCore.QSize(200, 80))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_about)
        self.page_credits = QtGui.QWidget()
        self.page_credits.setObjectName(_fromUtf8("page_credits"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_credits)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.page_credits)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_credits = QtGui.QWidget()
        self.tab_credits.setObjectName(_fromUtf8("tab_credits"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_credits)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_credits)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab_credits, _fromUtf8(""))
        self.tab_license = QtGui.QWidget()
        self.tab_license.setObjectName(_fromUtf8("tab_license"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_license)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_license)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.verticalLayout_5.addWidget(self.textBrowser_2)
        self.tabWidget.addTab(self.tab_license, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.page_credits)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.frame = QtGui.QFrame(Form)
        self.frame.setMinimumSize(QtCore.QSize(0, 60))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setBaseSize(QtCore.QSize(0, 60))
        self.frame.setStyleSheet(_fromUtf8("QFrame{\n"
"border:None;\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tBn_about = QtGui.QToolButton(self.frame)
        self.tBn_about.setMinimumSize(QtCore.QSize(80, 40))
        self.tBn_about.setCheckable(True)
        self.tBn_about.setChecked(True)
        self.tBn_about.setAutoExclusive(True)
        self.tBn_about.setObjectName(_fromUtf8("tBn_about"))
        self.horizontalLayout_2.addWidget(self.tBn_about)
        self.tBn_credits = QtGui.QToolButton(self.frame)
        self.tBn_credits.setMinimumSize(QtCore.QSize(80, 40))
        self.tBn_credits.setCheckable(True)
        self.tBn_credits.setAutoExclusive(True)
        self.tBn_credits.setObjectName(_fromUtf8("tBn_credits"))
        self.horizontalLayout_2.addWidget(self.tBn_credits)
        spacerItem = QtGui.QSpacerItem(263, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.tBn_close = QtGui.QToolButton(self.frame)
        self.tBn_close.setMinimumSize(QtCore.QSize(80, 40))
        self.tBn_close.setObjectName(_fromUtf8("tBn_close"))
        self.horizontalLayout_2.addWidget(self.tBn_close)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.tBn_close, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "about", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p> this program is created by</p><p>basant acharya</p><p>effectdoppler8@gmail.com</p></body></html>", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this program is created by</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">name: basant acharya</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">mail:effectdoppler8@gmail.com</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">if you have any comments and suggestions feel free to mail me.. :)</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_credits), _translate("Form", "credits", None))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Movie ratings viewer is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Movie Ratings viewer is distributed in the hope that it will be useful,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">but WITHOUT ANY WARRANTY; without even the implied warranty of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GNU General Public License for more details.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You should have received a copy of the GNU General Public License</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">along with this software; if not, write to the Free Software Foundation, Inc.,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For further information you can also visit http://www.gnu.org/licenses/gpl.html</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_license), _translate("Form", "license", None))
        self.tBn_about.setText(_translate("Form", "about", None))
        self.tBn_credits.setText(_translate("Form", "credits", None))
        self.tBn_close.setText(_translate("Form", "close", None))

import resource
