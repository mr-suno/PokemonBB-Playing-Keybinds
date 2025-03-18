from functions import *
from simulate import *
from interface import *
from time import *

hotspotTraining = False

def menuOpened():
    openRoblox()

    try:
        XY = recognizeImage("ALL_MENU_BUTTONS.png", "middle")

        if XY is not None:
            return True
        else:
            return False
    except Exception as _:
        return False

def pressMenu():
    XY = recognizeImage("MENU.png", "middle")

    if XY is not None:
        try:
            print(f"[SUCCESS]: Successfully toggled the Menu!")

            CLICKAT(XY[0], XY[1])
        except Exception as _:
            print("[FAILURE]: Unable to find the image. Skipping action.")

    sleep(1)

def flyTo(area):
    if area == "" or area is None:
        print("[FAILURE]: Failed to teleport due to no area being specified!")

        return

    openRoblox()
    closeOpenedInterface()

    print("[WORKING]: Attempting to open Menu...")

    if menuOpened():
        print("[WARNING]: Menu is already opened! Closing menu first...")

        pressMenu()
        sleep(1)

    XY = recognizeImage("MENU.png", "middle")

    if XY is not None:
        try:
            print(f"[SUCCESS]: Successfully opened the Menu!")

            CLICKAT(XY[0], XY[1])
            sleep(1)

            _XY = recognizeImage("PARTY.png", "middle")

            try:
                print(f"[SUCCESS]: Successfully opened your Party!")

                CLICKAT(_XY[0], _XY[1])
                sleep(1)
                
                __XY = recognizeImage("FLY.png", "middle")

                try:
                    print(f"[SUCCESS]: Successfully opened the Map!")

                    CLICKAT(__XY[0], __XY[1])
                except Exception as _:
                    print("[FAILURE]: Unable to find the image. Skipping action.")
            except Exception as _:
                print("[FAILURE]: Unable to find the image. Skipping action.")
        except Exception as _:
            print("[FAILURE]: Unable to find the image. Skipping action.")

    sleep(0.5)

    area = str(area).lower()
    area = area.replace("town", "")
    area = area.replace("city", "")
    area = area.replace(" ", "")
    area = area.upper()
    area = area + ".png"

    openInterface(area, "top")

    sleep(0.5)

    ___XY = recognizeImage("YES_BACKUP.png", "middle")

    if ___XY is not None:
        try:
            print("[SUCCESS]: Confirmed the message confirmation prompt!")

            CLICKAT(___XY[0], ___XY[1])
        except Exception as _:
            print("[FAILURE]: Unable to find the image. Skipping action.")
    else:
        print("[FAILURE]: Attempting to use backup image...")

        ____XY = recognizeImage("YES.png", "middle")

        if ____XY is not None:
            try:
                print("[SUCCESS]: Confirmed the message confirmation prompt!")

                CLICKAT(____XY[0], ____XY[1])
            except Exception as _:
                print("[FAILURE]: Unable to find the image. Skipping action.")
        else:
            print("[FAILURE]: Teleportation failure, confirmation prompt failed to accept!")

    sleep(4)

def healPokemon():
    flyTo("mitis")
    beginNewAction()

    pressKey("d", 1.3)
    pressKey("s", 1)
    pressKey("d", 0.48)

    _XY = recognizeImage("HEALER.png", "middle")

    if _XY is not None:
        print("[WORKING]: Healing all Pokemon...")

        CLICKAT(_XY[0], _XY[1])
        sleep(0.25)

        clickConfirmationArrow()

# def hotspotTrain(enabled):
#     global hotspotTraining

#     if enabled and not hotspotTraining:
#         print("[WORKING]: Setting up Hotspot Training...")

#         flyTo("aredia")
#         sleep(1)

#         pressKey("s", 0.5)
#         pressKey("d", 7.15)
#         pressKey("w", 4)

#         sleep(3)
#         pressKey("a", 2.5)

#         sleep(3)
#         pressKey("s", 1.6)
#         pressKey("a", 10.25)
#         pressKey("w", 2.95)

#         sleep(2)

#         _XY = recognizeImage("AREDIA_ROCK.png", "middle")

#         if _XY is not None:
#             print("[WORKING]: Cracking the boulder...")
#     elif enabled and hotspotTraining:
#         print("[FAILURE]: Already Hotspot Training! Press \"7\" to disable.")
#     else:
#         if hotspotTraining:
#             hotspotTraining = False

#             print("[SUCCESS]: Hotspot Training has been disabled.")