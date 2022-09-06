import http.client
import keyboard
import pyperclip
import pyautogui as pya
import time
from googletrans import Translator
from kivy.app import App
from kivy.uix.label import Label


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


def display(file_path):
    try:
        with open(f"{file_path}") as w:
            f = w.read()
        return str(f)
    except:
        return "Not found, Sorry, the user has no data entered yet."


def open_wnd():
    return Label(text=display('test.txt'), color="#DADADA")
def close_wnd():
    return quit(Label)


if have_internet():
    while True:
        try:
            if keyboard.is_pressed('ctrl'):
                if keyboard.is_pressed('c'):
                    translate()
        except:
            pass