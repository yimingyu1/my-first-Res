class Settings():
    """存储关于该游戏的所有设置的类"""
    def __init__(self):
        """初始化游戏设置"""
        #设置游戏屏幕的大小
        self.screen_width=1200
        self.screen_height=700
        #设置游戏屏幕的背景色
        self.bg_color=(230,230,230)
        #设置飞船的移动速度
        self.ship_speed_factor = 10
        #设置子弹的速度、大小、颜色
        self.bullet_speed_factor=5
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed =999
        #设置外星人水平移动
        self.alien_speed_factor=1
        #设置外星人下降的速度
        self.fleet_drop_speed=50
        #设置外星人移动方向（1向右，-1想做）
        self.fleet_direction=1
        #飞船的数量
        self.ship_limit=3