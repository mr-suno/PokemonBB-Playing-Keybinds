from functions import *
from simulate import *
from time import *
from interface import *
from adventure import *

def useItem(tab, item, inBattle):
    openRoblox()
    
    if anyOpenInterfaces(False):
        closeOpenedInterface()
    if not inBattle:
        if menuOpened():
            pressMenu()

        pressMenu()
        openInterface("BAG_MENU_BACKUP.png")
    else:
        openInterface("BAG.png")

    tab = str(tab).lower()
    tab = tab.replace(" ", "")
    tab = tab.replace(".png", "")

    item = str(item).upper()
    item = item.replace(" ", "_")
    item = item.replace(".PNG", "")
    item += ".png"

    def openTab(tab):
        tab = str(tab).upper()
        tab = tab.replace(".PNG", "")
        tab = tab.replace("_BAG", "")
        tab = tab.replace(" ", "_")
        tab += "_BAG"
        tab += ".png"

        XY = recognizeImage(tab, "middle")

        if XY is not None:
            print("[SUCCESS]: Navigated to corresponding tab")

            CLICKAT(XY[0], XY[1])
            sleep(1)
        else:
            print("[FAILURE]: Failed to open tab.. Skipped action instead.")

    if tab == "items":
        print("[WORKING]: Opening the Items tab...")

        openTab("items")
    elif tab == "medicine":
        print("[WORKING]: Opening the Medicine tab...")

        openTab("medicine")
    elif tab == "pokeballs":
        print("[WORKING]: Opening the Pokeballs tab...")

        openTab("pokeballs")

    openInterface(item)

    XY = recognizeImage(item, "middle")

    if XY is not None:
        XY = recognizeImage("USE_ITEM.png", "middle")

        if XY is not None:
            print("[SUCCESS]: Successfully used item!")

            CLICKAT(XY[0], XY[1])
        else:
            print("[FAILURE]: Failed to use item! Skipped action.")
    else:
        print("[FAILURE]: Could not find the item!")

        return False

def buyItem(item):
    XY = recognizeImage("MERCHANT.png", "middle")

    if XY is not None:
        print("[SUCCESS]: Started chat with Buyer Merchant!")

        CLICKAT(XY[0], XY[1])
        sleep(1)

        clickConfirmationArrow()
        sleep(0.45)

        clickConfirmationArrow()
        sleep(0.)