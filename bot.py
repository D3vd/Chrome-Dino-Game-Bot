import pyautogui


class Coordinates:
    restart_btn = (339,314)
    dino = (94,324)

def restart_game():
    pyautogui.click(Coordinates.restart_btn)
def jump():
    pyautogui.keyDown('space')

restart_game()
jump()