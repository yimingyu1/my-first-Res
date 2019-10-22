import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_sates import GameStates
from button import Button
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #设置界面样式（创建一个设置的对象）
    ai_settings=Settings()
    #显示窗口
    screen =pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #设置窗口标题
    pygame.display.set_caption("Alien Invasiofn")
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建外星人
    alien=Alien(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets=Group()
    #创建一个外星人组
    aliens=Group()
    #创建外星人群
    #创建一个保存游戏统计信息的对象
    states=GameStates(ai_settings)
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建开始按钮
    play_button=Button(ai_settings,screen,"play")
    #开始游戏主循环q
    while True:
        #监听键盘和鼠标事件
       # gf.check_event(ship)
        gf.check_event(ai_settings,screen,ship,bullets,states,play_button)
        # 飞船移动
        if states.game_active:
            ship.update()
            gf.updat_bullets(aliens,ai_settings,screen,ship,bullets)
            gf.update_aliens(ai_settings,aliens,ship,states,bullets, screen)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets,states,play_button)
        #跟新屏幕图像
        #gf.update_screen(ai_settings,screen,ship)


run_game()