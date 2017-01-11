#bot.py
import string, os
import time, _thread
import utils
from init import joinRoom, initData
from decode import command, bannedChat
from data import checkcooldown
import cfg

#Runs init functions for startup / creates socket
s = utils.openSocket()
joinRoom(s)
initData()

_thread.start_new_thread(utils.threadFillOpList, ())

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
                    utils.Pong(s)
                else:
                    message = getMessage(line)
                    user = getUser(line)
                    bannedChat(user, message, s)
                    if message[0] == '!':
                        end = command(user, message, s)
                        
                        #Optional timer for auto social message
                        if chatamount == 30:
                            if checkcooldown(1800, 1, "NULLUSER"):
                                end = command(cfg.NICK, "!social\r", s)
                                chatamount = 0
                        else:
                            chatamount = chatamount + 1
                        
                        
    if end:
        break
    time.sleep(1/cfg.RATE)