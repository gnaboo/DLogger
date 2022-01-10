from _token import gettoken
from _requests import checktoken
from _parser import parsemessages, askmessagecount, askconversationid
from _save import save_data_json, save_data_html

token = gettoken()
checktoken(token)
messages = parsemessages(token, askconversationid(), askmessagecount())
save_data_json("messages.json", messages)
save_data_html("messages.html", messages)
