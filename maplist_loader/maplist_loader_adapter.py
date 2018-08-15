import os,sys
import maplist_loader.maplist_loader_ui as ui
from PyQt5.QtWidgets import *
from maplist_loader.config_manager import Config_Manager
import setting

from PyQt5 import QtCore, QtGui, QtWidgets

class Maplistloader_Adapter(QtWidgets.QDialog):
    def __init__(self):
        super(Maplistloader_Adapter,self).__init__()
        self.relative_path = 'res\\data\\templateWarField'
        self.ui = ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.map_list = []
        self.last_success_loadpath = ''
        self.success_load = False
        self.startindex = { '2p':   0, 'Fun 2p':   0,'3p':  0, '4p':    0,'random': 0,'test':0 }
        self.startindex_tag = ['2p','Fun 2p','3p','4p','random','test']
        self.startindex_key = ['-- 2p', '-- Fun 2p maps', '-- 3p', '-- 4p', '-- random maps', '-- test maps']
        self.ui.comboBox_newitemtag.addItems(self.startindex_tag)
        self.ui.lineEdit_maplistrounte.setText(self.get_savedpath())
        #链接鼠标点击事件
        self.ui.pushButton_chooseroute.clicked.connect(self.event_selectroute)
        self.ui.pushButton_readlist.clicked.connect(self.event_loadlist)
        self.ui.pushButton_savelist.clicked.connect(self.event_savelist)

    def closeEvent(self, QCloseEvent):
        if (self.success_load):
            Config_Manager.save_lastpath(self.last_success_loadpath,force=True)

    def event_selectroute(self):
        #从文件夹列表选择路径，并更新之
        last_path = self.ui.lineEdit_maplistrounte.text()
        if (last_path == ''):
            last_path = os.path.dirname(os.path.realpath(__file__))
        print(last_path)
        dir_path = QFileDialog.getExistingDirectory(self, '选择BabyWars GitClone项目路径', directory=last_path+'\\')
        if (dir_path != ''):    #选定了目录的场合
            self.ui.lineEdit_maplistrounte.setText(dir_path +  '\\' + self.relative_path)

    def event_loadlist(self):
        "从文件中读取存储的地图列表，备份，处理后显示在itemlist上"
        current_startindex_mark = 0
        path = self.ui.lineEdit_maplistrounte.text()
        with open(path + '\\WarFieldList.lua', 'r') as f1 , open(path + '\\WarFieldList.lua.bak','w') as f2:
            original_file = f1.readlines()
            f2.writelines(original_file)
            self.map_list = original_file[1:-1]
        #删除分行后缀，寻找各种类地图标志
        for i in range(0,len(self.map_list)):
            if (self.map_list[i][-1:] == '\n'):
                self.map_list[i] = self.map_list[i][:-1]
                #按顺序查找下一个关键词：current_startindex_mark 待查找的关键词序号 startindex_tag：序号所队形的关键词字典索引 startindex_key：序号所对应的关键词在地图列表中的位置
                if (current_startindex_mark < len(self.startindex_key)):
                    if (self.map_list[i].find(self.startindex_key[current_startindex_mark])!= -1):
                        self.startindex[self.startindex_tag[current_startindex_mark]] = i
                        current_startindex_mark = current_startindex_mark + 1
        self.update_listbox()
        self.success_load = True
        self.last_success_loadpath = path

    def event_savelist(self):
        "将修改好的文件列表转换并存储至原有WarFieldList中"
        insert_list = self.map_list
        for i in range(0,len(insert_list)):
            insert_list[i] = insert_list[i] + '\n'
        insert_list.insert(0,'return {\n')
        insert_list.append('}\n')
        path = self.last_success_loadpath
        with open(path + '\\WarFieldList.lua', 'w') as f:
            f.writelines(insert_list)
        pass

    def event_insertitem(self):
        "TODO:将合法的项插入刀MapList中"

    def event_deleteitem(self):
        "TODO:将选中的项从列表中删除"
        pass

    def get_savedpath(self):
        "获取存储文件列表的目录，检测顺序：最后一次使用的->程序根目录设定的->文件路径控件上的文字"
        lastpath = Config_Manager.get_lastpath()
        if (lastpath != None):
            result_path = lastpath
        else:
            try:
                rootpath = setting.ROOT_PATH
                result_path = rootpath + '\\' + self.relative_path
            except AttributeError:
                result_path = self.ui.lineEdit_maplistrounte.text()
        return result_path

    def update_listbox(self):
        "更新listbox"
        self.ui.listWidget_activemaplist.clear()
        self.ui.listWidget_activemaplist.addItems(self.map_list)
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Maplistloader_Adapter()
    dialog.show()
    sys.exit(app.exec_())