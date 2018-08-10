# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maplist_loader_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(433, 372)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 411, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_maplistrounte = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_maplistrounte.setObjectName("lineEdit_maplistrounte")
        self.horizontalLayout.addWidget(self.lineEdit_maplistrounte)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.pushButton_chooseroute = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_chooseroute.setObjectName("pushButton_chooseroute")
        self.horizontalLayout_3.addWidget(self.pushButton_chooseroute)
        self.pushButton_readlist = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_readlist.setObjectName("pushButton_readlist")
        self.horizontalLayout_3.addWidget(self.pushButton_readlist)
        self.pushButton_savelist = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_savelist.setObjectName("pushButton_savelist")
        self.horizontalLayout_3.addWidget(self.pushButton_savelist)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.listView_activemaplist = QtWidgets.QListView(self.layoutWidget)
        self.listView_activemaplist.setObjectName("listView_activemaplist")
        self.verticalLayout.addWidget(self.listView_activemaplist)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_newmapitem = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_newmapitem.setObjectName("lineEdit_newmapitem")
        self.horizontalLayout_2.addWidget(self.lineEdit_newmapitem)
        self.pushButton_addnewmapitem = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_addnewmapitem.setObjectName("pushButton_addnewmapitem")
        self.horizontalLayout_2.addWidget(self.pushButton_addnewmapitem)
        self.pushButton_deleteselectitem = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_deleteselectitem.setObjectName("pushButton_deleteselectitem")
        self.horizontalLayout_2.addWidget(self.pushButton_deleteselectitem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MapListEditor"))
        self.label.setText(_translate("Dialog", "地图列表文件路径："))
        self.label_2.setText(_translate("Dialog", "地图列表"))
        self.pushButton_chooseroute.setText(_translate("Dialog", "选择"))
        self.pushButton_readlist.setText(_translate("Dialog", "读取"))
        self.pushButton_savelist.setText(_translate("Dialog", "保存"))
        self.pushButton_addnewmapitem.setText(_translate("Dialog", "添加"))
        self.pushButton_deleteselectitem.setText(_translate("Dialog", "删除"))

