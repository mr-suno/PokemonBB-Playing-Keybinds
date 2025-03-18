from functions import *
from simulate import *
from time import *

def anyOpenInterfaces(retrive):
    openRoblox()

    try:
        images = [
            ("BLUE_CANCEL.png", "middle"),
            ("BLUE_CLOSE.png", "middle"),
            ("YELLOW_CLOSE.png", "middle"),
            ("WHITE_CLOSE.png", "middle"),
            ("PINK_CLOSE.png", "middle"),
            ("YELLOW_CLOSE_BACKUP.png", "middle")]

        for file, side in images:
            print(f"[WORKING]: Attempting to search for \"{file}\"...")

            XY = recognizeImage(file, side)
            
            if XY is not None:
                print(f"[SUCCESS]: Found file \"{file}\"!")

                return True, XY if retrive else None
            
        return False, None
    except Exception:
        return False, None

def closeOpenedInterface():
    interfaces, XY = anyOpenInterfaces(True)

    if interfaces:
        print("[SUCCESS]: Closed the interface, checking again...")

        if XY is not None:
            CLICKAT(XY[0], XY[1])
            sleep(1)

            _interfaces, _XY = anyOpenInterfaces(True)

            if _interfaces:
                print("[WORKING]: Found another Window! Closing...")

                if _XY is not None:
                    print("[SUCCESS]: Closed the interface (x2)")

                    CLICKAT(_XY[0], _XY[1])
                    sleep(1)

def openInterface(name, side="middle"):
    if findImage(name):
        print(f"[WORKING]: Looking and matching found cached image...")
        
        XY = recognizeImage(name, side)

        if XY is not None:
            try:
                print(f"[SUCCESS]: Successfully opened Interface!")

                CLICKAT(XY[0], XY[1])
            except Exception as _:
                print("[FAILURE]: Unable to find the image. Skipping action.")
        else:
            print(f"[FAILURE]: Failed to open! Could not find Interface on screen...")
    else:
        print("[FAILURE]: Unable to find the image. Skipping action.")

    sleep(1)