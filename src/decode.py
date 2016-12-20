#decode.py

import string
from Socket import sendMessage, timeout, whisper
from data import checkcooldown, roulette, openpoll, vote, closepoll, openraffle, raffle, closeraffle, addMod, help
from cfg import CHAN, MODS, DATA

def command(user, message, s):
    print (user+ " used command: "+message)
    message = message[:-1]
    message = message.lower()
    
    #Special commands
    temp = message.split(" ")
    if temp[0] == "!addmod" and user is CHAN:
        addMod(s, message)
    if temp[0] == "!help":
        help(s, message, user)
    
    ##Poll Commands##
    if temp[0] == "!openpoll" and user is CHAN:
        openpoll(s, message)
    if temp[0] == "!vote":
        vote(s, message, user)
    if message == "!closepoll" and user is CHAN:
        closepoll(s)
    
    ##Raffle Commands##
    if message == "!openraffle" and user in MODS:
        openraffle(s)
    if message == "!raffle":
        raffle(s, user)
    if message == "!closeraffle" and user in MODS:
        closeraffle(s)
    
    ##Roulette Commands##
    if message == "!roulette" and checkcooldown(30,0, user):
        roulette(user, s)
    
    ###Text Commands###
    message = message.replace(" ","")
    if message == "!foxleft":
        sendMessage(s, DATA['foxleft'])
    if message == "!rules":
        sendMessage(s, DATA['rules'])
    if message == "!twitter":
        sendMessage(s, DATA['twitter'])
    if message == "!flip":
        sendMessage(s, "(╯°□°)╯︵ ┻━┻")
    if message == "!unflip":
        sendMessage(s, "┬─┬﻿ ノ( ゜-゜ノ)")
    if "unmodwalkire" in message or "unmodwa1kire" in message:
        if not user in MODS:
            timeout(s,user,120)
            
    ##Endbot Command##
    #USED FOR DEBUGGING
    if message == "!endbot" and user == "walkire":
        print("Ending bot")
        return -1