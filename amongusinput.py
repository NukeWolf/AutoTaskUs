import math
import time
import pyautogui
#pixels per second
SPEED = 125
pyautogui.PAUSE = .03

#Given a starting point and a destination, it will input the commands to travel to go from one point to another.
def goto(loc,taskLoc):
    loc = loc[0]
    xDist = taskLoc[0] - loc[0] 
    yDist = taskLoc[1] - loc[1]
    time.sleep(3)

    if abs(xDist) < abs(yDist):
        diagdist = math.sqrt(2 * (xDist ** 2))

        secs = diagdist/SPEED
        travel(xDist,yDist,secs)
        lastdist = abs(yDist)-abs(xDist)
        secs = lastdist/SPEED
        travel(0,yDist,secs)
    else:
        diagdist = math.sqrt(2 * (yDist ** 2))
        secs = diagdist/SPEED
        travel(xDist,yDist,secs)
        lastdist = abs(xDist)-abs(yDist)
        secs = lastdist/SPEED
        travel(xDist,0,secs)
    input()


#Given 2 directions, and time, it will press down the neccessary keys for the specified amount of time.
def travel(x,y,secs):
    pyautogui.PAUSE = .03
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


def drag(start,end,secs):
    pyautogui.moveTo(start[0],start[1],duration=0)
    pyautogui.dragTo(end[0], end[1], duration=secs)

def click(loc):
    pyautogui.click(loc[0],loc[1])    