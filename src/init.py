#init.py

import string, os
from Socket import sendMessage
from cfg import NICK, CHAN

MODS = []

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.mkdir(d)

def loadMods(file):
	#Create file if it exists and preloads it with the
	#bot name and host name
    if not os.path.exists(file):
        f = open(file, 'a')
        f.write(NICK+'\n')
        f.write(CHAN+'\n')
        f.close()
        print("Mods file made for the first time, check README for more info")
		
    f = open(file,'r')
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]
        MODS.append(line)
    print("Mods found: ")
    print(MODS)
    f.close()

def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024).decode('utf-8')
        temp = readbuffer.split("\n")
        readbuffer = temp.pop()
        
        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    #sendMessage (s, "Successfully joined chat")
    
def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
            