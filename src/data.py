#data.py
#Contains functions for more complex commands

import string
import time
import datetime
import random
from init import saveData
import utils
import cfg

"""
cooldowns[0] = roulette
cooldowns[1] = auto twitter
cooldowns[2] = bet command
"""
cooldowns = [0,0,0]

#poll stuff
poll = {}
voterlist = []

#raffle stuff
rafflelist = []

#points stuff
saveCounter = 0

"""
Tracks if event is in progress or not
trigger[0] = poll
trigger[1] = raffle
"""
trigger = [False, False]

def addPoints(user, amount):
    if user in cfg.POINTS:
        cfg.POINTS[user] += amount
    else:
        cfg.POINTS[user] = (10 + amount)
    saveData("etc/points.dat", cfg.POINTS)
    
def betGame(s, user, message):
    messagelist = message.split(" ")
    if len(messagelist) == 2 and messagelist[1].isdigit():
        bet = int(messagelist[1])
        num = random.randint(1,100)
        if bet > cfg.POINTS[user]:
            utils.sendMessage(s, user+" you are too broke to bet that much")
        else:
            cfg.POINTS[user] -= bet
            if num < 51:
                utils.sendMessage(s, "Sorry, you lost it all "+user+" :(")
            if num < 76 and num > 50:
                utils.sendMessage(s, "You won "+user+", but only broke even")
                cfg.POINTS[user] += bet
            if num < 100 and num > 75:
                utils.sendMessage(s, "You won double the amount you bet "+user+"!")
                cfg.POINTS[user] += (bet*2)
            if num == 100:
                utils.sendMessage(s, "Congrats "+user+", you won 3 times the amount you bet!")
                cfg.POINTS[user] += (bet*3)
            saveData("etc/points.dat", cfg.POINTS)
    else:
        utils.whisper(s, user, "Invalid syntax, command is: "+cfg.HELPLIST['bet'])
        
def help(s, message, user):
    messagelist = message.split(" ")
    temp = ""
    
    if len(messagelist) == 1:
        for key in cfg.HELPLIST.keys():
                temp+=str("!"+key+ " ")
        utils.whisper(s, user, "Use !help <command> to learn more -- "+temp)
    if len(messagelist) > 1:
        try:
            utils.whisper(s, user, cfg.HELPLIST[messagelist[1]])
        except KeyError:
            utils.whisper(s, user, "Command does not exist, Usage: !help <command name>")

def openpoll(s, message, user):
    if trigger[0]:
        utils.whisper(s, user, "A poll is already in progress")
    else:
        messagelist = message.split(" ")
        if len(messagelist) > 2:
            trigger[0] = True
            messagelist.remove("!openpoll")
            for i in messagelist:
                poll[i] = 0;
            utils.sendMessage(s, "Poll now open! Use the command !vote <option> to cast a vote")
        else:
            utils.whisper(s, user, "Need at least 2 options to vote from")

def vote(s, message, user):
    messagelist = message.split(" ")
    if trigger[0] and not user in voterlist:
        if messagelist[1] in poll:
            poll[messagelist[1]] = poll[messagelist[1]] + 1
            voterlist.append(user)
        else:
            utils.whisper(s, user, "Invalid syntax, command is: "+cfg.HELPLIST['vote'])
        

def closepoll(s, user):
    if trigger[0]:
        wonN = "Nothing"
        wonA = 0
        for i, j in poll.items():
            if j > wonA:
                wonA = j
                wonN = i
        utils.sendMessage(s, wonN+" was voted for with "+str(wonA)+" vote(s)")
        trigger[0] = False
        voterlist.clear()
        poll.clear()
    else:
        utils.whisper(s, user, "Invalid syntax, command is: "+cfg.HELPLIST['closepoll'])
        
def openraffle(s, user):
    if trigger[1]:
        utils.whisper(s, user, "A raffle is already in progress")
    else:
        utils.sendMessage(s,"Raffle now open! Use command !raffle to place your name in")
        trigger[1] = True
        
def raffle(s, user):
    if trigger[1] and not user in rafflelist:
        rafflelist.append(user)
        
def closeraffle(s, user):
    if trigger[1]:
        utils.sendMessage(s,"Raffle closed. Picking a name at random...")
        amount = len(rafflelist) - 1
        randNum = random.randint(0, amount)
        winner = rafflelist[randNum]
        time.sleep(2)
        utils.sendMessage(s, winner+" has won the raffle! Congrats!")
        rafflelist.clear()
        trigger[1] = False
    else:
        utils.whisper(s, user, "Invalid syntax, command is: "+cfg.HELPLIST['closeraffle'])
   
def checkcooldown(sec, listIndex, user):
    i = datetime.datetime.now()
    cTime = (i.hour * 3600) + (i.minute * 60) + i.second
    if utils.isOP(user):
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
    utils.sendMessage(s, "places the revolver to "+user+"'s head")
    time.sleep(2.5)
    num = random.randint(0,1)
    if num == 0:
        utils.sendMessage(s, "The trigger is pulled, and the revolver clicks. "+user+" has lived to survive roulette!")
    else:
        if utils.isOP(user):
            utils.sendMessage(s, "The trigger is pulled, but the revolver malfunctions! "+user+" has miraculously lived to survive roulette")
        else:
            utils.sendMessage(s, "The trigger is pulled, and the revolver fires! "+user+" lies dead in chat")
            utils.timeout(s,user,30)
        
    