from abc import ABC, abstractmethod
from constanes import *
import globals as gl
import pygame


class Bonus(ABC):
    def __init__(self):
        pass

    
    @abstractmethod
    def create_bonus(self):
        pass


    @abstractmethod
    def use_bonus(self, player):
        pass


    @abstractmethod
    def delete_bonus(self):
        pass


    @abstractmethod
    def get_info(self):
        pass