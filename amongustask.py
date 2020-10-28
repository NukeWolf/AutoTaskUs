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
def cardSwipe(screen,mouseData,pixelData):
    auin.click(mouseData['cardPos'])
    time.sleep(.5)
    auin.drag(mouseData['dragStart'],mouseData['dragEnd'],1.4)


time.sleep(3)
fin = "cardSwipe"
eval(fin+"(aucv.grabScreen(),testData[\""+fin+"\"]['mouseData'],[])")