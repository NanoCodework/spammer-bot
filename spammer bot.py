import time
import pyautogui
import webbrowser
webbrowser.open("www.discord.com") #this website is only for an example other wesite url can be used
time.sleep(25)
for i in range(10):
#other text can be used for example "hi" , "hey" etc.
    pyautogui.press("h")
    pyautogui.press("i")
    pyautogui.press("enter")
