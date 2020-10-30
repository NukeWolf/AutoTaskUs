import math
import yaml
import amonguscv2 as aucv

f = open("ref/tasks_1080p.yaml")
data = yaml.load(f, Loader=yaml.FullLoader)
config = data['misc']
f.close()

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

def checkMapOn(screen):
    mapCheck = config['checkMap']
    return (aucv.checkPixel(screen,mapCheck['pos'],mapCheck['color']))
def checkUse(screen):
    useCheck = config['useButton']
    return (aucv.checkPixel(screen,useCheck['pos'],useCheck['color']))