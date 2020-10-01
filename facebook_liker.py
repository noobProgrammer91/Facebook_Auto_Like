
#importing the modules
import pyautogui
import time


#Giving the user certain time to open the wesite
time.sleep(5)

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
        except:
            KeyboardInterrupt
            input("Press CTRl+C to exit")

main_code()    

    
   
    
    

