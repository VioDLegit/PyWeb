import time
import win32gui
import requests

hook = '----'

messages = {
    "YouTube": {
        "username": "red box white triangle",
        "content": "you can always change this message for going to youtube.com",
        "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png",
        "color": 0xFF0000
    },
    "Roblox": {
        "username": "cubical lego game",
        "content": "this is the message for going on roblox.com! you can always change it to whatever you want!",
        "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Roblox_logo_2017.png",
        "color": 0x0000FF
    },
    "Discord": {
        "username": "dicksord",
        "content": "can always change this message for going to discord.com",
        "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/6/69/Discord_logo_2015.png",
        "color": 0xFFA500
    }
}

recentkw = None

def wintitle():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def send(keyword):
    data = messages[keyword]
    payload = {
        "username": data["username"],
        "avatar_url": data["avatar_url"],
        "embeds": [{
            "description": data["content"],
            "color": data["color"]
        }]
    }
    requests.post(hook, json=payload)

while True:
    activewindow = wintitle()
    found = False
    for keyword in messages:
        if keyword.lower() in activewindow.lower():
            found = True
            if keyword != recentkw:
                send(keyword)
                recentkw = keyword
            break
    if not found:
        recentkw = None
    time.sleep(0.5)
