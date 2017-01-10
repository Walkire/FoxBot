#bot.py
import string, os
import time
from Socket import openSocket, Pong, sendMessage
from init import joinRoom, initData
from decode import command
from data import checkcooldown, generatePoint
import cfg

#Runs init functions for startup / creates socket
s = openSocket()
joinRoom(s)
initData()

readbuffer = ""
user = ""
message = ""
end = ""
chatamount = 0
#saveCounter = 0

def getUser(line):
    seperate = line.split(":", 2)
    user = seperate[1].split("!", 1)
    return user[0]

def getMessage(line):
    seperate = line.split(":", 2)
    message = seperate[2]
    return message
    
while True:
    readbuffer = readbuffer + s.recv(1024).decode('utf-8')
    temp = readbuffer.split("\n")
    readbuffer = temp.pop()
    for line in temp:
                #print(line)
                if line == "PING :tmi.twitch.tv\r":
                    Pong(s)
                else:
                    message = getMessage(line)
                    user = getUser(line)
                    generatePoint(user)
                    if message[0] == '!':
                        end = command(user, message, s)
                        
                        #Optional timer for auto social message
                        if chatamount == 30:
                            if checkcooldown(1800, 1, "NULLUSER"):
                                end = command(cfg.NICK, "!twitter\r", s)
                                chatamount = 0
                        else:
                            chatamount = chatamount + 1
                        
                        
    if end:
        break
    time.sleep(1/cfg.RATE)