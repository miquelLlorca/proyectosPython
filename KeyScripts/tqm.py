import pynput.keyboard as pyK
from time import sleep


keyboard = pyK.Controller()

sleep(5)

for i in range(1000):
    
    for key in "Te quiero <3":
        keyboard.press(key)
        keyboard.release(key)
    keyboard.press(pyK.Key.enter)
    keyboard.release(pyK.Key.enter)
    sleep(0.25)
    #break

#Te quiero <3

