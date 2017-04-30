import os
from flask import Flask, request, Response, jsonify
import json
import nexmo
import sys
import requests

app = Flask(__name__)

@app.route('/recordvoice', methods=['POST'])
def inbound():
    print ('something')
    try:
        nexmo_response = request.get_json()
        for key, value in nexmo_response.items() :
            if (key == 'recording_url'):
                print (value)
                getFile(value, 'patient_audio_recording.mp3')
        print ('Calling classifier', file=sys.stderr)
        os.system('python3 ../classifier/classifier.py')
       
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
                        "https://802f0353.ngrok.io/recordvoice"
                    ],
                    "format": "wav",
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
    print ('GET FILE CALLED')
    fp = open('private.key')
    contents = fp.read()
    client = nexmo.Client(application_id='45214214-8f58-4625-979f-cc6b3d8498d9', private_key=contents,key='a7c77f17', secret='14200a2d041b524c')
    headers =  client._Client__headers()
    headers['Content-Type'] = 'application/json'
    response = requests.get(url, headers=headers)
    if response.status_code ==200:
        with open(filename, 'w+') as f:
            f.write(response.content)
            print ('Wrote file')
    else:
        print (response.content)

if __name__ == "__main__":
    app.run(debug=True)

