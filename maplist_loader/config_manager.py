"config_manager.py：初始化、读取、创建maplist_loader的config.json，并转换为python可识别的格式"

import sys,os
import json

class config_manager():
    def __init__(self):
        pass

    def init_config(self):
        "在当前路径下创建一个包含必要参数的空白的cofing文件"
        cur_path = os.path.realpath(__file__)


if __name__ == "__main__":
    test_object = config_manager()
    test_object.init_config()