import math
import amongusinput as auin
import amonguscv2 as aucv
import yaml
import time
f = open("ref/tasks_1080p.yaml")
data = yaml.load(f, Loader=yaml.FullLoader)
testData = data['maps']['Skeld']['tasks']


def findClosestTask(loc,tasks):
    loc = loc[0]
    minDist = 9999
    minVal = []
    for x,y in tasks:
        dist = math.sqrt((y-loc[1]) ** 2 + (x-loc[0])**2)
        if(dist<minDist):
            minDist = dist
            minVal = (x,y)
    return minVal

#For each wire in the left, it will compare colors to wires on the right and drag accordingly.
def wiring(screen,mouseData,pixelData):
    for x in range(1,5): 
        check1 = mouseData['inwire'+str(x)]
        color1 = screen[check1[1],check1[0]]
        for y in range(1,5):
            check2 = mouseData['outwire'+str(y)]
            if(aucv.checkPixel(screen,check2,color1)):
                auin.drag(check1,check2,.5)

#Clicks on the card position and then drags the card from a specified start position to an end position.
def cardSwipe(screen,mouseData,pixelData):
    auin.click(mouseData['cardPos'])
    time.sleep(.5)
    auin.drag(mouseData['dragStart'],mouseData['dragEnd'],1.4)

#Spam clicks in a line in order to destroy asteroids. Exits the loop once the "Destroyed" text goes away by 
# checking a white pixel.
def asteroids(screen,mouseData,pixelData):
    x = mouseData["screensize"]/2
    startY = mouseData["startY"]
    endY = mouseData["endY"]
    step = mouseData["step"]
    while True:
        for y in range(startY,endY,step):
            auin.click([x,y])
        newscreen = aucv.grabScreen()
        pos = pixelData['whiteText']['pos']
        color = pixelData['whiteText']['color']
        if(not aucv.checkPixel(newscreen,pos,color)):
            break

#Clicks a download button and then sleeps.
def download(screen,mouseData,pixelData):
    auin.click(mouseData)
    time.sleep(12)
    print("Done")
def emptyGarbage(screen,mouseData,pixelData):
    auin.dragAndHold(mouseData['start'],mouseData['end'],.5,mouseData['holdDuration'])

def divertPower(screen,mouseData,pixelData):
    startx = mouseData['start'][0]
    starty = mouseData['start'][1]
    ydist = mouseData['dragDist']
    for x in range(startx,mouseData['endx']):
        if(aucv.checkPixel(screen,[x,starty],pixelData)):
            auin.drag([x+5,starty],[x+5,starty-ydist],.3)
            break

def divertAccept(screen,mouseData,pixelData):
    auin.click(mouseData)
    time.sleep(2)

def calibrateDistributor(screen,mouseData,pixelData):
    for x in range(1,4):
        while True:
            newscreen = aucv.grabScreen()
            color = pixelData["check"+str(x)]['color']
            pos = pixelData["check"+str(x)]['pos']
            if(aucv.checkPixel(newscreen,pos,color)):
                auin.click(mouseData[x-1])
                break

def alignEngine(screen,mouseData,pixelData):
    startx = mouseData['start'][0]
    starty = mouseData['start'][1]
    destY = mouseData['destinationY']
    for y in range(starty,mouseData['endy']):
        if(aucv.checkPixel(screen,[startx,y],pixelData)):
            auin.drag([startx,y],[startx,destY],.7)
            break
def medBayScan(screen,mouseData,pixelData):
    time.sleep(12)

def navigationChart(screen,mouseData,pixelData):
    starty = pixelData['starty']
    endy = pixelData['endy']
    lower = pixelData['lowerColor']
    upper = pixelData['upperColor']
    lastPos = []
    for x in range(1,6):
        x = mouseData["checkx"+str(x)]
        for y in range(starty,endy):
            if(aucv.checkPixelRange(screen,[x,y],upper,lower)):
                if len(lastPos) == 0:
                    lastPos= [x,y]
                else:
                    slope = (y-lastPos[1])/(x-lastPos[0])
                    extraY = slope*40
                    auin.drag(lastPos,[x+40,y+extraY],.5)
                    lastPos= [x,y]
                break

def navigationSteering(screen,mouseData,pixelData):
    auin.click(mouseData)
    auin.click(mouseData)
    time.sleep(2)

def clearFilter(screen,mouseData,pixelData):
    lower = pixelData['lowerColor']
    upper = pixelData['upperColor']
    leave = True
    while(leave):
        leave = False
        screen = aucv.grabScreen()
        for x in range(pixelData['topLeft'][0],pixelData['botRight'][0]):
            for y in range(pixelData['topLeft'][1],pixelData['botRight'][1]):
                if(aucv.checkPixelRange(screen,[x,y],upper,lower)):
                    auin.drag([x,y],mouseData,.3)
                    time.sleep(.4)
                    leave = True
                    screen = aucv.grabScreen()
                    


       
                 


time.sleep(3)
fin = "clearFilter"
eval(fin+"(aucv.grabScreen(),testData[\""+fin+"\"]['mouseData'],testData[\""+fin+"\"]['pixelData'])")