import pygame as pg
import math
from constanes import *
   
pg.init()
 
def enemy_image_load():
    image = pg.image.load(PATH_ASSETS + 'images/walls/wall2.png')
    
    # image.set_colorkey((255,0,255))
    # transformed_image = pg.transform.rotate(image, 180)
    # orig_image = pg.transform.scale(transformed_image, (40,80))
    return image
 
class Enemy:
    def __init__(self, image, walls):
        self.walls = walls
        self.image = image
        self.rect = self.image.get_rect()
        self.distance_above_player = 10 
        self.speed = 2
         
    def pos_towards_player(self, player_rect):
        c = math.sqrt((player_rect.x - self.rect.x) ** 2 + (player_rect.y - self.distance_above_player  - self.rect.y) ** 2)
        try:
            x = (player_rect.x - self.rect.x) / c
            y = ((player_rect.y - self.distance_above_player)  - self.rect.y) / c
        except ZeroDivisionError: 
            return False
        return (x,y)
         
    def update(self, dt, player):
        enemy_position = (self.rect.x, self.rect.y)
        #move enemy towards player
        new_pos = self.pos_towards_player(player.rect)
        if new_pos: #if not ZeroDivisonError
            self.rect.x, self.rect.y = (self.rect.x + new_pos[0] * self.speed, self.rect.y + new_pos[1] * self.speed)
        for j in self.walls:
            # print(type(player.rect)==type(j))
            if pg.rect.Rect.colliderect(j, self.rect):
                # print(1)
                self.rect.x = enemy_position[0]
                self.rect.y = enemy_position[1]
         
    def draw(self, surf):
        surf.blit(self.image, self.rect)
         
         
class Laser:
    def __init__(self, loc, screen_rect):
        self.screen_rect = screen_rect
        self.image = pg.Surface((5,40)).convert()
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect(center=loc)
        self.speed = 5
   
    def update(self):
        self.rect.y -= self.speed
   
    def render(self, surf):
        surf.blit(self.image, self.rect)
   
class Player:
    def __init__(self, screen_rect, walls):
        self.walls = walls
        self.screen_rect = screen_rect
        self.image = pg.image.load(PATH_ASSETS + 'images/walls/wall1.png').convert()
        self.image.set_colorkey((255,0,255))
        # self.transformed_image = pg.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.dx = 300
        self.dy = 300
        self.speed_x = 5
        self.speed_y = 5
        self.lasers = []
        self.timer = 0.0
        self.laser_delay = 500
        self.add_laser = False
   
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if self.add_laser:
                    self.lasers.append(Laser(self.rect.center, self.screen_rect))
                    self.add_laser = False
   
    def update(self, keys, dt):
        player_pos = (self.rect.x, self.rect.y)
        self.rect.clamp_ip(self.screen_rect)
        # if keys[pg.K_LEFT]:
        #     self.rect.x -= self.speed_x
        # if keys[pg.K_RIGHT]:
        #     self.rect.x += self.speed_x
        # if keys[pg.K_UP]:
        #     self.rect.y -= self.speed_y
        # if keys[pg.K_DOWN]:
        #     self.rect.y += self.speed_y
        mouse_x, mouse_y = pg.mouse.get_pos()
        dx = mouse_x - self.rect.x
        dy = mouse_y - self.rect.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # Обчислення кута між гравцем і курсором мишки
        if distance > 0:
            angle = math.degrees(math.atan2(dy, dx))
        # Оновлення позиції гравця
            self.rect.x += self.speed_x * math.cos(math.radians(angle))
            self.rect.y += self.speed_y * math.sin(math.radians(angle))
        for laser in self.lasers:
            laser.update()
        if pg.time.get_ticks()-self.timer > self.laser_delay:
            self.timer = pg.time.get_ticks()
            self.add_laser = True
        
        for j in self.walls:
            # print(type(player.rect)==type(j))
            if pg.rect.Rect.colliderect(j, self.rect):
                # print(1)
                self.rect.x = player_pos[0]
                self.rect.y = player_pos[1]
        # print(self.speed_x, self.speed_y)
   
    def draw(self, surf):
        for laser in self.lasers:
            laser.render(surf)
        surf.blit(self.image, self.rect)
   

ENEMY_IMAGE = enemy_image_load()

clock = pg.time.Clock()
done = False
# while not done:
#     keys = pg.key.get_pressed()
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             done = True
#         player.get_event(event)
#     screen.fill((0,0,0))
#     delta_time = clock.tick(60)/1000.0
#     player.update(keys, delta_time)
#     enemy.update(delta_time, player)
#     player.draw(screen)
#     enemy.draw(screen)
#     pg.display.update()