# * This file shouldn't be modified ! * #
# * Generated to simulate proper mouse controls! * #

# * LAST UPDATED : March 10th, 2025 * #

# * ------------------------------------- * #

import ctypes
import time

MOUSEEVENTFMOVE = 0x0001
MOUSEEVENTFABSOLUTE = 0x8000
MOUSEEVENTFLEFTDOWN = 0x0002
MOUSEEVENTFLEFTUP = 0x0004
INPUTMOUSE = 0

SCREENWIDTH = ctypes.windll.user32.GetSystemMetrics(0)
SCREENHEIGHT = ctypes.windll.user32.GetSystemMetrics(1)

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong)),
    ]

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("mi", MOUSEINPUT)]
    _anonymous_ = ("_input",)
    _fields_ = [("type", ctypes.c_ulong), ("_input", _INPUT)]

def SIMULATEMOUSEMOVE(X, Y, DURATION=0):
    STARTY = Y - 10
    ABSX = int((X / SCREENWIDTH) * 65535)
    ABSY = int((STARTY / SCREENHEIGHT) * 65535)
    TARGETABSY = int((Y / SCREENHEIGHT) * 65535)
    STEPS = 1

    for I in range(STEPS + 1):
        INTERMEDIATEX = ABSX
        INTERMEDIATEY = ABSY + int((TARGETABSY - ABSY) * I / STEPS)
        MI = MOUSEINPUT(dx=INTERMEDIATEX, dy=INTERMEDIATEY, mouseData=0, dwFlags=MOUSEEVENTFMOVE | MOUSEEVENTFABSOLUTE, time=0, dwExtraInfo=None)
        INPUTEVENT = INPUT(type=INPUTMOUSE, _input=INPUT._INPUT(mi=MI))
        
        ctypes.windll.user32.SendInput(1, ctypes.byref(INPUTEVENT), ctypes.sizeof(INPUTEVENT))
        time.sleep(DURATION / STEPS)

def CLICKAT(X, Y):
    SIMULATEMOUSEMOVE(X, Y, DURATION=0)
    time.sleep(0.05)
    
    MI = MOUSEINPUT(dx=0, dy=0, mouseData=0, dwFlags=MOUSEEVENTFLEFTDOWN, time=0, dwExtraInfo=None)
    INPUTEVENT = INPUT(type=INPUTMOUSE, _input=INPUT._INPUT(mi=MI))
    ctypes.windll.user32.SendInput(1, ctypes.byref(INPUTEVENT), ctypes.sizeof(INPUTEVENT))
    
    time.sleep(0.05)

    MI = MOUSEINPUT(dx=0, dy=0, mouseData=0, dwFlags=MOUSEEVENTFLEFTUP, time=0, dwExtraInfo=None)
    INPUTEVENT = INPUT(type=INPUTMOUSE, _input=INPUT._INPUT(mi=MI))
    ctypes.windll.user32.SendInput(1, ctypes.byref(INPUTEVENT), ctypes.sizeof(INPUTEVENT))

# * ------------------------------------- * #
