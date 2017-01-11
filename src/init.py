#init.py

import string, os, pickle
import cfg

def initData():
    #Load game data
    cfg.POINTS = loadData("etc/points.dat")
    if cfg.POINTS is None:
        cfg.POINTS = {cfg.CHAN:10}
        saveData("etc/points.dat", cfg.POINTS)
    print("Points loaded")

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.mkdir(d)

def loadData(file):
    try:
        return pickle.load(open(file, 'rb'))
    except FileNotFoundError:
        print(file+" does not exist yet")
    
def saveData(file, data):
    pickle.dump(data, open(file,'wb'))
    
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
            