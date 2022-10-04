#Script to remain available on msteams
import time
import pyautogui

pyautogui.FAILSAFE = False
numMinutes = 2

while(True):
    x =0

    while(x < numMinutes):
        print(str(x))
        time.sleep(60)
        x += 1

    for i in range(0,200):
        pyautogui.moveTo(0,i+4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        pyautogui.press("shift")
        pyautogui.press("control")
    print("Woke up")
    