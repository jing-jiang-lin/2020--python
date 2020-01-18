# Add your Python code here. E.g.
from microbit import *


while True:
    if button_a.is_pressed():
        display.show('A')
        sleep(1000)
        
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll('AB')
        sleep(1000)
        
    if button_b.is_pressed():
        display.show('B')
        sleep(1000)