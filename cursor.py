import pynput
from pynput import keyboard

string_to_type = "Hello! How are you?"

c = keyboard.Controller()
for char in string_to_type:
    c.tap(char)