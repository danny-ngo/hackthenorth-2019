import os, sys
from flask import Flask, request, jsonify, Response
from pymessenger import Bot
import requests
import json
import uuid
from utils import create_buttons, create_quick_replies
from flask_pymongo import PyMongo
import pymongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

''' Setup mongoDB '''
app.config['MONGO_DBNAME'] = 'AdAR'
app.config['MONGO_URI'] = 'mongodb+srv://danny:567693@cluster0-eg553.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)

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
                        
                    bot.send_text_message(sender_id, messaging_text)
                    
                elif messaging_event.get('postback'):
                    mongo.db.user_ratings.find_one_and_update({"uuid": messaging_event['postback']['payload']}, 
                        {"$set": {"isRated": True, "rating": messaging_event['postback']['title']}})
                                     
    return "OK", 200
    
def log(message):
    print(message)
    sys.stdout.flush()
    
    
@app.route('/purchased', methods=['POST'])
def sendButtons():
    searchToken = str(uuid.uuid4())
    body = str(request.stream.read())
    #print(body.split("lat="))
    '''
    split_1 = body.split("&")
    print(split_1)
    lat_val = split_1[0].split("=")[1]
    lon_val = split_1[1].split("=")[1]
    weather_val = split_1[2].split("=")[1]
    food = split_1[3].split("=")[1]
    
    payload = {
        "latitude": float(lat_val), 
        "longitude": float(lon_val), 
        "weather": weather_val, 
        "food": food 
    }
    '''
    payload = jsons.loads(body.decode('utf-8'))
    #payload = request.get_json()
    payload.update({'isRated': False, 'uuid': searchToken})
    mongo.db.user_ratings.insert_one(payload)
    
    text = "How was your experience today?"
    buttons = create_buttons(searchToken)
    bot.send_button_message('2470284623018202', text, buttons)
    
    return "OK", 200
    

@app.route('/data', methods=['GET'])
def getData():
    output = mongod.db.user_ratings.find()
    return Response(json_util.dumps(output), mimetype='application/json')  

    
if __name__ == "__main__":
    app.run(debug = True, port = 80)