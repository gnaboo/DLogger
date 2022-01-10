
def Auth():
    import os
    from json import loads, dump
    from re import findall
    if os.name != "nt":
        exit()
    LOCAL = os.getenv('LOCALAPPDATA')
    ROAMING = os.getenv("APPDATA")
    PATHS = {
        "Discord"           : ROAMING + r"\Discord",
        "Discord Canary"    : ROAMING + r"\discordcanary",
        "Discord PTB"       : ROAMING + r"\discordptb",
        "Google Chrome"     : LOCAL + r"\Google\Chrome\User Data\Default",
        "Opera"             : ROAMING + r"\Opera Software\Opera Stable",
        "Brave"             : LOCAL + r"\BraveSoftware\Brave-Browser\User Data\Default",
        "Yandex"            : LOCAL + r"\Yandex\YandexBrowser\User Data\Default"
    }
    tokens = {}
    def gettokens(path):
        try:
            path += "\\Local Storage\\leveldb"
            tokens = []
            for file_name in os.listdir(path):
                if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                    continue
                for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in findall(regex, line):
                            tokens.append(token)
            return tokens
        except:
            pass

    for path in PATHS:
        token = gettokens(PATHS[path])
        if token != None and token != []:
            for _token in token:
                if _token.startswith('mfa.'):
                    tokens[_token] = path

    return tokens

def gettoken():
    tokens = Auth()
    tokens = list(tokens.keys())
    print(f"[Found {len(tokens)} tokens]") if len(tokens) > 1 else print(f"[Found {len(tokens)} token]")
    for i, y in enumerate(tokens):
        censure = "*" * 10
        print(f"[{i+1}] {y[:20]}{censure}")

    if len(tokens) > 1:
        print("[Enter the number of the token you want to use]")
        token = input("Token: ")
        if token.isdigit():
            token = tokens[int(token)-1]
        else:
            token = tokens[0]

    else:
        token = tokens[0]
    return token

