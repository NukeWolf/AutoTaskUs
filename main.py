import numpy as np
from PIL import ImageGrab
import cv2
import time


#Grabs a screenshot and converts the format to RGB
def grabScreen():
    printscreen =  np.array(ImageGrab.grab(bbox=(0,0,1920,1080)))
    printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
    return printscreen

#Finds a color on the map and then proceeds to find that color, and create a contour of it.
def findContours(img):
    lower = np.array([20, 34, 92], dtype="uint8")
    upper = np.array([30, 73, 113], dtype="uint8")
    mask = cv2.inRange(img, lower, upper)
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    return cnts

#Given a list of contours, will draw rectangles on the image.
def drawContours(cnts,img):
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if(w>=5 and h>=5):
            cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)


#Built for 1080p screen sizes, finds the task. If on a different resolution, mess with the threshold, and you may need a different screenshot.
def findTasks(screen):
    template = cv2.imread('ref/task-template.png')
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    threshold = .95
    loc = np.where(res >= threshold)

    w, h = template.shape[:-1]
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    return [pt for pt in zip(*loc[::-1])]
        

def screen_record(): 
    last_time = time.time()
    while(True):
        #output = cv2.bitwise_and(printscreen, printscreen, mask = mask)
        #print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()


        screen = grabScreen()        
        contours = findContours(screen)
        drawContours(contours,screen)
        print(findTasks(screen))


        cv2.imshow('window', screen)
       # cv2.imshow('original',original)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
