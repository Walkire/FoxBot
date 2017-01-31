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
'bet':'!bet <number> -- Try your luck in a game of chance! (whole numbers only)',
'leaderboard':'!leaderboard -- Shows top 5 users with the highest points',
'roulette':'!roulette -- take your chance in a game of roulette'
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

URL_REGEX = r"(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.] \
	(?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi| \
	museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar \
	|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by \
	|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk| \
	dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh \
	|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io \
	|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk \
	|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv \
	|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl \
	|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk \
	|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp \
	|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za \
	|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+ \
	?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:' \
	\".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org| \
	edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post| \
	pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax| \
	az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf \
	|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee \
	|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp \
	|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je \
	|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv \
	|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na \
	|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt \
	|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr \
	|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz \
	|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@ \
	)))"