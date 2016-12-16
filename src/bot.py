#bot.py
import string
import time
from Socket import openSocket, Pong, sendMessage
from init import joinRoom
from decode import command
from data import checkcooldown

s = openSocket()
joinRoom(s)

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
        
    if chatamount == 30:
        if checkcooldown(1800, 1, "NULLUSER"):
            end = command("foxbrobot", "!twitter\r", s)
            chatamount = 0
    else:
        chatamount = chatamount + 1
        
    time.sleep(.1)