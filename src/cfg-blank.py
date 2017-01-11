#cfg.py
HOST = "irc.twitch.tv"                        # the Twitch IRC server
PORT = 6667                                   # always use port 6667!
NICK = ''# your Twitch username that will be the bot, lowercase
PASS = ''# your Twitch OAuth token goes here
CHAN = ''# the channel you want to join
URL = "http://tmi.twitch.tv/group/user/"+CHAN+"/chatter"
RATE = (80/30) #Messages per second (20/30 for normal users / 100/30 for mods)
POINTS = {} #leave empty
MODS = [] #leave empty

"""
List of all possible commands for command !help
CHANGING THESE DOES NOT ADD, CHANGE OR REMOVE COMMANDS
See decode.py for command changes or below for text command changes
"""
HELPLIST = {
'openpoll':'(Mods Only) !openpoll <option 1> <option 2> ... -- open a poll for users to vote for (needs at least 2 options) use !closepoll to end',
'closepoll':'(Mods Only) !closepoll -- closes current poll and gives results, opened by !openpoll',
'openraffle':'(Mods Only) !openraffle -- starts a raffle',
'closeraffle':'(Mods Only) !closeraffle -- closes current raffle and gives results',
'mods':'!mods -- Shows list of current mods online',
'vote':'!vote <option> -- allows you to vote for an option in the poll if one is currently open',
'raffle':'!raffle -- allows you to place your name in the raffle if one is currently open',
'rules':'!rules -- shows channel rules',
'twitter':'!twitter -- shows channel twitter page url',
'flip':'!flip -- flips the table',
'unflip':'!unflip -- unflips the table :(',
'points':'!points -- Shows how many points you have',
'bet':'!bet <number> -- Try your luck in a game of chance! (whole numbers only)'
}

"""
All text commands here:
add as many as needed '!command':'message sent'
"""
DATA = {
'!social':'twitter/facebook/other message here',
'!rules':'rules message here',
'!flip':'(╯°□°)╯︵ ┻━┻',
'!unflip':'┬─┬﻿ ノ( ゜-゜ノ)'
}