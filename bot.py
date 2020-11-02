import cv2
import time
import amonguscv2 as aucv
import amongusinput as auin
import amongustask as autask
import amongusmap as aumap

def run():
    global medBayLastDone
    #Turns map on and finds screen
    screen = aucv.grabScreen()
    if(not aumap.checkMapOn(screen)):
        auin.mapToggle()
        time.sleep(.1)
        screen = aucv.grabScreen()
    #Gets Player location. If it can't see the player, adjust and try again.   
    player = aucv.findImage(screen,"ref/player-template.png",.87)
    while (len(player) == 0):
        auin.travel(0,-1,.2)
        if(not aumap.checkMapOn(screen)):
            auin.mapToggle()
            time.sleep(.1)
        screen = aucv.grabScreen()
        player = aucv.findImage(screen,"ref/player-template.png",.87)
    
    #Getting Tasks. Secondary Tasks will flash, so we need to take multiple screenshots for a higher chance to get the proper frame.
    tasks = aucv.findImage(screen,"ref/task-template.png",.9)
    for x in range(2):
        screen = aucv.grabScreen()
        moreTasks = aucv.findImage(screen,"ref/task-template.png",.9)
        tasks.extend(x for x in moreTasks if x not in tasks)
    #MedbaySamples Exception; Removes all medbaySample Locations if it was last done 60 seconds ago.
    if(time.time()-medBayLastDone < 60):
        samples = autask.getSamplesLoc()
        tasks = [x for x in moreTasks if not(samples[0]-6 <= x[0] <= samples[0]+6 and samples[1]-6 <= x[1] <= samples[1]+6)]
    #If there are any Tasks, find the closest one, goto it, and then perform it.
    if(len(tasks) > 0):
        closeTask = aumap.findClosestTask(player,tasks)
        auin.goto(player,closeTask)
        task = autask.getTask(closeTask)
        if task == None:
            print("Can't Find Task")
        else:
            #Exception for Medbay Samples
            if(task['funcCall'] == "medBaySamples"):
                medBayLastDone = time.time()
            
            functionCall = getattr(autask,task['funcCall'])
            if(aumap.checkMapOn(screen)):
                auin.mapToggle()
            time.sleep(.05)
            screen = aucv.grabScreen()
            if(aumap.checkUse(screen)):
                print(f"Doing Task {task['funcCall']}")
                auin.doTask()
                time.sleep(.4)
                screen = aucv.grabScreen()
                functionCall(screen,task['mouseData'],task['pixelData'])
                time.sleep(.3)
            else:
                print("Use not Found")


def speedCalibrate():
    screen = aucv.grabScreen()
    if(not aumap.checkMapOn(screen)):
        auin.mapToggle()
        time.sleep(.1)
        screen = aucv.grabScreen()
    
    mapCheck = True
    while(mapCheck):
        player = aucv.findImage(screen,"ref/player-template.png",.87)
        while (len(player) == 0):
            auin.travel(0,1,.2)
            if(not aumap.checkMapOn(screen)):
                auin.mapToggle()
                time.sleep(.1)
            screen = aucv.grabScreen()
            player = aucv.findImage(screen,"ref/player-template.png",.87)

        lastY = player[0][1]
        auin.travel(0,1,1)
        screen = aucv.grabScreen()
        player = aucv.findImage(screen,"ref/player-template.png",.87)
        if(len(player)>=1): 
            auin.SPEED = abs(lastY-player[0][1]) 
            mapCheck=False
            print(auin.SPEED)
def start():
    time.sleep(2)
    global medBayLastDone
    medBayLastDone = 0
    speedCalibrate()
    while True:
        try:
            run()
        except Exception as e:
            print("Unexpected error:",e)
            raise

if __name__ == "__main__":
    start()
