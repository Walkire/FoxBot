#decode.py

import string
from Socket import sendMessage, timeout
from data import checkcooldown, roulette, openpoll, vote, closepoll, openraffle, raffle, closeraffle
from cfg import MODS

def command(user, message, s):
    print (user+ " used command: "+message)
    message = message[:-1]
    message = message.lower()
    
    ##Poll Commands##
    temp = message.split(" ")
    if temp[0] == "!openpoll" and user == "gimmethefox":
        openpoll(s, message)
    if temp[0] == "!vote":
        vote(s, message, user)
    if message == "!closepoll" and user == "gimmethefox":
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
        sendMessage(s, "fox when I said I would never leave you I thought it went both ways. I thought you wouldn't leave me either")
    if message == "!rules":
        sendMessage(s,"No discrimination, No racism, Be mindful of other chatters, No trolling and No spam. We are here to have fun!")
    if message == "!twitter":
        sendMessage(s, "Follow me on Twitter! @Gimmethefox https://twitter.com/Gimmethefox")
    if message == "!flip":
        sendMessage(s, "(╯°□°)╯︵ ┻━┻")
    if message == "!unflip":
        sendMessage(s, "┬─┬﻿ ノ( ゜-゜ノ)")
    if "unmodwalkire" in message or "unmodwa1kire" in message:
        if not user in MODS:
            timeout(s,user,120)
            
    ##Endbot Command##
    if message == "!endbot" and user == "walkire":
        print("Ending bot")
        return -1