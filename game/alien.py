import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_setting,screen):
        super(Alien, self).__init__()
        self.screen=screen
        self.ai_setting= ai_setting
        self.image=pygame.image.load(r'images/alien.bmp')
        self.rect=self.image.get_rect()
        #设置外星人图片的位置
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #保存外形人图片的x坐标
    def blitme(self):
        #在屏幕上显示外形人图片
        self.screen.blit(self.image,self.rect)
    #更新外星人的位置和方向
    def update(self):
        self.x+=self.ai_setting.alien_speed_factor*self.ai_setting.fleet_direction
        self.rect.x=self.x
    #判断外星人是否撞到了边缘
    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if(self.rect.right>=screen_rect.right):
            return True
        elif(self.rect.left<=0):
            return True