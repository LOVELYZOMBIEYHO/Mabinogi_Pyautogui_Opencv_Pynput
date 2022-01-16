# Mabinogi get gold on the floor

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

# Mabinogi is made by DirectX, directkey and run the script by admin right is must. 
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    #  input the key and change to Mabinogi for starting the script manually
    a = input("input '1' to start:")
    if a == "1":
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        # Depence on your view name
        wincap = WindowCapture('新瑪奇 mabinogi')
        vision_limestone = Vision('images/mabinogi_gold.jpg')

        # loop_time = time()
        time.sleep(5)


        counter = 0

        while counter < 1:

            PressKey(ALT)
            time.sleep(0.25)
            # get an updated image of the game
            screenshot = wincap.get_screenshot()

            # display the processed image
            points = vision_limestone.find(screenshot, 0.5, 'rectangles')
            print(points)
            
            x=points[0][0]
            y=points[0][1]+35


            
            time.sleep(0.1)
            pyautogui.moveTo(x, y) 
            time.sleep(0.25)
            pyautogui.click(button='left',x=x, y=y)
            time.sleep(1)
            pyautogui.mouseDown(button='left',x=random.randint(500, 2000),y=random.randint(500, 1000))
            time.sleep(0.5)
            pyautogui.mouseUp(button='left')

            time.sleep(1)
            ReleaseKey(ALT)

            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break

            


            
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)



