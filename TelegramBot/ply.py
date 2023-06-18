import requests

def send_msg(text):
   token = "your_token"
   chat_id = "your_chatId"
   url_req = "https://api.telegram.org/bot" + '6202700443:AAFV2jcNIVDet6hC_v2fCx0N9MfrK_sfEpg' + "/getUpdates" + "?chat_id=" + '1494250709' 
   results = requests.get(url_req)
   print(results.json()['result'][0]['message'])

send_msg("Hello there!")

