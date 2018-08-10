import os,sys
import maplist_loader.maplist_loader_ui as ui
from PyQt5.QtWidgets import *
import setting

from PyQt5 import QtCore, QtGui, QtWidgets

class Maplistloader_Adapter(QtWidgets.QDialog):
    def __init__(self):
        super(Maplistloader_Adapter,self).__init__()
        self.ui = ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.map_list = []
        #链接鼠标点击事件
        self.ui.pushButton_chooseroute.clicked.connect(self.event_selectroute)
        self.ui.pushButton_readlist.clicked.connect(self.event_loadlist)

    def event_selectroute(self):
        #从文件夹列表选择路径，并更新之
        last_path = self.ui.lineEdit_maplistrounte.text()
        if (last_path == ""):
            last_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = QFileDialog.getExistingDirectory(self, "选择BabyWars地图列表文件路径", last_path)
        if (dir_path != ""):    #选定了目录的场合
            self.ui.lineEdit_maplistrounte.setText(dir_path)

    def event_loadlist(self):
        #从文件中读取存储的地图列表，并显示在itemlist上
        # print(test_1,test_2,test_3)
        pass

    def get_savedpath(self):
        "获取存储文件列表的目录，检测顺序：最后一次使用的->程序根目录设定的->文件路径控件上的文字"
        exist_lastpath = False
        exist_setting_rootpath = False
        exist_inputpath = False
        try:
            lastpath =
            rootpath = setting.ROOT_PATH
            exist_setting_root_path = True
        except NameError:
            #全局变量未设定根目录的情况下
            pass
        pass





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Maplistloader_Adapter()
    dialog.show()
    sys.exit(app.exec_())