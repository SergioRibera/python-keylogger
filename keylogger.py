import keyboard, sys, json
from pathlib import Path

dataFile = str(Path().absolute()) + '/data'

def OnKeyboardKeyDown(e):
    print(e.name)

keyboard.on_press(OnKeyboardKeyDown)
input("On Key Down Functionando")