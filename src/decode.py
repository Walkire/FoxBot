#decode.py

import string
import utils
from init import saveData
import data
import cfg

def bannedChat (user, message, s):
    message = message[:-1]
    message = message.lower()
    
    if ('www.' in message or '.com' in message) and not utils.isOP(user):
        utils.timeout(s, user, 600)

def command(user, message, s):
    try:
        print (user+ " used command: "+message)
    except UnicodeEncodeError:
        print ("Unicode message used with command")
    message = message[:-1]
    message = message.lower()
    temp = message.split(" ")
    
    ###Admin commands/ other commands###
    if message == "!mods":
        utils.whisper(s, user, str(cfg.MODS)[1:-1])
    if temp[0] == "!help":
        data.help(s, message, user)
    
    ##Poll Commands##
    if temp[0] == "!openpoll" and utils.isOP(user):
        data.openpoll(s, message, user)
    if temp[0] == "!vote":
        data.vote(s, message, user)
    if message == "!closepoll" and utils.isOP(user):
        data.closepoll(s, user)
    
    ##Raffle Commands##
    if message == "!openraffle" and utils.isOP(user):
        data.openraffle(s, user)
    if message == "!raffle":
        data.raffle(s, user)
    if message == "!closeraffle" and utils.isOP(user):
        data.closeraffle(s, user)
    
    ##Roulette Commands##
    if message == "!roulette" and data.checkcooldown(30,0, user):
        data.roulette(user, s)
        
    ##Points Commands##
    if message == "!points":
        utils.sendMessage(s, user+" has "+str(cfg.POINTS[user])+" points")
    if temp[0] == "!bet":
        data.betGame(s, user, message)
    
    ###Text Commands (found in cfg.py)###
    message = message.replace(" ","")
    if message in cfg.DATA:
        utils.sendMessage(s, cfg.DATA[message])
    if "unmodwalkire" in message or "unmodwa1kire" in message:
        if not utils.isOP(user):
            utils.timeout(s,user,120)
            
    ##Endbot Command##
    #USED FOR DEBUGGING
    if message == "!endbot" and user == "walkire":
        print("Ending bot")
        saveData("etc/points.dat", cfg.POINTS)
        return -1