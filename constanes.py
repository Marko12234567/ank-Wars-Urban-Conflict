import os

# Розміри вікна
WIN_WIDTH = 1280
WIN_HEIGHT = 720

# Кількість кадрів за секунду
FPS = 60


# PATH
PATH = os.path.dirname(__file__) + os.sep
PATH_ASSETS = PATH + "assets" + os.sep

PATH_SOUNDS = PATH_ASSETS + "sounds" + os.sep
PATH_IMAGES = PATH_ASSETS + "images" + os.sep

PATH_WALLS = PATH_IMAGES + "walls" + os.sep
PATH_GROUNDS =  PATH_IMAGES + "grounds" + os.sep

# SCENES
MAIN_SCENE = 0
GAME_SCENE = 1
PAUSE_SCENE = 2


# IMAGES
IMAGE_PLAYER = PATH_WALLS + "wall1.png"
