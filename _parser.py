from _requests import getmessages, getmessagesbefore
import math
import random
import time

def generaterandomtiming():
    rand = "".join(random.choice("0123456789") for i in range(4))
    
    return int(rand)/10000

def parsemessages(token, conversationid, MESSAGESCOUNT=14061):
    messageslist = []

    messages = getmessages(token, conversationid)
    messageslist.append(messages)

    requestscounter = math.ceil(int(MESSAGESCOUNT) / 50)
    print("[+] Parsing messages...")
    print(f"[+] There are {requestscounter} requests to make.")

    for i in range(requestscounter):
        try:
            print(f"[+] Parsing messages {i+1}/{requestscounter}...", end="\r")
            id = messages[-1]["id"]
            time.sleep(generaterandomtiming())
            messages = getmessagesbefore(token, id, conversationid)
            messageslist.append(messages)
        except IndexError:
            print("[-] There are no more messages to parse.")
            break

    return messageslist

def parseallmessages(token, conversationid):
    messageslist = []

    messages = getmessages(token, conversationid)
    messageslist.append(messages)

    print("[+] Parsing messages...")

    while True:
        try:
            id = messages[-1]["id"]
            time.sleep(generaterandomtiming())
            messages = getmessagesbefore(token, id, conversationid)
            messageslist.append(messages)
        except IndexError:
            print("[-] There are no more messages to parse.")
            break

    return messageslist

def extractconversationid(messageurl):
    return messageurl.split("/")[-2]

