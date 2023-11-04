from abc import ABC, abstractmethod
from constanes import *
import pygame

class Entity(ABC):
    """
    Абстрактний клас для створення будь-якої сутності
    """
    def __init__(self, image, width, height, direction, coords, speed):
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))

        self.direction = direction
        self.coords = coords
        self.speed = speed

    

    def make_move(self):
        pass

    @abstractmethod
    def update(self):
        pass


class Enemy(Entity):
    """
    Клас по створенню ворога
    """
    def __init__(self, image, width, height, hp, direction, coords, speed):
        super().__init__(image, width, height, direction, coords, speed)

        self.hp = hp


    def update(self):
        pass


class Player(Entity):
    """
    Клас гравця
    """
    def __init__(self, image, width, height, hp, direction, coords, speed):
        super().__init__(image, width, height, direction, coords, speed)

        self.hp = hp


    def update(self):
        pass