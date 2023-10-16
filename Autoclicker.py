import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener , KeyCode

toggleKey = KeyCode(char="t")

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.01) # every 200ms

def toggleState(key):
    if key == toggleKey:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target = clicker)
click_thread.start()

with Listener(on_press=toggleState) as listener:
    listener.join()


    



