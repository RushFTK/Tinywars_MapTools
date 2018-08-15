# Map.py 定义了存储地图对象的数据结构

class Map(object):
    def __init__(self,map_name = '',autor_name = '',map_player_count = '',map_width = 0,map_height = 0):
        self.name = map_name
        self.author = autor_name
        self.player_count = map_player_count
        self.width = map_width
        self.height = map_height
        self.layer_tileBase = []
        self.layer_tileObject = []
        self.layer_unit = []