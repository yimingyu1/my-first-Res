import pygame
class Ship():
    def __init__(self,ai_settings,screen):
        self.moving_right=False
        self.moving_left=False
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load(r'images/ship.bmp')
        #返回飞船图片的外接矩形
        self.rect=self.image.get_rect()
        #返回屏幕窗口的外接矩形
        self.screen_rect=screen.get_rect()
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
    def update(self):
        if (self.moving_right) and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        elif(self.moving_left) and (self.rect.left>0):
            self.center-=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.center
    def center_ship(self):
        self.center = self.screen_rect.centerx