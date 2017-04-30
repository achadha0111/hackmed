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

# load json and create model
json_model = open('../models/model_binary.json', 'r')
loaded_model_json = json_model.read()
json_model.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("../models/model_binary.h5")
print("Loaded model from disk")
 
# evaluate loaded model on test data
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
# score = model.evaluate(X_test, Y_test, verbose=1)

np.set_printoptions(precision=15)
np.set_printoptions(linewidth=232)

def classify():

	feature_vector = np.array([0.1350000,0.0000073,0.0670000,0.0780000,0.2020000,2.0330000,0.1780000,1.0740000,1.3360000,1.5760000,3.2230000,0.9960500,0.0039670,24.2040000,186.2660000,186.3000000,0.8590000,184.5020000,187.8800000,183.0000000,182.0000000,0.0053680,0.0000255,0.0000000,0.0000000]).reshape(1,25)
	feature_vector_custom = extract_features()

	for i in feature_vector:
		print(i)
	for j in feature_vector_custom:
		print(j)
		
	# returns probability of parkinsons
<<<<<<< HEAD:classifier.py
	# print("Our extracted feature prediction")
	print(model.predict(feature_vector_custom))
=======
	print("Our extracted feature prediction")
	predictions = model.predict(feature_vector)
	print (predictions)
	diagnostic_information = {}
	diagnostic_information['probability_has_parkinsons'] = predictions[0]
	diagnostic_information['voice_features'] = feature_vector
	return diagnostic_information
>>>>>>> 2a0638707897cbbf4f7bd1d4b8bb0663fe0f5d4e:classifier/classifier.py

patient_features = classify()

sendSms(patient_features['probability_has_parkinsons'], patient_features['voice_features'])

print ('Fin')
