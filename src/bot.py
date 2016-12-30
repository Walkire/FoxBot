#bot.py
import string, os
import time
from Socket import openSocket, Pong, sendMessage
from init import joinRoom, ensure_dir, loadMods
from decode import command
from data import checkcooldown
from cfg import NICK, RATE

#Runs init functions for startup / creates socket
s = openSocket()
joinRoom(s)
ensure_dir("etc/")
loadMods("etc/mods.txt")

readbuffer = ""
user = ""
message = ""
end = ""
chatamount = 0

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
                        chatamount = chatamount - 1
                        Pong(s)
                else:
                    message = getMessage(line)
                    if message[0] == '!':
                        user = getUser(line)
                        end = command(user, message, s)
                        
    if end:
        break
    #If 30 messages and 30 minutes go by, run twitter command    
    if chatamount == 30:
        if checkcooldown(1800, 1, "NULLUSER"):
            end = command(NICK, "!twitter\r", s)
            chatamount = 0
    else:
        chatamount = chatamount + 1
        
    time.sleep(1/RATE)