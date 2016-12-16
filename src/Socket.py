#socket.py
import socket
from cfg import HOST, PORT, PASS, NICK, CHAN

def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(("PASS " + PASS + "\r\n").encode('utf-8'))
    s.send(("NICK " + NICK + "\r\n").encode('utf-8'))
    s.send(("JOIN #" + CHAN + "\r\n").encode('utf-8'))
    #s.send(("CAP REQ :twitch.tv/tags\r\n").encode('utf-8'))
    return s

def sendMessage(s, message):
        messageTemp = "PRIVMSG #" + CHAN + " :" + message
        s.send((messageTemp + "\r\n").encode('utf-8'))
        try:
                print("Sent: " + messageTemp)
        except UnicodeEncodeError:
                print("Unicode message sent")

def Pong(s):
        s.send(("PONG :tmi.twitch.tv\r\n").encode("utf-8"))
        print("Sent PONG")

def timeout(s, user, secs):
    """
    Time out a user for a set period of time.
    Keyword arguments:
    sock -- the socket over which to send the timeout command
    user -- the user to be timed out
    secs -- the length of the timeout in seconds (default 600)
    """
    secs = str(secs)
    sendMessage(s,".timeout "+user+" "+secs)
    print(user +" has been timed out for "+secs+" seconds")
