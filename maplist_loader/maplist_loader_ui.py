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
        Dialog.resize(449, 373)
        Dialog.setMinimumSize(QtCore.QSize(150, 0))
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 422, 351))
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
        self.listWidget_activemaplist = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_activemaplist.setObjectName("listWidget_activemaplist")
        self.verticalLayout.addWidget(self.listWidget_activemaplist)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBox_newitemtag = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_newitemtag.sizePolicy().hasHeightForWidth())
        self.comboBox_newitemtag.setSizePolicy(sizePolicy)
        self.comboBox_newitemtag.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_newitemtag.setObjectName("comboBox_newitemtag")
        self.horizontalLayout_4.addWidget(self.comboBox_newitemtag)
        self.pushButton_addnewmapitem = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_addnewmapitem.setObjectName("pushButton_addnewmapitem")
        self.horizontalLayout_4.addWidget(self.pushButton_addnewmapitem)
        self.pushButton_deleteselectitem = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_deleteselectitem.setObjectName("pushButton_deleteselectitem")
        self.horizontalLayout_4.addWidget(self.pushButton_deleteselectitem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_newmapitem = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_newmapitem.setObjectName("lineEdit_newmapitem")
        self.horizontalLayout_5.addWidget(self.lineEdit_newmapitem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)

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
        self.label_5.setText(_translate("Dialog", "地图种类"))
        self.pushButton_addnewmapitem.setText(_translate("Dialog", "添加"))
        self.pushButton_deleteselectitem.setText(_translate("Dialog", "删除"))
        self.label_4.setText(_translate("Dialog", "地图名称"))

