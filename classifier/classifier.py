import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.models import model_from_json
from extract_features import extract_features
from sms import sendSms
from keras import optimizers

# load json and create model
json_model = open('../models/model.json', 'r')
loaded_model_json = json_model.read()
json_model.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("../models/model.h5")
print("Loaded model from disk")
 
optimizer=optimizers.SGD(lr=1e-7, decay=1e-6, momentum=0.9)
# evaluate loaded model on test data
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])


def classify():

	payload_vector = extract_features()

	# for i in feature_vector:
	# 	print(i)
	# for j in payload_vector:
	# 	print(j)
		
	# returns probability of parkinsons

	# print("Our extracted feature prediction")
	print("Prediction: " + str(model.predict(payload_vector)))

	# print("Our extracted feature prediction")
	predictions = model.predict(payload_vector)
	# print (predictions)
	diagnostic_information = {}
	diagnostic_information['probability_has_parkinsons'] = predictions[0]
	diagnostic_information['voice_features'] = payload_vector
	return diagnostic_information

# classify()
patient_features = classify()

sendSms(patient_features['probability_has_parkinsons'], patient_features['voice_features'])

print ('Fin')
