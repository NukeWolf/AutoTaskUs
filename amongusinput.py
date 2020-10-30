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
    time.sleep(1)

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

def dragAndHold(start,end,dragDuration,holdDuration):
    pyautogui.mouseDown(x=start[0],y=start[1])
    pyautogui.moveTo(end[0],end[1],dragDuration)
    time.sleep(holdDuration)
    pyautogui.mouseUp()

def hold(loc,secs):
    pyautogui.mouseDown(x=loc[0],y=loc[1])
    time.sleep(secs)
    pyautogui.mouseUp()

def mapToggle():
    pyautogui.press("tab")
def doTask():
    pyautogui.press("e")