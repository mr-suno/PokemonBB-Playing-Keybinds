from functions import *
from simulate import *
from time import *
from interface import *

def movesOpened():
    openRoblox()

    try:
        XY = recognizeImage("BAG.png", "middle")

        if XY is not None:
            return False
        else:
            return True
    except Exception as _:
        return True

def pickChoice(name):
    name = str(name).lower()

    name = name.replace(".png", "") # Remove the ".png" from our name.
    name = name.upper()

    name = f"{name}.png"

    openRoblox()

    print(f"[WORKING]: Scanning for \"{name}\"")

    openInterface(name, "middle")

def inBattle():
    openRoblox()

    try:
        XY = recognizeImage("FIGHT.png", "middle")

        if XY is not None:
            return True
        else:
            return False
    except Exception as _:
        return False

def chooseMove(index):
    if not inBattle():
        print("[FAILURE]: You must be in battle to use this command!")

        return
    
    closeOpenedInterface()

    if not movesOpened():
        print("[WORKING]: Moves aren't showing! Opening moves...")

        pickChoice("fight")

    XY = recognizeImage("FIGHT.png", "middle")

    if XY is not None:
        if index == 1:
            _XY = recognizeImage("TOP_LEFT_MOVE.png", "left")
            __XY = recognizeImage("TOP_LEFT_MOVE_MEGA.png", "left")

            try:
                if _XY is not None:
                    print("[WORKING]: Attempting to use top left move... (Megaless)")

                    CLICKAT(_XY[0], _XY[1])
                else:
                    print("[FAILURE]: Unable to find the image. Skipping action.")
            except Exception as _:
                if __XY is not None:
                    print("[FAILURE]: Attempting to use top left Mega-focused move...")

                    CLICKAT(__XY[0], __XY[1])
                else:
                    print("[FAILURE]: Unable to find the image. Skipping action.")
                
        elif index == 2:
            _XY = recognizeImage("BOTTOM_LEFT_MOVE.png", "left")

            if _XY is not None:
                print("[WORKING]: Attempting to use bottom left move...")

                CLICKAT(_XY[0], _XY[1])
            else:
                print("[FAILURE]: Unable to find the image. Skipping action.")
        elif index == 3:
            _XY = recognizeImage("TOP_RIGHT_MOVE.png", "right")
            __XY = recognizeImage("TOP_RIGHT_MOVE_MEGA.png", "right")

            try:
                if _XY is not None:
                    print("[WORKING]: Attempting to use top right move... (Megaless)")

                    CLICKAT(_XY[0], _XY[1])
                else:
                    print("[FAILURE]: Unable to find the image. Skipping action.")
            except Exception as _:
                if __XY is not None:
                    print("[FAILURE]: Attempting to use top right Mega-focused move...")

                    CLICKAT(__XY[0], __XY[1])
                else:
                    print("[FAILURE]: Unable to find the image. Skipping action.")
        elif index == 4:
            _XY = recognizeImage("BOTTOM_RIGHT_MOVE.png", "right")

            if _XY is not None:
                print("[WORKING]: Attempting to use bottom right move...")

                CLICKAT(_XY[0], _XY[1])
            else:
                print("[FAILURE]: Unable to find the image. Skipping action.")
    else:
        print("[FAILURE]: Unable to find the image. Skipping action.")