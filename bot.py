import pyautogui
import time
from PIL import ImageGrab, ImageOps
from numpy import *

class Coordinates:
    restart_btn = (340,390)
    dino = (90,325)
    box = (126,317,194,356)
    restart_box = (315,294,366,337)
    below_ptero = (243,412,253,422)
    above_petro = (243,387,253,399)

def restart_game():
    pyautogui.click(Coordinates.restart_btn)

def jump():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    print("jump")

def duck():
    pyautogui.keyDown('down')
    time.sleep(0.05)
    pyautogui.keyUp('down')
    print("duck")

def imageGrab(box):
    image   = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    sum = a.sum()
    #print(sum)
    return sum


def is_game_over():
    image = ImageGrab.grab(Coordinates.restart_box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    sum = a.sum()

    if sum == 2934:
        return False
    else:
        return True


def main():
    restart_game()
    while True:
        if imageGrab(Coordinates.below_ptero) != 347:
            jump()
            continue
        if imageGrab(Coordinates.above_petro) != 367:
            duck()

main()
