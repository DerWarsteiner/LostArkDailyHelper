import time, pyautogui

pyautogui.FAILSAFE = True

def leftClickWait(min):
    pyautogui.leftClick()
    time.sleep(min)

def rightClickWait(min):
    pyautogui.rightClick()
    time.sleep(min)

def altPress(key):
    pyautogui.keyDown('alt')
    pyautogui.press(key)
    pyautogui.keyUp('alt')

def moveToLeftWait(x, y, min):
    pyautogui.moveTo(x, y)
    leftClickWait(min)

def moveToRightWait(x, y, min):
    pyautogui.moveTo(x, y)
    rightClickWait(min)

def interactQuest():
    pyautogui.press("g")