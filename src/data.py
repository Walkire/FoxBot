#data.py
#Contains functions for more complex commands

import string
import time
import datetime
import random
from init import saveData
from Socket import sendMessage, timeout, whisper
import cfg

#cooldowns[0] = roulette
#cooldowns[1] = auto twitter
#cooldowns[2] = text commands
cooldowns = [0,0,0]

#poll stuff
poll = {}
voterlist = []

#raffle stuff
rafflelist = []

#trigger[0] = poll
#trigger[1] = raffle
trigger = [False, False]

def help(s, message, user):
    messagelist = message.split(" ")
    temp = ""
    
    if len(messagelist) == 1:
        for key in cfg.HELPLIST.keys():
                temp+=str("!"+key+ " ")
        whisper(s, user, "Use !help <command> to learn more -- "+temp)
    if len(messagelist) > 1:
        try:
            whisper(s, user, cfg.HELPLIST[messagelist[1]])
        except KeyError:
            whisper(s, user, "Command does not exist, Usage: !help <command name>")

def addMod(s, user, data):
    messagelist = data.split(" ")
    if len(messagelist) == 2:
        cfg.MODS.append(messagelist[1])
        saveData("etc/mods.dat", cfg.MODS)
        whisper(s, user, "Added user "+messagelist[1]+" to mod list")
    else:
        whisper(s, "Invalid syntax, command is !addmod <name>, only provide one name")
        
def removeMod(s, user, data):
    messagelist = data.split(" ")
    if len(messagelist) == 2:
        if messagelist[1] in cfg.MODS:
            cfg.MODS.remove(messagelist[1])
            saveData("etc/mods.dat", cfg.MODS)
            whisper(s, user, "Removed user "+messagelist[1]+" from mod list")
        else:
            whisper(s, user, messagelist[1]+" does not exist in mod list")
    else:
        whisper(s, user, "Invalid syntax, command is !removemod <name>, only provide one name")

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
    if user in cfg.MODS:
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
    num = random.randint(0,1)
    if num == 0:
        sendMessage(s, "The trigger is pulled, and the revolver clicks. "+user+" has lived to survive roulette!")
    else:
        if user in cfg.MODS:
            sendMessage(s, "The trigger is pulled, but the revolver malfunctions! "+user+" has miraculously lived to survive roulette")
        else:
            sendMessage(s, "The trigger is pulled, and the revolver fires! "+user+" lies dead in chat")
            timeout(s,user,30)
        
    