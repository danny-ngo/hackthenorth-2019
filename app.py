import os, sys
from flask import Flask, request
from pymessenger import Bot
import requests
import json
from utils import create_buttons, create_quick_replies

app = Flask(__name__)

PAGE_ACCESS_TOKEN = 'EAANmy13IMxMBAE2pQ96eGFgULzIZBTvjEXQeYUVDJudBEuZALuUMfbBBokMiHAnpxGB2bue4JrZBaL99WcVlZBAOjz4aVTZBAcXGnszx1jRC7UjZBUnMyO0JyvVcUkUjJhFYX2LGewhZAEQBlr8rMoOZCTIp0UViX6AkZAHjivtMEaPM0BD1k8DI7'

bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
    
    #Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "verification mismatch", 403
        return request.args['hub.challenge'], 200
    return "Server running", 200   
  
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)
    
    if data['object'] == "page":
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                #IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']
                
                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'
                        
                    #Send message
                    text = "How was your experience today?"
                    buttons = create_buttons()
                    bot.send_button_message(sender_id, text, buttons)
                    
                elif messaging_event.get('postback'):
                    bot.send_text_message(sender_id, messaging_event['postback']['payload'])
                                     
    return "OK", 200
    
def log(message):
    print(message)
    sys.stdout.flush()
    
if __name__ == "__main__":
    app.run(debug = True, port = 80)