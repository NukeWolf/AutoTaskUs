import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32gui

DEBUG = True

#Grabs a screenshot and converts the format to RGB
def grabScreen():
    # hwnd = win32gui.FindWindow(None, r'Among Us')
    # win32gui.SetForegroundWindow(hwnd)
    # dimensions = win32gui.GetWindowRect(hwnd)
    # print(dimensions)
    # image = np.array(ImageGrab.grab(dimensions))
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    printscreen =  np.array(ImageGrab.grab(bbox=(0,0,1920,1080)))
    printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
    return printscreen


#Given a screen,file,and threshold, will return a list of locations that the image is found
def findImage(screen,file,threshold):
    template = cv2.imread(file)
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    if (DEBUG):
        w, h = template.shape[:-1]
        for pt in zip(*loc[::-1]):  # Switch collumns and rows
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 200, 255), 2)
    return [pt for pt in zip(*loc[::-1])]            

def checkPixel(screen,px,color):
    compare_color = screen[px[1],px[0]]
    #print(color,compare_color)
    return np.array_equal(compare_color,color)

def checkPixelRange(screen,px,upper,lower):
    compare_color = screen[px[1],px[0]]
    table = [lower[x]<=compare_color[x]<=upper[x] for x in range(3)]
    return np.all(table)











#Depricated method of finding the character by finding their color and creating a contour based off a filtered color mask.

# #Finds a color on the map and then proceeds to find that color, and create a contour of it.
# def findContours(img):
#     lower = np.array([20, 34, 92], dtype="uint8")
#     upper = np.array([30, 73, 113], dtype="uint8")
#     mask = cv2.inRange(img, lower, upper)
#     cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = cnts[0] if len(cnts) == 2 else cnts[1]
#     return cnts

# #Given a list of contours, will draw rectangles on the image.
# def drawContours(cnts,img):
#     for c in cnts:
#         x,y,w,h = cv2.boundingRect(c)
#         if(w>=5 and h>=5):
#             cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)
# def findTasks(screen):
#     template = cv2.imread('ref/task-template.png')
#     res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
#     threshold = .9
#     loc = np.where(res >= threshold)
#     if (DEBUG):
#         w, h = template.shape[:-1]
#         for pt in zip(*loc[::-1]):  # Switch collumns and rows
#             cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
#     return [pt for pt in zip(*loc[::-1])]


