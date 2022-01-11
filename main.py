from _token import gettoken
from _requests import checktoken, downloadimage
from _parser import parsemessages, askmessagecount, askconversationid
from _save import save_data_json, save_data_html

token = gettoken()
checktoken(token)
#downloadimage(token, "718456289704804392", "25ecb6088b58ecec388cc6ce73da0a7c")
messages = parsemessages(token, askconversationid(), askmessagecount())
save_data_json("messages.json", messages)
save_data_html("messages.html", messages)
