from _requests import getmessages, getmessagesbefore
import math

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

            messages = getmessagesbefore(token, id, conversationid)
            messageslist.append(messages)
        except IndexError:
            print("[-] There are no more messages to parse.")
            break

    return messageslist

def askconversationid():
    print("[+] Please enter the conversation ID:")
    return input("Conversation ID: ")

def askmessagecount():
    print("[+] Please enter the number of messages to parse:")
    return input("Number of messages to parse: ")

