import pyautogui
import time
pyautogui.PAUSE = .03
pyautogui.FAILSAFE = True
# time.sleep(3)
# print('down')
# pyautogui.keyDown("d")
# time.sleep(1.95)
# print("up")

pyautogui.keyUp("d")    

def checkPos():
    while True:
        print(pyautogui.position())

#checkPos()
def cardSwipe():
    pyautogui.click(850,820)
    x = 450
    y = 400
    time.sleep(.5)
    pyautogui.moveTo(x, y, duration=0)
    pyautogui.dragRel(1000, 0, duration=1.4)
def asteroids():
    for x in range(1000):
        for y in range(140,941,100):
            pyautogui.click(1000,y)
            #time.sleep(.1)
asteroids()


#140 to 940
#x is 1000

