## Facebook Auto Like Bot

This is a small program that will like your facebook posts automatically by selecting them. It is also smart enough to skip those posts which are already liked.

## Installation

We need to install the pyautogui module in oder to build the program.

```bash
pip install pyautogui
```

## Usage

```python
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT License

Copyright (c) 2020 Swastik Sarkar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWAR
