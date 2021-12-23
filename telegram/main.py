from flask import Flask, request
import os, requests, random

app = Flask(__name__)

URL = f'https://api.telegram.org/bot{TOKEN}/'
TOKEN = os.getenv('TOKEN', '')
CHAT_ID = os.getenv('CHAT_ID', '')
message_type_list = ['sendMessage', 'sendPhoto']

@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    response = request.get_json()

    text = response['message'].get('text')
    photo = response['message'].get('photo')
    location = response['message'].get('location')

    if text:
        send_message(message_type_list[0], text)
    elif photo:
        send_message(message_type_list[1])
    elif location:
        print("Location")
    
    return '', 200

def send_message(message_type, value=''):
    if message_type == message_type_list[0]:
        text = 'Text 확인'
        params = {
            'chat_id': CHAT_ID,
            'text': text,
        }
        requests.get(URL + message_type, params=params)
    elif message_type == message_type_list[1]:
        print("Photo")

@app.route("/")
def index():
    return 'Test'

app.run(host=os.getenv('IP','localhost'), port=int(os.getenv('PORT', 5000)))