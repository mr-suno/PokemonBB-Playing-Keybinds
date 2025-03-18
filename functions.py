import cv2
import numpy

from pyautogui import *
from time import *
from os import *
from pygetwindow import *
from math import *
from simulate import *
from keyboard import *

movementKeys = ["w","a","s","d"]

def findImage(name):
    for dirpath, _, files in walk("."):
        for file in files:
            if str(file).lower() == str(name).lower():
                return path.join(dirpath, file)
    return None

def openRoblox():
    print("[WORKING]: Focusing on Roblox...")

    window = getWindowsWithTitle("Roblox")[0]
    window.activate()
    
    sleep(0.05)

def pressKey(key, length):
    openRoblox()

    key = str(key).lower()

    def movementKey(key):
        return key in movementKeys
    
    if movementKey(key):
        print("[NOTICES]: Detected movement key! Holding down shift to move quicker.");
        press("shift")

    print(f"[WORKING]: Holding down \"{key}\" for {length} second(s)...")
    press(key)

    sleep(length) # Wait before releasing.
    
    release(key)
    if movementKey(key):
        release("shift")

    print("[SUCCESS]: Released all computer-pressed keys!")

def recognizeImage(name, side):
    savedPositions = []

    savedScreenshot = screenshot()
    savedScreenshot = numpy.array(savedScreenshot)
    savedScreenshot = cv2.cvtColor(savedScreenshot, cv2.COLOR_RGB2BGR)

    buttonImage = cv2.imread(findImage(name))

    if buttonImage is None:
        return None

    scales = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]

    bestMatchValue = -1
    bestMatchPosition = None

    for scale in scales:
        resizedButton = cv2.resize(buttonImage, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        match = cv2.matchTemplate(savedScreenshot, resizedButton, cv2.TM_CCOEFF_NORMED)

        threshold = 0.8
        locations = numpy.where(match >= threshold)

        for point in zip(*locations[::-1]):
            matchValue = match[point[1], point[0]]
            if matchValue > bestMatchValue:
                bestMatchValue = matchValue
                bestMatchPosition = point

                centerX = point[0] + (resizedButton.shape[1] // 2)
                centerY = point[1] + (resizedButton.shape[0] // 2)

                if side == "left":
                    centerX = point[0]
                elif side == "right":
                    centerX = point[0] + resizedButton.shape[1]
                elif side == "top":
                    centerY = point[1]
                elif side == "bottom":
                    centerY = point[1] + resizedButton.shape[0]

                savedPositions = [centerX, centerY]

    if bestMatchValue >= threshold:
        cv2.rectangle(savedScreenshot, bestMatchPosition, (bestMatchPosition[0] + resizedButton.shape[1], bestMatchPosition[1] + resizedButton.shape[0]), (0, 255, 0), 2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return savedPositions if savedPositions else None

def closeChat():
    pass

def clickConfirmationArrow():
    if findImage("CONFIRMATION_ARROW.png"):
        print(f"[WORKING]: Searching for confirmation arrow...")
        
        XY = recognizeImage("CONFIRMATION_ARROW.png", "middle")

        def startCounter():
            attempts = 3
            count = 0

            while count <= attempts:
                if XY is not None:
                    print("[SUCCESS]: Continued narrative dialog!")

                    CLICKAT(XY[0], XY[1])

                    return True

                sleep(0.15)
                count += 1

            return False
        try:
            if XY is not None:
                print("[SUCCESS]: Continued narrative dialog!")

                CLICKAT(XY[0], XY[1])

                return True
            else:
                return startCounter()
        except Exception as _:
            return startCounter()
    else:
        print("[FAILURE]: Unable to find the image. Skipping action.")

        return False

def continueDialogUntilFinished():
    openRoblox()

    timesUntilBreak = 2
    currentTimesChecked = 0
    clicked = False

    while currentTimesChecked <= timesUntilBreak:
        XY = recognizeImage("YES_BACKUP.png", "middle")

        if clickConfirmationArrow():
            print(f"[SUCCESS]: Confirmation Arrow found & clicked! Reset checked counter.")

            currentTimesChecked = 0
            clicked = True

            continue

        if XY is not None:
            print("[NOTICES]: Confirmation Prompt showed up! Clicking YES...")
            CLICKAT(XY[0], XY[1])

            clicked = True
            continue

        if not clicked:
            print(f"[FAILURE]: Confirmation Arrow couldn't be found! ({currentTimesChecked}/{timesUntilBreak})")

        currentTimesChecked += 1

    if not clicked:
        print("[FAILURE]: Times checked exceeded limit! Skipping action.")
    else:
        print("[SUCCESS]: Finished dialog!")

    sleep(1)

def beginNewAction():
    print("[WORKING]: Zooming out camera...")

    pressKey("o", 0.3)