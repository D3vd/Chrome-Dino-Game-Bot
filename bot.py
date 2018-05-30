import pyautogui
import time


class Coordinates:
    restart_btn = (339,314)
    dino = (94,324)

def restart_game():
    pyautogui.click(Coordinates.restart_btn)

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')



restart_game()
time.sleep(1)
jump()