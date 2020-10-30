import cv2
import time
import amonguscv2 as aucv
import amongusinput as auin
import amongustask as autask
import amongusmap as aumap
import math
import win32api
import pyautogui
import threading
import numpy as np

def debug():
    last_time = time.time()
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    while(True):

        #print(f'Frame took {time.time()-last_time} seconds')
        #last_time = time.time()

        
        screen = aucv.grabScreen()

        mouse = win32api.GetKeyState(0x01)

        if mouse <= -127:
            try:
                pos = pyautogui.position()
                print(pyautogui.position())
                print(screen[pos[1],pos[0]])
            except:
                pass

        player = aucv.findImage(screen,"ref/player-template.png",.87)
        tasks = aucv.findImage(screen,"ref/task-template.png",.9)

        if (len(player)>=1):
            closeTask = aumap.findClosestTask(player,tasks)
            if(len(closeTask) > 0):
                print(tasks)
                print("Player",player)
                print(closeTask)
                auin.goto(player,closeTask)
                input()





        cv2.imshow('window', screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
debug()