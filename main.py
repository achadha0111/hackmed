import nexmo
import array
a=['447463616735', '447397333232']


def sevLevel(level):

    client = nexmo.Client(key='db62889d', secret='3b06d19d574b099d')
    for number in a:
        client.send_message({'from' : '447520619351', 'to' : number, 'text' : 'PATIENT REPORT NR.3. VOICE TEST COMPLETED. THIS IS THE LEVEL OF SEVERITY: ' + level})

    '''response = 

    response = response['messages'][0]

    if response['status'] == '0':
        print 'Sent message ', response['message-id']
    else:
        print 'Error: ', response['error-text']'''

sevLevel("0.3")