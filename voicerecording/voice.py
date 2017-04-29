import os
from flask import Flask, request, Response, jsonify
import json
import nexmo
import sys
import requests

#db62889d
#3b06d19d574b099d
#60315a7f-fb0b-4046-a82e-70668ca83e1a

app = Flask(__name__)

@app.route('/recordvoice', methods=['POST'])
def inbound():
    print ('')
    try:
        nexmo_response = request.get_json()
        for key, value in nexmo_response.items() :
            if (key == 'recording_url'):
                getFile(value, 'patient_audio_recording.mp3')

    except Exception as e:
        print (e)

    return Response(), 200

@app.route('/ncco', methods=['GET'])
def requestNCCO():
    NCCO = [
                {
                    "action": "talk",
                    "text": "You have reached the Mobile Parkinson's Diagnostic Service. Please say the vowel O continuously for 3 seconds after the beep ",
                    "voiceName": "Emma"
                },
                {
                    "action": "record",
                    "eventUrl": [
                        "https://7bab0845.ngrok.io/recordvoice"
                    ],
                    "endOnSilence": "3",
                    "endOnKey" : "#",
                    "beepStart": "true"
                },
                {
                    "action": "talk",
                    "text": "Thank you. Your diagnostic information will be sent to your phone and your G P shortly.",
                    "voiceName": "Emma"
                }
            ]

    return Response(json.dumps(NCCO), mimetype='application/json')

@app.route('/', methods=['GET'])
def test():
    return Response('It works')

def getFile(url, filename):
    fp = open('private.key')
    contents = fp.read()
    client = nexmo.Client(application_id='ede20e77-cb73-4829-a6b9-576af0cc73b1', private_key=contents,key='db62889d', secret='3b06d19d574b099d')
    headers =  client._Client__headers()
    headers['Content-Type'] = 'application/json'
    response = requests.get(url, headers=headers)
    if response.status_code ==200:
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        print (response.content)

if __name__ == "__main__":
    app.run(debug=True)

