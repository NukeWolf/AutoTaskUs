import cv2
import time
import amonguscv2 as aucv
import amongusinput as auin
import amongustask as autask
import math
import win32api
import pyautogui
import threading
import numpy as np

def main(): 
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

        # whitelo=np.array([100,100,100])
        # whitehi=np.array([255,255,255])
        # mask=cv2.inRange(screen,whitelo,whitehi)
        # screen[mask>0]=(219,153,54)             
        # gray = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
        # edges = cv2.Canny(gray, 75, 150)
        # lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=15,minLineLength=130)
        # for line in lines:
        #     x1, y1, x2, y2 = line[0]
        #     cv2.line(screen, (x1, y1), (x2, y2), (0, 0, 128), 1)

        template = cv2.imread('ref/task-template.png')
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        threshold = .9
        loc = np.where(res >= threshold)
        w, h = template.shape[:-1]
        for pt in zip(*loc[::-1]):  # Switch collumns and rows
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)


        player = aucv.findPlayer(screen)
        tasks = aucv.findTasks(screen)

        # if (len(player)>=1):
        #     closeTask = autask.findClosestTask(player,tasks)
        #     if(len(closeTask) > 0):
        #         print(closeTask)
        #         auin.goto(player,closeTask)





        cv2.imshow('window', screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break





main()
