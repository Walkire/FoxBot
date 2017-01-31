#utils.py
import socket, json
from data import addPoints
import urllib.request
from init import saveData
import cfg
import time, _thread

def openSocket():
    s = socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send(("PASS " + cfg.PASS + "\r\n").encode('utf-8'))
    s.send(("NICK " + cfg.NICK + "\r\n").encode('utf-8'))
    s.send(("JOIN #" + cfg.CHAN + "\r\n").encode('utf-8'))
    #s.send(("CAP REQ :twitch.tv/tags\r\n").encode('utf-8'))
    return s

def sendMessage(s, message):
        messageTemp = "PRIVMSG #" + cfg.CHAN + " :" + message
        s.send((messageTemp + "\r\n").encode('utf-8'))
        try:
                print("Sent: " + messageTemp)
        except UnicodeEncodeError:
                print("Unicode message sent")

def Pong(s):
        s.send(("PONG :tmi.twitch.tv\r\n").encode("utf-8"))
        #print("Sent PONG")

def timeout(s, user, secs):
    """
    Time out a user for a set period of time.
    Keyword arguments:
    s -- the socket over which to send the timeout command
    user -- the user to be timed out
    secs -- the length of the timeout in seconds (default 600)
    """
    secs = str(secs)
    sendMessage(s,".timeout "+user+" "+secs)
    print(user +" has been timed out for "+secs+" seconds")
    
def whisper(s, user, message):
    """
    whispers a user.
    Keyword arguments:
    s -- the socket over which to send the timeout command
    user -- the user to be whispered to
    message -- message that is sent to user
    """
    sendMessage(s, ".w "+user+" "+message)
    
def threadFillOpList():
    while True:
        try:
            url = cfg.URL
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            cfg.MODS.clear()
            str_response = response.read().decode('utf-8')
            data = json.loads(str_response)
            for p in data["chatters"]["moderators"]:
                cfg.MODS.append(p)
                if not p == cfg.NICK:
                    addPoints(p, 1)
            for p in data["chatters"]["viewers"]:
                addPoints(p, 1)
        except:
            print()
        time.sleep(5)
        
def isOP(user):
    return user in cfg.MODS