from abc import ABC, abstractmethod
from constanes import *
import globals as gl
import pygame
import sys
import math

pygame.init()
class Entity(ABC):
    """
    Абстрактний клас для створення будь-якої сутності
    """
    def __init__(self, image, width, height):
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))


    @abstractmethod
    def update(self):
        pass


class Enemy(Entity):
    """
    Клас по створенню ворога
    """
    def __init__(self, image, width, height, hp, direction, coords, speed):
        super().__init__(image, width, height)

        self.hp = hp


    def update(self):
        pass


class Player(Entity):
    """
    Клас гравця
    """
    def __init__(self, image, width, height, hp, coords, speed):
        super().__init__(image, width, height)

        self.hp = hp
        self.directon = "right"
        self.x, self.y = coords
        self.speed = speed

    
    def make_move(self, events):
        # Отримання позиції курсора мишки
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Обчислення відстані між гравцем і курсором мишки
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # Обчислення кута між гравцем і курсором мишки
        if distance > 0:
            angle = math.degrees(math.atan2(dy, dx))

            # Оновлення позиції гравця
            for e in events:
                if e.type == pygame.KEYDOWN:
                    # Рух до курсору миші(вперед)
                    if e.key == pygame.K_w:
                        self.x += self.speed * math.cos(math.radians(angle))
                        self.y += self.speed * math.sin(math.radians(angle))

                    # Рух від курсору миші(назад)
                    elif e.key == pygame.K_s:
                        self.x -= self.speed * math.cos(math.radians(angle))
                        self.y -= self.speed * math.sin(math.radians(angle))

        # Перевірка, чи курсор мишки знаходиться в центрі гравця
        if distance <= 1:
            self.x = mouse_x
            self.y = mouse_y




    def update(self, events):
        
        gl.WINDOW.blit(self.image,(self.x, self.y))

        # Постійне оновлення руху
        self.make_move(events)
