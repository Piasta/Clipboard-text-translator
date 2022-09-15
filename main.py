# import http.client
import keyboard
import pyperclip
import pyautogui as pya
import time
from googletrans import Translator


def have_internet():
    conn = http.client.HTTPSConnection('8.8.8.8', timeout=1)
    try:
        conn.request("HEAD", "/")
        return True
    except Exception:
        return False
    finally:
        conn.close


def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)
    return pyperclip.paste()


def translate():
    translator = Translator()
    var = copy_clipboard()
    strVar = str(var)
    file = open('test.txt', "w")
    file.write("EN: " + strVar + "\n")

    transVar = translator.translate(strVar, dest='pl')
    strTransVar = transVar.text
    
    file.write("\n" + "PL: " + strTransVar)


# if have_internet():
while True:
    try:
        if keyboard.is_pressed('ctrl'):
            if keyboard.is_pressed('c'):
                translate()
    except:
        pass



