# This code is for automated text messaging

# Import the relevant modules
import time
import pyautogui

def SendMessage():
    time.sleep(7)
    text = open('message.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')                                # Writes each line and presses enter

SendMessage()