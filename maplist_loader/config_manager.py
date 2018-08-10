"config_manager.py：初始化、读取、创建maplist_loader的config.json，并转换为python可识别的格式"

import sys,os
import json

class Config_Manager():
    def __init__(self):
        pass

    @staticmethod
    def init_config():
        "在当前路径下创建一个包含必要参数的空白的cofing文件"
        initdata = {
            'last_path' : '',
        }
        if (not Config_Manager.save_config(initdata)):
            return 0
        else:
            return 1

    @staticmethod
    def save_config(config_data):
        "将json字符串存储到文件中"
        try:
            with open('config.json','w') as f:
                json.dump(config_data, f , sort_keys=True, indent=4, separators=(',', ': '))
        except Exception as e:
            print(e)
            return 1
        return 0

    @staticmethod
    def load_config():
        "从config.json中读取信息"
        try:
            with open('config.json', 'r') as f:
                data = json.load(f)
        except Exception as e:
            print(e)
            return None
        return data

    @staticmethod
    def get_lastpath():
        "从config.json中读取lastpath字段"
        data = Config_Manager.load_config()
        if (data == None):
            return None
        else:
            return data['last_path']

    @staticmethod
    def save_lastpath(new_lastpath,force = False):
        "在其他变量不变的情况下，更新lastpath字段，force=True时，没有config文件将会进行创建"
        data = Config_Manager.load_config()
        if (data == None):
            if (force == False):
                return 1,"config.json不存在"
            else:
                Config_Manager.init_config()
                data = Config_Manager.load_config()
        data['last_path'] = new_lastpath
        result = Config_Manager.save_config(data)
        return result


if __name__ == "__main__":
    Config_Manager.init_config()
    Config_Manager.save_lastpath(os.path.dirname(os.path.realpath(__file__)))
    pass