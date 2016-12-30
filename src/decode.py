#decode.py

import string
from Socket import sendMessage, timeout
import data
from cfg import CHAN, MODS, DATA

def command(user, message, s):
    print (user+ " used command: "+message)
    message = message[:-1]
    message = message.lower()
    
    ###Admin commands/ other commands###
    temp = message.split(" ")
    if temp[0] == "!addmod" and user is CHAN:
        data.addMod(s, message)
    if temp[0] == "!help":
        data.help(s, message, user)
    
    ##Poll Commands##
    if temp[0] == "!openpoll" and user is CHAN:
        data.openpoll(s, message)
    if temp[0] == "!vote":
        data.vote(s, message, user)
    if message == "!closepoll" and user is CHAN:
        data.closepoll(s)
    
    ##Raffle Commands##
    if message == "!openraffle" and user in MODS:
        data.openraffle(s)
    if message == "!raffle":
        data.raffle(s, user)
    if message == "!closeraffle" and user in MODS:
        data.closeraffle(s)
    
    ##Roulette Commands##
    if message == "!roulette" and checkcooldown(30,0, user):
        data.roulette(user, s)
    
    ###Text Commands (found in cfg.py)###
    message = message.replace(" ","")
    if message in DATA:
        sendMessage(s, DATA[message])
    if "unmodwalkire" in message or "unmodwa1kire" in message:
        if not user in MODS:
            timeout(s,user,120)
            
    ##Endbot Command##
    #USED FOR DEBUGGING
    if message == "!endbot" and user == "walkire":
        print("Ending bot")
        return -1