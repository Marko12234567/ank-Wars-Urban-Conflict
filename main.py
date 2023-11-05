import pygame
from constanes import *
import globals as gl
from logger import logger
from scenes import *
import entity


# Инициализация модулей Pygame
pygame.init()

pygame.display.set_caption("Ank Wars: Urban Conflict")

# Объект для работы со временем
clock = pygame.time.Clock()
APP = True
SCENE = GAME_SCENE


while APP:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            APP = False
    
    if SCENE == MAIN_SCENE:
        pass

    elif SCENE == GAME_SCENE:
        player = entity.Player(IMAGE_PLAYER, 20, 35, 1000, (200, 200), 0.1)
        player.update(events)

    elif SCENE == PAUSE_SCENE:
        pass


    # Обновление экрана
    pygame.display.update()

    clock.tick(FPS)


