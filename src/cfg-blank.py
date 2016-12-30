#cfg.py
HOST = "irc.twitch.tv"                        # the Twitch IRC server
PORT = 6667                                   # always use port 6667!
NICK = # your Twitch username that will be the bot, lowercase
PASS = # your Twitch OAuth token goes here
CHAN = # the channel you want to join
MODS = [] #leave empty
RATE = (80/30) #Messages per second (20/30 for normal users / 100/30 for mods)

"""
List of all possible commands for command !help
CHANGING THESE DOES NOT ADD, CHANGE OR REMOVE COMMANDS
See decode.py for command changes
"""
HELPLIST = {
'addmod': '(Host Only) !addmod <username> -- Adds user to bot mod list',
'openpoll':'(Host Only) !openpoll <option 1> <option 2> ... -- open a poll for users to vote for (needs at least 2 options) use !closepoll to end',
'closepoll':'(Host Only) !closepoll -- closes current poll and gives results, opened by !openpoll',
'openraffle':'(Mods Only) !openraffle -- starts a raffle',
'closeraffle':'(Mods Only) !closeraffle -- closes current raffle and gives results',
'vote':'!vote <option> -- allows you to vote for an option in the poll if one is currently open',
'raffle':'!raffle -- allows you to place your name in the raffle if one is currently open',
'foxleft':'!foxleft -- Use when fox leaves us :(',
'rules':'!rules -- shows channel rules',
'twitter':'!twitter -- shows channel twitter page url',
'flip':'!flip -- flips the table',
'unflip':'!unflip -- unflips the table :(',
}

"""
All text commands here:
twitter -- Put twitter URL and message here
rules --  Put the channel rules here
foxleft -- put whatever you want here, change the command name above and in decode.py
"""
DATA = {
'twitter':'twitter message here',
'rules':'rules message here',
}