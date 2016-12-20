#data.py

import string
import time
import datetime
import random
from Socket import sendMessage, timeout
from init import MODS

#cooldowns[0] = roulette
#cooldowns[1] = auto twitter
cooldowns = [0,0]

#poll stuff
poll = {}
voterlist = []

#raffle stuff
rafflelist = []

#trigger[0] = poll
#trigger[1] 
trigger = [False, False]


def openpoll(s, message):
    if trigger[0]:
        sendMessage(s, "A poll is already in progress")
    else:
        messagelist = message.split(" ")
        if len(messagelist) > 2:
            trigger[0] = True
            messagelist.remove("!openpoll")
            for i in messagelist:
                poll[i] = 0;
            sendMessage(s, "Poll now open! Use the command !vote <option> to cast a vote")
        else:
            sendMessage(s,"Need at least 2 options to vote from")

def vote(s, message, user):
    messagelist = message.split(" ")
    if trigger[0] and not user in voterlist:
        if messagelist[1] in poll:
            poll[messagelist[1]] = poll[messagelist[1]] + 1
            voterlist.append(user)
        else:
            sendMessage(s, user+" that is not a valid option")
        

def closepoll(s):
    if trigger[0]:
        wonN = "Nothing"
        wonA = 0
        for i, j in poll.items():
            if j > wonA:
                wonA = j
                wonN = i
        sendMessage(s, wonN+" was voted for with "+str(wonA)+" vote(s)")
        trigger[0] = False
        voterlist.clear()
        poll.clear()
    else:
        sendMessage(s, "No poll currently open. Use command !openpoll <arg1> <arg2>... to start a poll")
        
def openraffle(s):
    if trigger[1]:
        sendMessage(s,"A raffle is already in progress")
    else:
        sendMessage(s,"Raffle now open! Use command !raffle to place your name in")
        trigger[1] = True
        
def raffle(s, user):
    if trigger[1] and not user in rafflelist:
        rafflelist.append(user)
        
def closeraffle(s):
    if trigger[1]:
        sendMessage(s,"Raffle closed. Picking a name at random...")
        amount = len(rafflelist) - 1
        randNum = random.randint(0, amount)
        winner = rafflelist[randNum]
        time.sleep(2)
        sendMessage(s, winner+" has won the raffle! Congrats!")
        rafflelist.clear()
        trigger[1] = False
    else:
        sendMessage(s, "No raffle currently open. Use command !openraffle to start")
    
def checkcooldown(sec, listIndex, user):
    i = datetime.datetime.now()
    cTime = (i.hour * 3600) + (i.minute * 60) + i.second
    if user in MODS:
         return True
    if cooldowns[listIndex] == 0:
        cooldowns[listIndex] = cTime
        return True
    coolDown = cTime - cooldowns[listIndex]
    if coolDown > sec:
        cooldowns[listIndex] = cTime
        return True
    return False
    
def roulette(user, s):
    sendMessage(s, "places the revolver to "+user+"'s head")
    time.sleep(2.5)
    if user == "dyxna":
        sendMessage(s, "Oh hey "+user)
        timeout(s, user, 30)
    else:
        num = random.randint(0,1)
        if num == 0:
           sendMessage(s, "The trigger is pulled, and the revolver clicks. "+user+" has lived to survive roulette!")
        else:
            if user in MODS:
                sendMessage(s, "The trigger is pulled, but the revolver malfunctions! "+user+" has miraculously lived to survive roulette")
            else:
                sendMessage(s, "The trigger is pulled, and the revolver fires! "+user+" lies dead in chat")
                timeout(s,user,30)
        
    