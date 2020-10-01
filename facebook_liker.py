#importing the modules
import pyautogui
import time
import sys

#Giving the user certain time to open the wesite
print("Open the facebook timeline")
time.sleep(5)
print("Starting the bot..")
time.sleep(2)
print("Bot activated..")

def main_code():
    while True:
        try:
            #This will auto select a post
            pyautogui.press('j',interval=3)
            
            #All the emojis will pop up
            pyautogui.press('l',interval=1)
            time.sleep(1)

            #This will press the like button
            pyautogui.press('enter')
            time.sleep(5)
            print('''(Ctrl + C) to exit the program''')
        except:
            KeyboardInterrupt
            sys.exit()
            

main_code()   

    
   
    
    

