import pygame
from constanes import *
import globals as gl
from logger import logger
from scenes import *


# Инициализация модулей Pygame
pygame.init()

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
        pass

    elif SCENE == PAUSE_SCENE:
        pass


    # Обновление экрана
    pygame.display.update()

    clock.tick(FPS)


