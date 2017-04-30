import nexmo
import array
a=['447435804721']


def sendSms(has_parkinsons, feature_vectors):
    print (feature_vectors)
    feature_vectors = [item for sublist in feature_vectors for item in sublist]
    messageString = """ Probability of Parkinsons:{parkinson_probability} 
    Jitter (local):{l_jitter}
    Jitter (local, absolute):{la_jitter}
    Jitter (rap):{rap_jitter}
    Jitter (ppq5):{ppq5_jitter}
    Jitter (ddp):{ddp_jitter}
    Shimmer (local):{local}
    Shimmer (local, dB):{dB_local}
    Shimmer (apq5):{apq5}
    Shimmer (apq11):{apq11}
    Shimmer (dda):{dda}
    Mean autocorrelation:{mat}
    Mean noise-to-harmonics ratio:{nth}
    Mean harmonics-to-noise ratio:{htn}
    Median pitch:{mp}
    Mean pitch:{mean_pitch}
    Standard deviation:{sd}
    Minimum pitch:{minp}
    Maximum pitch:{maxp}
    Number of periods:{nop}
    Mean period:{mep}
    Standard deviation of period:{sdp}
    Fraction of locally unvoiced frames:{luf}
    Number of voice breaks:{numVoiceBreaks}
    Degree of voice breaks:{degVoiceBreaks}
    """.format(parkinson_probability=has_parkinsons[0], l_jitter=feature_vectors[0], la_jitter=feature_vectors[1], rap_jitter=feature_vectors[2], ppq5_jitter=feature_vectors[3],ddp_jitter=feature_vectors[4], local=feature_vectors[5], dB_local=feature_vectors[6], apq5=feature_vectors[7], apq11=feature_vectors[8], dda=feature_vectors[8],mat=feature_vectors[9],nth=feature_vectors[10],htn=feature_vectors[11],mp=feature_vectors[12],mean_pitch=feature_vectors[13],sd=feature_vectors[14],minp=feature_vectors[15],maxp=feature_vectors[16],nop=feature_vectors[17],mep=feature_vectors[18],sdp=feature_vectors[19],luf=feature_vectors[20],numVoiceBreaks=feature_vectors[21],degVoiceBreaks=feature_vectors[22])


    client = nexmo.Client(key='db62889d', secret='3b06d19d574b099d')
    print ('Sending message now')
    for number in a:
        client.send_message({'from' : '447520619351', 'to' : number, 'text' : messageString})
    

    return True
    '''response = 

    response = response['messages'][0]

    if response['status'] == '0':
        print 'Sent message ', response['message-id']
    else:
        print 'Error: ', response['error-text']'''
  
#sevLevel("0.3")