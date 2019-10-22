import sys
import pygame
from bullet import Bullet
from alien import  Alien
from time import sleep
def check_event(ai_settings,screen,ship,bullets,states,play_button):
    # 监控键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #check_keydown_events(event,ship)
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(states,play_button,mouse_x,mouse_y)
"""相应按键"""
def check_keydown_events(event,ai_settings,screen,ship,bullets):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
           fire_bullet(ai_settings,screen,ship,bullets)
        #退出游戏
        elif event.key == pygame.K_q:
            sys.exit()
"""响应松开"""
def check_keyup_events(event,ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
def update_screen(ai_settings,screen,ship,aliens,bullets,states,play_button):
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #aliens.blitme()
    aliens.draw(screen)
    #aliens.draw(screen)
    if not states.game_active:
        play_button.draw_button()
    # 让绘制的屏幕可见
    pygame.display.flip()
#更新子弹的位置并删除已消失的子弹
def updat_bullets(aliens,ai_settings,screen,ship,bullets):
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(bullets, aliens, screen, ship, ai_settings)
    print(len(bullets))
#子弹和外星人碰撞处理
def check_bullet_alien_collisions(bullets,aliens,screen,ship,ai_settings):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if (len(aliens) == 0):
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
def fire_bullet(ai_settings,screen,ship,bullets):
    # 创建一个子弹
    if (len(bullets) < ai_settings.bullet_allowed):
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
#创建外星人组
def create_fleet(ai_settings,screen,ship,aliens):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien_height=alien.rect.height
    ship_height=ship.rect.height
    number_aliens_x=get_number_aliens_x(ai_settings,alien_width)
    number_rows=get_number_rows(ai_settings,alien_height,ship_height)

    for number_row in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,number_row)
        #计算一行外星人的数量
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
#创建外星人
def create_alien(ai_settings,screen,aliens,alien_number,number_row):
    alien = Alien(ai_settings, screen)
    alien_width=alien.rect.width
    alien_height=alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y=alien_height+2*alien_height*number_row
    alien.rect.x = alien.x
    alien.rect.y=alien.y
    aliens.add(alien)
#计算可以布置多少行
def get_number_rows(ai_settings,alien_height,ship_height):
    available_space_y=ai_settings.screen_height-3*alien_height-ship_height
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows
#更新外星人的位置
def update_aliens(ai_settings,aliens,ship,states,bullets, screen):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #外星人和飞船的碰撞处理
    if(pygame.sprite.spritecollideany(ship,aliens)):
        ship_hit(states, ai_settings, ship, aliens, bullets, screen)
        print('ship hit !!!')
    check_aliens_bottom(ai_settings, states, screen, ship, aliens, bullets)
#将整群外星人向下移，并改变移动方向
def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1
#外星人到达边缘时的处理
def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if(alien.check_edges()):
            change_fleet_direction(ai_settings,aliens)
            break
#碰撞方法
def ship_hit(states,ai_settings,ship,aliens,bullets,screen):
    if states.ship_left>0:
        states.ship_left-=1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        sleep(1)
    else:
        states.game_active=False
#检查外星人是否已到达底部
def check_aliens_bottom(ai_settings,states,screen,ship,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if(alien.rect.bottom>=screen_rect.bottom):
            ship_hit(states, ai_settings, ship, aliens, bullets, screen)
            break
#在玩家点击play按钮时 开始游戏
def check_play_button(states,play_button,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        states.game_active=True






