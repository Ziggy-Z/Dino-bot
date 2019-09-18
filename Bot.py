from PIL import ImageGrab, ImageOps
import time
import pyautogui
from numpy import *

class Coordinate():
    replayBtn = (1440, 405)
    dinosaur = (1180, 430)
    #1280=xcordinate for tree
    #y=435
def restartGame():
    pyautogui.click(Coordinate.replayBtn)
    pyautogui.keyDown('down')
def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    time.sleep(0.15)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    box = (Coordinate.dinosaur[0]+100, Coordinate.dinosaur[1],
           Coordinate.dinosaur[0]+170, Coordinate.dinosaur[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    while True:
        if (imageGrab()!=597):
            pressSpace()
            time.sleep(0.05)

main()


