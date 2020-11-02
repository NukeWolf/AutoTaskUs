import bot
from threading import Thread

def startBot():
    bot.start()



def main(): 
    thread0 = Thread(target=startBot)
    thread0.daemon = True  
    thread0.start()
    print("OY")


main()
