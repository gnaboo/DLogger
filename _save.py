# -*- coding: utf-8 -*-
import json
import codecs

def htmlheader(): 
    return """<!DOCTYPE html>
    <html lang="en" >

    <head>
    <meta charset="UTF-8">
    <title>DLogged Conversation</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body>

    
    <div class="flex-container">
    <div class="flex-item">
        <div class="icon messenger" data-tooltip="Direct Messages"></div>
        <div class="icon" data-tooltip="DLogger"></div>
        <div class="icon" data-tooltip=":)"></div>
    </div>
    <div class="flex-item">
        <div class="header">
        <div class="title">DLogged Conversation</div>
        </div>
    
        <div class="body">
        <div class="group">
            
        </div>
        <div class="group">
            <div class="category">Voice Channels</div>
            <div class="channel">
            <div class="title"> channel</div>
            </div>
        </div>
        </div>
        <div class="footer"></div>
    </div>
    <div class="flex-item">
        <div class="header">
        <div class="title">
            <div class="prefix">&num;</div>general
        </div>
        </div>

        <div class="body">
        <div class="post">
            <div class="avatar"></div>
            <div class="text">"""

def htmlfooter():
    return """<div class="footer"></div>
    </div>
    <div class="flex-item"></div>
    </div>

    </body>

    </html>"""

def htmlmessage(content, author, timestamp, modified, mentions = [""]):
    if mentions == []: mentions = [{"username": ""}]
    if modified == "None": modified = ""
    else: modified = f"(modifié: {modified})"
    message = f"""<div class="post">
        <div class="avatar"></div>
        <div class="text">
          <div class="username">{str(author["username"])}</div>
          <div class="mention">{str(mentions[0]["username"])}</div>
          <div class="timestamp">{timestamp}</div>
          <div class="message">{content}</div>
          <div class="modified">{(modified)}</div>
        </div>
      </div>"""
    return message

def save_data_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def save_data_html(filename, data):
    finaldata = [htmlheader()]
    
    data.reverse()
    for _data in data:
        _data.reverse()

    for i, y in enumerate(data):
        for z in y:
            content = str(z["content"])
            author = z["author"]
            timestamp = str(z["timestamp"])
            modified = str(z["edited_timestamp"])
            if modified == None: modified = ""
            mentions = z["mentions"]
            finaldata.append(htmlmessage(content, author, timestamp, modified, mentions))
    finaldata.append(htmlfooter())
    with codecs.open(filename, "w", "utf-8-sig") as f:
        f.write('\n'.join(finaldata))