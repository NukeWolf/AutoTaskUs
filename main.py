import numpy as np
from PIL import ImageGrab
import cv2
import time
import amonguscv2 as aucv
import math
import pyautogui

pyautogui.PAUSE = .03


def main(): 
    last_time = time.time()
    while(True):
        print(f'Frame took {time.time()-last_time} seconds')
        last_time = time.time()
        screen = aucv.grabScreen()
        player = aucv.findPlayer(screen)
        tasks = aucv.findTasks(screen)
        if (len(player)>=1):
            closeTask = findClosestTask(player,tasks)
            if(len(closeTask) > 0):
                goto(player,closeTask)

        #contours = aucv.findContours(screen)
        #aucv.drawContours(contours,screen)
        
        

        cv2.imshow('window', screen)
       # cv2.imshow('original',original)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def findClosestTask(loc,tasks):
    print(loc,tasks)
    loc = loc[0]
    minDist = 9999
    minVal = []
    for x,y in tasks:
        dist = math.sqrt((y-loc[1]) ** 2 + (x-loc[0])**2)
        if(dist<minDist):
            minDist = dist
            minVal = (x,y)
    return minVal

def goto(loc,taskLoc):
    loc = loc[0]
    xDist = taskLoc[0] - loc[0] 
    yDist = taskLoc[1] - loc[1]
    time.sleep(3)

    if abs(xDist) < abs(yDist):
        diagdist = math.sqrt(2 * (xDist ** 2))
        secs = diagdist/125
        travel(xDist,yDist,secs)
        lastdist = abs(yDist)-abs(xDist)
        secs = lastdist/125
        travel(0,yDist,secs)
    else:
        diagdist = math.sqrt(2 * (yDist ** 2))
        secs = diagdist/125
        travel(xDist,yDist,secs)
        lastdist = abs(xDist)-abs(yDist)
        secs = lastdist/125
        travel(xDist,0,secs)
    input()
        
def travel(x,y,secs):
    if(x > 0):
        pyautogui.keyDown("d")
    if(x < 0):
        pyautogui.keyDown("a")
    if(y > 0):
        pyautogui.keyDown("s")
    if(y < 0):
        pyautogui.keyDown("w")
    time.sleep(secs)
    pyautogui.keyUp("w")
    pyautogui.keyUp("a")
    pyautogui.keyUp("s")
    pyautogui.keyUp("d")

main()
