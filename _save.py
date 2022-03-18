# -*- coding: utf-8 -*-
import json
import codecs
import datetime
import re
import os

def get_time():
    return datetime.datetime.now().strftime("%d/%m%y %H:%M:%S")

def htmlheader(): 
    return ("""<!DOCTYPE html>
    <html lang="en" >

    <head>
    <meta charset="UTF-8">
    <title>DLogged Conversation</title>
        <style>
        /*Downloaded from https://www.codeseek.co/nicholasdrzewiecki/discord-responsive-recreation-owbzvz */

    .downtext{
        font-size: 1.5em;
        font-weight: bold;
        color: #fff;
        text-align: center;
        margin-top: 1em;
        margin-bottom: 1em;
    }
    *{
  scroll-behavior: smooth;
    }

    .circle{
    min-width: 32px;
    min-height: 32px;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background-color: #7289da;
    margin: 0 1rem 0 0;
    cursor: pointer;
    transition: all 0.2s ease;
    display: block;
    overflow: hidden;
    }
    .circle img{
    min-width: 32px;
    min-height: 32px;
    border-radius: 50%;
    }
    .circle:hover{
    transform: scale(1.1);
    }

    .attachement{
    margin: auto;
    display: flex;
    align-items: center;
    width: auto;
    height: auto;
    max-width: 250px;
    max-height: 250px;
    }

    .attachement:hover{
    transform: scale(1.5);
    }

    body {
        margin: 0;
        font-family: "Hind Vadodara", sans-serif;
        overflow-x: hidden;
    }
    
    .flex-container {
        display: flex;
        height: 100vh;
    }
    .flex-container .flex-item:nth-child(1) {
        display: flex;
        flex: 0 0 67px;
        flex-direction: column;
        align-items: center;
        background-color: #1F2124;
    }
    .flex-container .flex-item:nth-child(1) .icon {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        position: relative;
        background-color: #2e3136;
        border-radius: 50%;
        min-width: 50px;
        min-height: 50px;
        cursor: pointer;
    }
    .flex-container .flex-item:nth-child(1) .icon:before, .flex-container .flex-item:nth-child(1) .icon:after {
        position: absolute;
        pointer-events: none;
        opacity: 0;
        z-index: -1;
    }
    .flex-container .flex-item:nth-child(1) .icon:hover:before, .flex-container .flex-item:nth-child(1) .icon:hover:after {
        opacity: 1;
        z-index: 1;
    }
    .flex-container .flex-item:nth-child(1) .icon:before {
        left: calc(100% + 0.25rem);
        border-top: 0.25rem solid transparent;
        border-bottom: 0.25rem solid transparent;
        border-right: 0.25rem solid #7289da;
        content: "";
    }
    .flex-container .flex-item:nth-child(1) .icon:after {
        left: calc(100% + 0.5rem);
        background-color: #7289da;
        border-radius: 0.25rem;
        color: #fff;
        font-size: 0.75rem;
        padding: 0.25rem 0.5rem;
        content: attr(data-tooltip);
        white-space: nowrap;
    }
    .flex-container .flex-item:nth-child(1) .icon:first-child {
        margin-top: 0.5rem;
    }
    .flex-container .flex-item:nth-child(1) .icon:not(:last-child) {
        margin-bottom: 0.5rem;
    }
    .flex-container .flex-item:nth-child(1) .icon.messenger {
        background-image: url(data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjwhLS0gR2VuZXJhdG9yOiBBZG9iZSBJbGx1c3RyYXRvciAxOS4wLjAsIFNWRyBFeHBvcnQgUGx1Zy1JbiAuIFNWRyBWZXJzaW9uOiA2LjAwIEJ1aWxkIDApICAtLT4NCjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeG1sbnM6c2tldGNoPSJodHRwOi8vd3d3LmJvaGVtaWFuY29kaW5nLmNvbS9za2V0Y2gvbnMiDQoJIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSItMjg5IDM4MiAzMiAzMCINCgkgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAtMjg5IDM4MiAzMiAzMDsiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4NCgkuc3Qwe2ZpbGw6I0ZGRkZGRjt9DQoJLnN0MXtvcGFjaXR5OjAuNjt9DQo8L3N0eWxlPg0KPHBhdGggY2xhc3M9InN0MCIgZD0iTS0yNzMsNDA5LjVMLTI3Myw0MDkuNWMtNC4xLDAtNi44LTAuNi03LjktMS43Yy0wLjUtMC42LTAuNi0xLjEtMC42LTEuM2MwLTAuNywwLjEtMi45LDAuNi0zLjgNCgljMC4xLTAuMywwLjUtMSw0LjUtMi40Yy0xLjYtMS40LTIuNi00LTIuNi03LjFjMC00LjIsMi4zLTcsNS45LTcuMWwwLjEsMGMzLjYsMC4xLDUuOSwyLjgsNS45LDcuMWMwLDMuMS0xLDUuNy0yLjYsNy4xDQoJYzQsMS40LDQuNCwyLjEsNC41LDIuNGMwLjQsMC45LDAuNSwzLjEsMC42LDMuOGMwLDAuMiwwLDAuNy0wLjYsMS4zQy0yNjYuMyw0MDguOS0yNjguOSw0MDkuNS0yNzMsNDA5LjV6IE0tMjczLDQwNy41TC0yNzMsNDA3LjUNCgljNS4xLDAsNi4yLTAuOSw2LjQtMS4xYy0wLjEtMS4xLTAuMi0yLjMtMC4zLTIuN2MtMC42LTAuNC0yLjktMS4zLTQuOC0xLjlsLTAuNy0wLjJsLTAuMS0ybDAuNy0wLjNjMS43LTAuNiwyLjgtMy4xLDIuOC02LjENCgljMC0zLjEtMS41LTUtMy45LTUuMWMtMi41LDAtNCwyLTQsNS4xYzAsMywxLjEsNS41LDIuOCw2LjFsMC43LDAuM2wtMC4xLDJsLTAuNywwLjJjLTEuOSwwLjYtNC4yLDEuNS00LjgsMS45DQoJYy0wLjEsMC40LTAuMywxLjYtMC4zLDIuN0MtMjc5LjIsNDA2LjYtMjc4LDQwNy41LTI3Myw0MDcuNXoiLz4NCjxnIGNsYXNzPSJzdDEiPg0KCTxwYXRoIGNsYXNzPSJzdDAiIGQ9Ik0tMjU3LDQwMi44YzAtMC43LTAuMS0yLjktMC42LTMuOGMtMC4xLTAuMy0wLjUtMS00LjUtMi40YzEuNi0xLjQsMi42LTQsMi42LTcuMWMwLTQuMi0yLjMtNy01LjktNy4xbC0wLjEsMA0KCQljLTEuOSwwLTMuNSwwLjgtNC41LDIuMmMwLjYsMC4zLDEuMiwwLjYsMS44LDFjMC43LTAuOCwxLjYtMS4zLDIuOC0xLjNjMi40LDAsMy45LDIsMy45LDUuMWMwLDMtMS4xLDUuNS0yLjgsNi4xbC0wLjcsMC4zbDAuMSwyDQoJCWwwLjcsMC4yYzEuOSwwLjYsNC4zLDEuNSw0LjgsMS45YzAuMSwwLjQsMC4zLDEuNiwwLjMsMi43Yy0wLjIsMC4yLTEsMC44LTMuOCwxYzAuMSwwLjYsMC4yLDEuMiwwLjIsMmMyLjUtMC4yLDQuMi0wLjgsNS0xLjYNCgkJQy0yNTcsNDAzLjUtMjU3LDQwMy0yNTcsNDAyLjh6Ii8+DQoJPHBhdGggY2xhc3M9InN0MCIgZD0iTS0yODcsNDAyLjdjMC4xLTEuMSwwLjItMi4zLDAuMy0yLjdjMC42LTAuNCwyLjktMS4zLDQuOC0xLjlsMC43LTAuMmwwLjEtMmwtMC43LTAuMw0KCQljLTEuNi0wLjYtMi44LTMuMS0yLjgtNi4xYzAtMy4xLDEuNS01LDQtNS4xYzEuMiwwLDIuMSwwLjUsMi44LDEuM2MwLjUtMC40LDEuMS0wLjgsMS44LTFjLTEtMS40LTIuNi0yLjItNC41LTIuMmwtMC4xLDANCgkJYy0zLjYsMC01LjksMi44LTUuOSw3LjFjMCwzLjEsMSw1LjcsMi42LDcuMWMtNCwxLjQtNC40LDIuMS00LjUsMi40Yy0wLjQsMC45LTAuNSwzLjEtMC42LDMuOGMwLDAuMiwwLDAuNywwLjYsMS4zDQoJCWMwLjgsMC45LDIuNSwxLjQsNS4xLDEuNmMwLTAuNywwLjEtMS40LDAuMi0yQy0yODYsNDAzLjUtMjg2LjgsNDAyLjktMjg3LDQwMi43eiIvPg0KPC9nPg0KPC9zdmc+DQo=);
        background-repeat: no-repeat;
        background-position: 50%;
        background-size: 1.75rem 1.25rem;
    }
    .flex-container .flex-item:nth-child(2) {
        background-color: #303136;
        flex: 0 0 240px;
        flex-direction: column;
    }
    .flex-container .flex-item:nth-child(2) .header {
        display: flex;
        align-items: center;
        border-bottom: 1px solid #1F2124;
        height: 67px;
        padding: 0 1rem;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .flex-container .flex-item:nth-child(2) .header:hover {
        background-color: #26272B;
    }
    .flex-container .flex-item:nth-child(2) .header .title {
        color: #fff;
        font-size: 1rem;
        font-weight: 500;
    }
    .flex-container .flex-item:nth-child(2) .body {
        padding: 2rem 0.5rem;
    }
    .flex-container .flex-item:nth-child(2) .body .group:not(:last-child) {
        margin-bottom: 1rem;
    }
    .flex-container .flex-item:nth-child(2) .body .category {
        color: rgba(255, 255, 255, 0.3);
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.05rem;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        padding: 0 0 0 0.5rem;
        pointer-events: none;
    }
    .flex-container .flex-item:nth-child(2) .body .channel {
        color: rgba(255, 255, 255, 0.3);
        cursor: pointer;
        font-weight: 300;
    }
    .flex-container .flex-item:nth-child(2) .body .channel .title {
        padding: 0.5rem;
    }
    .flex-container .flex-item:nth-child(2) .body .channel:hover {
        color: rgba(255, 255, 255, 0.7);
        background-color: #36393f;
        border-radius: 3px;
    }
    .flex-container .flex-item:nth-child(3) {
        background-color: #36393E;
        flex-grow: 1;
        overflow-y: scroll;
    }
    .flex-container .flex-item:nth-child(3) .header {
        display: flex;
        align-items: center;
        border-bottom: 1px solid #1F2124;
        height: 67px;
        padding: 0 1rem;
    }
    .flex-container .flex-item:nth-child(3) .header .title {
        color: #fff;
        font-size: 1.25rem;
        font-weight: 700;
    }
    .flex-container .flex-item:nth-child(3) .header .title .prefix {
        display: inline;
        color: rgba(255, 255, 255, 0.3);
        font-weight: 300;
        padding: 0 0.25rem 0 0;
        pointer-events: none;
    }
    .flex-container .flex-item:nth-child(3) .body {
        padding: 1rem;
        font-weight: 300;
        overflow-x: hidden;
    }
    .flex-container .flex-item:nth-child(3) .body .post {
        display: flex;
        align-items: center;
    }
    .flex-container .flex-item:nth-child(3) .body .post:not(:last-child) {
        margin-bottom: 2rem;
        padding-bottom: 2rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .flex-container .flex-item:nth-child(3) .body .post .avatar {
        min-width: 32px;
        min-height: 32px;
        border-radius: 50%;
        background-color: #7289da;
        margin: 0 1rem 0 0;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .flex-container .flex-item:nth-child(3) .body .post .avatar:hover {
        -webkit-filter: brightness(90%);
                filter: brightness(90%);
    }
    .flex-container .flex-item:nth-child(3) .body .post .username {
        display: inline;
        color: #fff;
        font-weight: 500;
        padding: 0 0.25rem 0 0;
        cursor: pointer;
    }
    .flex-container .flex-item:nth-child(3) .body .post .username:hover {
        text-decoration: underline;
    }
    .flex-container .flex-item:nth-child(3) .body .post .timestamp {
        display: inline;
        color: rgba(255, 255, 255, 0.3);
        font-size: 0.75rem;
        font-weight: 300;
    }
        .flex-container .flex-item:nth-child(3) .body .post .modified {
        display: inline;
        color: rgba(196, 117, 97, 0.705);
        font-size: 0.75rem;
    }

    .flex-container .flex-item:nth-child(3) .body .post .mention {
        display: inline;
        color: rgb(192, 109, 53);
        font-size: 100.rem;
    }

    .flex-container .flex-item:nth-child(3) .body .post .message {
        color: rgba(255, 255, 255, 0.7);
    }
    .flex-container .flex-item:nth-child(4) {
        background-color: #303136;
        flex: 0 0 240px;
    }
    
    @media screen and (max-width: 769px) {
        .flex-container {
        flex-direction: column;
        }
        .flex-container .flex-item:nth-child(1) {
        display: flex;
        flex-direction: row;
        }
        .flex-container .flex-item:nth-child(1) .icon:first-child {
        margin-top: 0;
        margin-left: 0.5rem;
        }
        .flex-container .flex-item:nth-child(1) .icon:not(:last-child) {
        margin-bottom: 0;
        margin-right: 0.5rem;
        }
    }
    
    </style>
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
    """
    +
    f"""
        </div>
        <div class="group">
            <div class="category">Conversation logged on: {get_time()}</div>
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
        <a href="#down">Descendre en bas</a>
        <div class="post">
            <div class="avatar"></div>
            <div class="text">""")

def htmlfooter():
    return """
    <div id="down"></div>
    <div class="footer"></div>
    </div>
    <div class="flex-item"></div>
    </div>

    </body>

    </html>"""

def htmlmessage(content, author, timestamp, modified, mentions, reference, attachements, id):
    message = "<div class=\"post\">"
    message += f'<img class="circle" src="https://cdn.discordapp.com/avatars/{author["id"]}/{author["avatar"]}.png">'
    message += '<div class="text">'
    message += f'<div class="username">{author["username"]}</div>'
    if reference != [] and reference != None:
        message += f'<a class="mention" href="#{reference["id"]}"><style="font-weight: bold;">@{reference["author"]["username"]}</style> {reference["content"]}</a>'
    
    if mentions != [] and reference == []: 
        message += f'<div class="mention">mention: {mentions[0]["username"]}</div>'
        content = re.sub(r'<[^>]*>', '', content)
    message += f'<div class="timestamp"> {timestamp}</div>'
    message += f'<div class="message" id="{id}">{content}</div>'
    if modified.count(":") > 0: message += f'<div class="modified">(modifié) {modified}</div>'
    if attachements != []:
        for attachement in attachements:
            message += f'<img class="attachement" src="{attachement["url"]}">'
    message += '</div>'
    message += '</div>'
    return message

def save_data_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def save_data_html(filename, data):
    finaldata = [htmlheader()]
    
    try:
        data.reverse()
        for _data in data:
            _data.reverse()
    except:
        pass

    for i, y in enumerate(data):
        for z in y:
            content = str(z["content"])
            author = z["author"]
            timestamp = str(z["timestamp"])
            modified = str(z["edited_timestamp"])
            if modified == None: modified = ""
            mentions = z["mentions"]
            try:
                reference = z["referenced_message"]
            except:
                reference = []
            attachements = z["attachments"]
            id = z["id"]
            finaldata.append(htmlmessage(content, author, timestamp, modified, mentions, reference, attachements, id))
    finaldata.append(htmlfooter())
    with codecs.open(filename, "w", "utf-8-sig") as f:
        f.write('\n'.join(finaldata))

def outputfolder():
    try:
        os.chdir("output")
    except:
        os.mkdir("output")
        os.chdir("output")

def openhtmlfile(filename):
    os.system(f"start {filename}.html")