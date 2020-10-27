import pyautogui
from PIL import Image
pyautogui.PAUSE = .30

startX = 125
startY = 505
people = 4
skip = 3
muteX = 285
muteY = 785
clickOffx = 200
clickOffy = 75
#285,845

def checkPos():
    while True:
        print(pyautogui.position())
checkPos()

def checkDef(muteX = 285,muteY = 785):
    im = Image.open("nice.png")
    px = im.load()
    pixel = px[muteX,muteY][0]
    return not (pixel == 24)
    

for index in range(people):
        pyautogui.click(startX,startY+(index*33),button='right')
        if index != skip:
            pyautogui.click(muteX, muteY)
        else:
            pyautogui.click(startX,startY+(index*33),button='right')
            pyautogui.click(startX+160,startY+(index*33)+241)
        pyautogui.click(clickOffx,clickOffy)
input()       
for index in range(people):
    if index != skip:
        pyautogui.click(startX,startY+(index*33),button='right')
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'nice.png')
        if checkDef():
            pyautogui.click(muteX, muteY)
        pyautogui.click(clickOffx,clickOffy)
        
        #checkPos()

#for index in range(100):
#    width, height = pyautogui.size()
#    pyautogui.click(1316, 989,)
#    pyautogui.PAUSE = .5
#    pyautogui.typewrite(str(index+1))
#    pyautogui.PAUSE = .5
#    pyautogui.press('down')
#    pyautogui.press('enter')
#    pyautogui.click(1638, 620)
#    pyautogui.PAUSE = .70