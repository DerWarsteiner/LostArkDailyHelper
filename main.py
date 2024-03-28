from helperFunctions import *

pyautogui.FAILSAFE = True

def unaTasksAcceptor():
    # Hotkey Daily Tasks Menu
    altPress('j')
    time.sleep(3)
    moveToLeftWait(1210, 400, 1)
    moveToLeftWait(1210, 455, 1)
    moveToLeftWait(1210, 515, 1)
    pyautogui.keyUp('alt')
    pyautogui.press('esc')

def bifrostTeleport(i):
    # Hotkey Bifrost Menu
    altPress('w')

    match i:
        case 1:
            moveToLeftWait(1345, 430, 1)
            moveToLeftWait(920, 620, 10)

        case 2:
            moveToLeftWait(1345, 490, 1)
            moveToLeftWait(920, 620, 10)

        case 3:
            moveToLeftWait(1345, 550, 1)
            moveToLeftWait(920, 620, 10)

        case 4:
            moveToLeftWait(1345, 650, 1)
            moveToLeftWait(920, 620, 10)

        case 5:
            moveToLeftWait(1345, 710, 1)
            moveToLeftWait(920, 620, 10)
            pyautogui.press('esc')


def lopangWalk():
    bifrostTeleport(1)
    interactQuest()

    # Walk to the second quest
    moveToRightWait(1425, 930, 2)
    moveToRightWait(1425, 930, 2)
    moveToRightWait(1695, 304, 3)
    moveToRightWait(1551, 260, 3)
    moveToRightWait(1551, 210, 3)

    interactQuest()
    time.sleep(1)

    bifrostTeleport(5)
    time.sleep(1)
    interactQuest()

def swichChar(i):

    pyautogui.press('esc')
    time.sleep(1)
    moveToLeftWait(540, 680, 1)
    mousePosition(i)
    leftClickWait(1)
    moveToLeftWait(1030, 685, 1)
    moveToLeftWait(920, 590, 50)

def guildContribution(i):

    # true: Gold Char
    if i < 7:
        # open guild menu
        altPress('u')
        time.sleep(5)

        # donate silver
        moveToLeftWait(1430, 840, 1)
        moveToLeftWait(765, 560, 3)

def mousePosition(i):
    posX = 0
    posY = 0

    if i == 1 or i == 3 or i == 7:
        posX = 760

    elif i == 2 or i == 5 or i == 8:
        posX = 960

    elif i == 3 or i == 6 or i == 9:
        posX = 1160

    if i == 1 or i == 2 or i == 3:
        posY = 440

    elif i == 4 or i == 5 or i == 6:
        posY = 530

    elif i == 7 or i == 8 or i == 9:
        posY = 620

    pyautogui.moveTo(posX, posY)
def unaTasksHandle():

    # Finish the Quests
    for i in range(2, 5):
        bifrostTeleport(i)
        interactQuest()
        time.sleep(1)
        pyautogui.keyDown('shift')
        interactQuest()
        time.sleep(1)
        interactQuest()
        time.sleep(1)
        interactQuest()
        pyautogui.keyUp('shift')
        time.sleep(5)

def main():
    charSlotArray = []
    charAmount = int(input("Enter the amount of characters to use: "))

    for i in range(charAmount):
        charSlot = int(input("Enter character slot " + str(i+1) + ": "))
        charSlotArray.append(charSlot)

    for char in charSlotArray:
        time.sleep(3)
        swichChar(char)
        guildContribution(char)
        unaTasksAcceptor()
        lopangWalk()
        unaTasksHandle()

if __name__ == '__main__':
    main()