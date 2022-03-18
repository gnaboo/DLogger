from tkinter import StringVar, Tk, ttk
from tkinter.messagebox import showwarning

from _token import gettoken
from _requests import checktoken
from _parser import parsemessages, parseallmessages, extractconversationid
from _save import save_data_json, save_data_html, outputfolder, openhtmlfile, get_time

def parser(token, mid, messages=None):
    """[Make the popup]

    Args:
        token ([token]): [Token]
        mid ([int]): [Message ID]
        messages ([int, None], optional): [Number of messages]. Defaults to None.
    """
    print(token)
    if not checktoken(token):
        showwarning(
            "Error", "Invalid token. Please check your token and try again.")
        return
    if not mid:
        showwarning(
            "Error", "Please enter a conversation ID to extract a conversation ID")
        return
    if messages is not None:
        messages = parsemessages(token, mid, messages)
    else:
        messages = parseallmessages(token, mid)

    date = get_time()
    outputfolder()
    save_data_json(f"messages{date}.json", messages)
    save_data_html(f"messages{date}.html", messages)
    openhtmlfile(f"messages{date}")


def main():
    # make a basic tkinter interface
    root = Tk()
    root.title("DLogger - gnaboo")
    root.geometry("800x700")
    root.resizable(False, False)

    # make a label
    label = ttk.Label(root, text="DLogger - gnaboo")
    label.pack(pady=10)

    button = ttk.Button(root, text="Extract token",
                        command=lambda: token.set(gettoken()))
    button.pack(pady=5)

    # make an entry for a token
    labeltoken = ttk.Label(root, text="Token:")
    labeltoken.pack()
    token = StringVar()
    entry = ttk.Entry(root, textvariable=token)
    entry.pack(pady=20)

    # Separator object
    ttk.Separator(root, orient='horizontal').pack(fill="x")

    # make a extractconversationid button and entry
    labelmessageurl = ttk.Label(root, text="Message URL:")
    labelmessageurl.pack()
    messageurl = StringVar()
    entrymessageurl = ttk.Entry(root, textvariable=messageurl)
    entrymessageurl.pack(pady=10)

    buttonconversationid = ttk.Button(root, text="Extract conversation ID",
        command=lambda: showwarning("Error", "Please enter a Message URL to extract the ID")
        if messageurl.get() == "" else conversationid.set(extractconversationid(messageurl.get())))

    buttonconversationid.pack(pady=5)

    # make an entry for a conversation id
    labelconversationid = ttk.Label(root, text="Conversation ID:")
    labelconversationid.pack(pady=5)
    conversationid = StringVar()
    entryconversationid = ttk.Entry(root, textvariable=conversationid)
    entryconversationid.pack(pady=20)

    # Separator object
    ttk.Separator(root, orient='horizontal').pack(fill="x")

    # make a button
    button = ttk.Button(root, text="Parse All Messages", command=lambda: parser(
        token.get(), entryconversationid.get()))
    button.pack(pady=10)

    # make an entry for a message count
    labelmessagecount = ttk.Label(root, text="Number of messages to parse:")
    labelmessagecount.pack(pady=10)
    messagecount = StringVar()
    entrymessagecount = ttk.Entry(root, textvariable=messagecount)
    entrymessagecount.pack(pady=10)

    # make a button
    button = ttk.Button(root, text="Parse Messages", command=lambda: parser(
        token.get(), entryconversationid.get(), messages=messagecount.get()))
    button.pack(pady = 20)

    # Separator object
    ttk.Separator(root, orient='horizontal').pack(fill="x")

    # Parameters
    labelparameters = ttk.Label(root, text="Parameters:")
    labelparameters.pack(pady=10)

    # make a label
    labelparameters = ttk.Label(root, text="None yet :)")
    labelparameters.pack(pady=5)

    root.mainloop()

main()
