import math
import amongusinput as auin
import amonguscv2 as aucv
import yaml
import time
f = open("ref/tasks_1080p.yaml")
DATA = yaml.load(f, Loader=yaml.FullLoader)
CONFIG = DATA['maps']['Skeld']['tasks']
f.close()

def getTask(loc):
    for x in CONFIG:
        for taskLoc in CONFIG[x]['locations']:
            if (loc[0]-6 <= taskLoc[0] <= loc[0]+6 and loc[1]-6 <= taskLoc[1] <= loc[1]+6):
                return CONFIG[x]
    return None

def getSamplesLoc():
    return CONFIG['medBaySamples']['locations'][0]

def closeTask():
    auin.click(DATA['misc']['exitButton'])

def taskCheck(screen,pixelData):
    if(aucv.checkPixel(screen,pixelData["taskCheck"]["pos"],pixelData["taskCheck"]["color"])):
        return True
    else:
        closeTask()
        return False 



#For each wire in the left, it will compare colors to wires on the right and drag accordingly.
def wiring(screen,mouseData,pixelData):
    if(not taskCheck(screen,pixelData)):
        return
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
    auin.drag(mouseData['dragStart'],mouseData['dragEnd'],1.5)

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
    if(not taskCheck(screen,pixelData)):
        return
    auin.click(mouseData)
    time.sleep(pixelData['sleepDuration'])

#Drags and keeps the mouse down
def emptyGarbage(screen,mouseData,pixelData):
    if(not taskCheck(screen,pixelData)):
        return
    auin.dragAndHold(mouseData['start'],mouseData['end'],.5,mouseData['holdDuration'])

#Checks a horizontal line of pixels for the lit up slider, then drags it up.
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

#For each calibrate, it checks for a pixel in the bar, and clicks when lit up.
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
    if(not taskCheck(screen,pixelData)):
        return
    time.sleep(12)

def navigationChart(screen,mouseData,pixelData):
    screen = aucv.grabScreen()
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
    auin.drag(mouseData,mouseData,.3)
    time.sleep(2)

#Clear Filter needs a REDO Too Slow
def clearFilter(screen,mouseData,pixelData):
    if(not taskCheck(screen,pixelData)):
        return
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
                    
def reactorManifolds(screen,mouseData,pixelData):
    directory = "ref/"
    for x in range(1,11):
        file = directory+str(x)+".png"
        loc = aucv.findImage(screen,file,.8)
        if(len(loc)>=1):
            auin.click(loc[0])
        else:
            screen = aucv.grabScreen()

def startReactor(screen,mouseData,pixelData): 
    keypad = []
    tiles = []
    step = mouseData['step']
    for y in range(3):
        for x in range(3):
            keypad.append([mouseData['first'][0] + step*x,mouseData['first'][1] + step*y])
            tiles.append([pixelData['firstTile'][0] + step*x,pixelData['firstTile'][1] + step*y])
    for attempt in range(5):
        password = []
        counter = 0
        while (counter<=attempt):
            screen = aucv.grabScreen()
            for ind in range(len(tiles)):
                if(aucv.checkPixel(screen,tiles[ind],pixelData['color'])):
                    password.append(keypad[ind])
                    counter+=1
                    time.sleep(pixelData['tileCooldown'])
                    break
        time.sleep(.05)
        for loc in password:
            auin.click(loc)

def primeShields(screen,mouseData,pixelData):
    lower = pixelData['lowerColor']
    upper = pixelData['upperColor']
    for loc in mouseData:
        if(aucv.checkPixelRange(screen,loc,upper,lower)):
            auin.click(loc)
            time.sleep(pixelData['coolDown'])

def fuelEngines(screen,mouseData,pixelData):
    auin.hold(mouseData['pos'],mouseData['holdDuration'])

def medBaySamples(screen,mouseData,pixelData):
    time.sleep(.5) #Make sure the button is the right color
    screen = aucv.grabScreen()     
    posButton = pixelData['startButton']['pos']
    if(aucv.checkPixel(screen,posButton,pixelData['startButton']['color'])):
        vialStartX = pixelData['firstvial'][0]
        vialStartY = pixelData['firstvial'][1]
        step = mouseData['stepx']
        compare = pixelData['redVialColor']
        for x in range(5):
            if(aucv.checkPixel(screen,[vialStartX+step*x,vialStartY],compare)):
                buttonX = mouseData["firstButton"][0]
                buttonY = mouseData["firstButton"][1]
                auin.click([buttonX+step*x,buttonY])
    else:
        auin.click(posButton)
        closeTask()




time.sleep(1)
fin = "wiring"
eval(fin+"(aucv.grabScreen(),CONFIG[\""+fin+"\"]['mouseData'],CONFIG[\""+fin+"\"]['pixelData'])")