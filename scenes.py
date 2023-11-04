from abc import ABC, abstractmethod
import globals as gl


class Scene(ABC):
    def __init__(self):
        pass

    
    @abstractmethod
    def update(self):
        pass


class Game_Scene(Scene):
    def __init__(self):
        pass

    def update(self):
        pass