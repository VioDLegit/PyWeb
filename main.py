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

last_keyword = None

def get_active_window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def send_message(keyword):
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
    active_window = get_active_window_title()
    found = False
    for keyword in messages:
        if keyword.lower() in active_window.lower():
            found = True
            if keyword != last_keyword:
                send_message(keyword)
                last_keyword = keyword
            break
    if not found:
        last_keyword = None
    time.sleep(0.5)
