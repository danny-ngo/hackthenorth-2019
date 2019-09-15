import os, sys
from flask import Flask, request
from pymessenger import Bot
import requests
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
    return "Hello world", 200
    
@app.route('/', methods=['POST'])
def handle_messages():
    data = request.get_json()
    log(data)
    
    for sender, message in messaging_events(data):
        print 'Incoming from {}: {}'.format(sender, message)
        send_message(PAGE_ACCESS_TOKEN, sender, message)
    return "OK", 200

def log(message):
    print(message)
    sys.stdout.flush()
    
def messaging_events(payload): 
    '''
    Generate tuples of (sender_id, message_text) from the provided payload
    '''
    data = json.loads(payload)
    messaging_events = data['entry'][0]['messaging']
    
    for event in messaging_events:
        if "message" in event and "text" in event['message']:
            yield event['sender']['id'], event['message']['text'].encode('unicode_escape')
        else:
            yield event['sender']['id'], "Cannot echo this message"
            
def send_message(token, recipient, message):
    '''
    Send message to recipient id
    '''
    
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": token},
            data=json.dumps({
                "recipient": {"id": recipient},
                "message": {"text": 'Hello',
                            "quick_replies":create_quick_replies()}
            }),
            headers={'Content-type': 'application/json'})
    
'''    
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
    
    return "OK", 200
    
def log(message):
    print(message)
    sys.stdout.flush()
'''
    
if __name__ == "__main__":
    app.run(debug = True, port = 80)