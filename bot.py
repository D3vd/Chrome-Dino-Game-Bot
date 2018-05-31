import pyautogui
import time
from PIL import ImageGrab, ImageOps
from numpy import *

class Coordinates:
    restart_btn = (339,314)
    dino = (90,325)

def restart_game():
    pyautogui.click(Coordinates.restart_btn)

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def imageGrab():
    box = (126,317,194,356 )
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()


def main():
    restart_game()
    while True:
        if imageGrab() != 2899 :
            jump()
            time.sleep(0.2)

main()