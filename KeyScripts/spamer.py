import pynput.keyboard as pyK
from time import sleep


keyboard = pyK.Controller()

sleep(5)

for i in range(999):
    
    for key in "Puto crack":
        keyboard.press(key)
        keyboard.release(key)
    keyboard.press(pyK.Key.enter)
    keyboard.release(pyK.Key.enter)
    sleep(0.1)
    #break