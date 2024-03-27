import time, pyautogui

#Read this: Lopang Unas have to be favs. (only Lopang)
#You need the Bifrost in Front the first Terminal as first Bifrost, last Bifrost in front of the last Terminal
# 2-4 are In front of the DeliveryGuys

pyautogui.FAILSAFE = True

def left_clicki(i):
    pyautogui.leftClick()
    time.sleep(i)

def right_clicki(i):
    pyautogui.rightClick()
    time.sleep(i)

def altpress(c):
    pyautogui.keyDown('alt')
    pyautogui.press(c)
    pyautogui.keyUp('alt')

def movetoleft(i, j ,k):
    pyautogui.moveTo(i, j)
    left_clicki(k)

def movetoright(i, j ,k):
    pyautogui.moveTo(i, j)
    right_clicki(k)

def una_tasks():
    altpress('j')
    time.sleep(3)
    movetoleft(1210, 400, 1)
    movetoleft(1210, 455, 1)
    movetoleft(1210, 515, 1)
    pyautogui.keyUp('alt')
    pyautogui.press('esc')

def port(i):#Bifrost i (nummeriert von oben nach unten 1-5)
    altpress('w')
    if i == 1:
        movetoleft(1345, 430, 1)
        movetoleft(920, 620, 10)

    if i == 2:
        movetoleft(1345, 490, 1)
        movetoleft(920, 620, 10)

    if i == 3:
        movetoleft(1345, 550, 1)
        movetoleft(920, 620, 10)

    if i == 4:
        movetoleft(1345, 650, 1)
        movetoleft(920, 620, 10)

    if i == 5:
        movetoleft(1345, 710, 1)
        movetoleft(920, 620, 5)
        pyautogui.press('esc')

def lopang_walk():
    port(1)
    pyautogui.press('g')
    movetoright(1425, 930, 2)
    movetoright(1425, 930, 2)
    movetoright(1695, 304, 3)
    movetoright(1551, 260, 3)
    movetoright(1551, 210, 3)
    pyautogui.press('g')
    time.sleep(1)
    port(5)
    time.sleep(1)
    pyautogui.press('g')

def sw_char(i):
    pyautogui.press('esc')
    time.sleep(1)
    movetoleft(540, 680, 1)
    mouse_pos(i)
    left_clicki(1)
    movetoleft(1030, 685, 1)
    movetoleft(920, 590, 50)

def guild_con(i):
    if ord(i) < 55:
        altpress('u')
        time.sleep(5)
        movetoleft(1430, 840, 1)
        movetoleft(765, 560, 3)

def mouse_pos(i):
    posx = 0
    posy = 0

    if i == '1' or i == '4' or i == '7':
        posx = 760

    if i == '2' or i == '5' or i == '8':
        posx = 960

    if i == '3' or i == '6' or i == '9':
        posx = 1160

    if i == '1' or i == '2' or i == '3':
        posy = 440

    if i == '4' or i == '5' or i == '6':
        posy = 530

    if i == '7' or i == '8' or i == '9':
        posy = 620

    pyautogui.moveTo(posx, posy)
def una_abgabe():
    for i in range(2, 5):
        port(i)
        pyautogui.press('g')
        time.sleep(1)
        pyautogui.keyDown('shift')
        pyautogui.press('g')
        time.sleep(1)
        pyautogui.press('g')
        time.sleep(1)
        pyautogui.press('g')
        pyautogui.keyUp('shift')
        time.sleep(5)

def alt_u_nolopang():
    chars = {'2', '6'}
    for c in chars:
        time.sleep(3)
        sw_char(c)


def una_lopang():
    chars = []  # Leere Liste erstellen
    anzahl_eingaben = int(input("Gib die Anzahl der Eingaben ein: "))

    for i in range(anzahl_eingaben):
        eingabe = input("Gib einen Wert ein: ")
        chars.append(eingabe)  # Wert zur Liste hinzufügen

    for c in chars:
        time.sleep(3)
        sw_char(c)
        guild_con(c)
        una_tasks()
        lopang_walk()
        una_abgabe()

    #alt_u_nolopang()

if __name__ == '__main__':
    una_lopang()
