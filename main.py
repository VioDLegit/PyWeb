# theese are the modules required to run this program you can use pip install requirements.txt to install them or py -m pip install requirements.txt (you need to be in the same directory as requirements.txt in command prompt)

import time
import win32gui
import requests

hook = '----'

messages = {
    "YouTube": {
        "username": "red box white triangle", # username
        "content": "you can always change this message for going to youtube.com", # the message which will be sent
        "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png", # avatar 
        "color": 0xFF0000 # embed color
    },
    "Roblox": {
        "username": "cubical lego game", # username
        "content": "this is the message for going on roblox.com! you can always change it to whatever you want!", # the  message which will be sent
        "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Roblox_logo_2017.png", # avatar 
        "color": 0x0000FF # embed color
    },
    "Discord": {
        "username": "dicksord", # username
        "content": "can always change this message for going to discord.com", # the message which will be sent 
        "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/6/69/Discord_logo_2015.png", # avatar 
        "color": 0xFFA500 # embed color
    }
}

recentkw = None

def wintitle():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow()) # returns the title of the window thats currently being used (focused) like roblox.com 

def send(keyword):
    data = messages[keyword]
    payload = {
        "username": data["username"], # getting username from data
        "avatar_url": data["avatar_url"], # getting avatar url from data 
        "embeds": [{
            "description": data["content"], # getting the message to send
            "color": data["color"] # getting  the embed color
        }]
    }
    requests.post(hook, json=payload)

while True: # creates a loop how it works: while true does something while something is equal to true but it will always be equal to true as there was no variable before it so if there was a varaible NotTrue = False and you did while NotTrue = True: it wouldnt work.
    activewindow = wintitle() # makes a variable active window and says its = to the function wintitle
    found = False # found is a variavle at false but sent to true later.
    for keyword in messages:
        if keyword.lower() in activewindow.lower():
            found = True
            if keyword != recentkw:
                send(keyword)
                recentkw = keyword
            break
    if not found:
        recentkw = None
    time.sleep(0.5) # how long in intervals inbetween sending the messages (to prevent spam and ratelimits)
