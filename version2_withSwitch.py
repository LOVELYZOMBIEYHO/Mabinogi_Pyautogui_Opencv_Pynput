# PyautoGUI
import pyautogui
from directkeys import PressKey, ReleaseKey, W, A, S, D, SHIFT, CTRL, ESC, C, LEFT, RIGHT, ALT, NUM4, NUM0
import time


import ctypes, sys
import random

# OpenCV
import cv2 as cv
import numpy as np
import os
# local files
from windowcapture import WindowCapture
from vision import Vision


# State change(pynput&threading)  - notice: pynput need to be installed locally, which means install the "pip3 install pynput" without virtual envirnoment (venv)
from threading import Thread
from pynput import keyboard

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    def exit_program():
        def on_press(key):
            if str(key) == 'Key.esc':
                main.status = 'pause'
                print(main.status)


            elif str(key) == 'Key.space':
                main.status = 'run'
            #  choose one, Key.space,esc,shift are the function of pynput.  or keyboard.read_key()== "p"   (a-z, prefer this one) 
            elif keyboard.read_key() == "p":
                main.status = 'exit'
                exit()

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()


    def main():
        main.status = 'run'
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        # Depence on your view name
        wincap = WindowCapture('新瑪奇 mabinogi')
        vision_limestone = Vision('images/mabinogi_gold.jpg')
        time.sleep(5)

        while True:
            print('running')
            # -----You can adjust the script here----------------
            time.sleep(1)
            PressKey(ALT)
            time.sleep(0.25)
            # get an updated image of the game
            screenshot = wincap.get_screenshot()

            # display the processed image
            points = vision_limestone.find(screenshot, 0.5, 'rectangles')
            
            # Switch to pause state when point is empty
            if points == []:
                main.status = 'pause'

            else:
                # Adjust the points
                x=points[0][0]
                y=points[0][1]+35

                
                
                time.sleep(0.01)
                pyautogui.moveTo(x, y) 
                time.sleep(0.15)
                pyautogui.click(button='left',x=x, y=y)
                time.sleep(0.15)
                pyautogui.mouseDown(button='left',x=random.randint(500, 2000),y=random.randint(500, 1000))
                time.sleep(0.15)
                pyautogui.mouseUp(button='left')

                time.sleep(0.01)
                ReleaseKey(ALT)


            # --------------------------------------------

            

            # Pasue state
            while main.status == 'pause':
                time.sleep(1)

            # Exit state
            if main.status == 'exit':
                print('Main program closing')
                break


    Thread(target=main).start()
    Thread(target=exit_program).start()



else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)