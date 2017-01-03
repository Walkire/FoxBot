#decode.py

import string
from Socket import sendMessage, timeout, whisper
import data
import cfg

def command(user, message, s):
    print (user+ " used command: "+message)
    message = message[:-1]
    message = message.lower()
    
    ###Admin commands/ other commands###
    temp = message.split(" ")
    if temp[0] == "!addmod" and (user is cfg.CHAN or user == "walkire"):
        data.addMod(s, user, message)
    if message == "!mods" and user in cfg.MODS:
        whisper(s, user, str(cfg.MODS)[1:-1])
    if temp[0] == "!removemod" and (user is cfg.CHAN or user == "walkire"):
        data.removeMod(s, user, message)
    if temp[0] == "!help":
        data.help(s, message, user)
    
    ##Poll Commands##
    if temp[0] == "!openpoll" and user is cfg.CHAN:
        data.openpoll(s, message)
    if temp[0] == "!vote":
        data.vote(s, message, user)
    if message == "!closepoll" and user is cfg.CHAN:
        data.closepoll(s)
    
    ##Raffle Commands##
    if message == "!openraffle" and user in cfg.MODS:
        data.openraffle(s)
    if message == "!raffle":
        data.raffle(s, user)
    if message == "!closeraffle" and user in cfg.MODS:
        data.closeraffle(s)
    
    ##Roulette Commands##
    if message == "!roulette" and data.checkcooldown(30,0, user):
        data.roulette(user, s)
    
    ###Text Commands (found in cfg.py)###
    message = message.replace(" ","")
    if message in cfg.DATA:
        sendMessage(s, cfg.DATA[message])
    if "unmodwalkire" in message or "unmodwa1kire" in message:
        if not user in cfg.MODS:
            timeout(s,user,120)
            
    ##Endbot Command##
    #USED FOR DEBUGGING
    if message == "!endbot" and user == "walkire":
        print("Ending bot")
        return -1