from urllib.request import Request, urlopen
from json import loads

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

def getuserdata(token):
        try:
            loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
        except:
            raise Exception("Failed to get messages. A you sure you have a valid token?")

def getmessages(token, conversationid):
    try:
        return loads(urlopen(Request(f"https://discord.com/api/v9/channels/{conversationid}/messages?limit=50", headers=getheaders(token))).read().decode())
    except Exception as e:
        print(e)
        raise Exception("Failed to get messages. A you sure you have a valid token?")

def getmessagesbefore(token, id, conversationid):
    try:
        return loads(urlopen(Request(f"https://discord.com/api/v9/channels/{conversationid}/messages?before={id}&limit=50", headers=getheaders(token))).read().decode())
    except Exception as e:
        print(e)
        raise Exception("Failed to get messages. A you sure you have a valid token?")

def getmessagescount(token, userid, id): # TODO: implement this
    "https://discord.com/api/v9/channels/*/messages/search?author_id=*&author_id=*"

def downloadimage(token, userid, useravatarid):
    try:
        """download image from url"""
        url = f"https://cdn.discordapp.com/avatars/{userid}/{useravatarid}.png"
        print(url)
        with open(f"{userid}.png", "wb") as f:
            f.write(urlopen(Request(url, headers=getheaders(token))).read())
    except Exception as e:
        raise Exception("Failed to get messages. A you sure you have a valid token / userid / avatar id ?")

def download(url, filename, token):
    try:
        with open(filename, "wb") as f:
            f.write(urlopen(Request(url, headers=getheaders(token))).read())
    except Exception as e:
        print(e)
        raise Exception("Failed to download file. A you sure you have a valid token?")

def checktoken(token):
    try:
        getuserdata(token)
        censure = "*" * 10
        print(f"The {token[:20]}{censure} token is valid!")
        return True
    except:
        censure = "*" * 10
        print(f"The {token[:20]}{censure} token is invalid!")
        return False

