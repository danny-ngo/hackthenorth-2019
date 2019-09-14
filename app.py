import os, sys
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = 'EAANmy13IMxMBAOIO5K337zhxM4hZAV3ZAexUt1vCweZCPDkLxwjWcKBYrCjIKB9GqgozOg9DlxlrjBqTFYl54dS3YBan3FZBCSJWulXIBOQoxZBMBcEoMyzyZCgM8WRlqSfFcuoqZAkykFEFOBVcEFPd0G2Da3XDdE6i797ZAYVz7u6Xts9x0Jay'

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
                    response = [{
                        'title': messaging_text,
                        'buttons': [
                            {
                                'type': 'web_url',
                                'title': '1',
                                'url': 'https://www.google.ca'
                            },
                            {
                                'type': 'web_url',
                                'title': '2',
                                'url': 'https://www.google.ca'
                            },
                            {
                                'type': 'web_url',
                                'title': '3',
                                'url': 'https://www.google.ca'
                            },
                            {
                                'type': 'web_url',
                                'title': '4',
                                'url': 'https://www.google.ca'
                            },
                            {
                                'type': 'web_url',
                                'title': '5',
                                'url': 'https://www.google.ca'
                            }
                        ]
                    }]
                    bot.send_text_message(sender_id, response)
    
    return "OK", 200
    
def log(message):
    print(message)
    sys.stdout.flush()

    
if __name__ == "__main__":
    app.run(debug = True, port = 80)