import os, sys
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = 'EAANmy13IMxMBAE2pQ96eGFgULzIZBTvjEXQeYUVDJudBEuZALuUMfbBBokMiHAnpxGB2bue4JrZBaL99WcVlZBAOjz4aVTZBAcXGnszx1jRC7UjZBUnMyO0JyvVcUkUjJhFYX2LGewhZAEQBlr8rMoOZCTIp0UViX6AkZAHjivtMEaPM0BD1k8DI7'

bot = Bot()

@app.route('/', methods=['GET'])
def verify():
    
    #Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "verification mismatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200
    
    
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
                        
                    #Echo
                    response = messaging_text
                    bot.send_text_message(sender_id, response)
    
    return "OK", 200
    
def log(message):
    pring(message)
    sys.stdout.flush()

    
if __name__ == "__main__":
    app.run(debug = True, port = 80)