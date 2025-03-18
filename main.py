from keyboard import *
from battle import *
from adventure import *
from tkinter import *
from items import *

add_hotkey("1", lambda: chooseMove(1)) # BATTLE MOVE - 1
add_hotkey("2", lambda: chooseMove(2)) #             - 2
add_hotkey("3", lambda: chooseMove(3)) #             - 3
add_hotkey("4", lambda: chooseMove(4)) #             - 4

add_hotkey("5", lambda: healPokemon()) # HEAL POKEMON AT MITIS TOWN - 5

print("[SUCCESS]: Keybinds loaded! More features coming soon.")
print("[WORKING]: Loading Interface Modules...")

def addInput():
    city = None

    def saveCity():
        nonlocal city

        response = entry.get()

        if response == "" or response is None:
            city = None
        else:
            city = response

        app.destroy()

    app = Tk()
    app.title("Instant Traveling Box")
    app.geometry("250x100")
    app.resizable(False, False)

    frame = Frame(app)
    frame.pack(padx=10, pady=10, anchor="w")

    entry = Entry(frame, width=30)
    entry.grid(row=1, column=0, pady=5)

    OK = Button(frame, text="OK", command=saveCity)
    OK.grid(row=2, column=0, pady=(5, 0), sticky="w")

    app.mainloop()

    return city

add_hotkey("6", lambda: flyTo(addInput()))
# add_hotkey("7", lambda: hotspotTrain(True))
# add_hotkey("8", lambda: hotspotTrain(False))

print("[WAITING]: Waiting for next inputs...")

wait()