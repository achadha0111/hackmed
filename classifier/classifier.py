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

# load json and create model
json_model = open('model_binary.json', 'r')
loaded_model_json = json_model.read()
json_model.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("model_binary.h5")
print("Loaded model from disk")
 
# evaluate loaded model on test data
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
# score = model.evaluate(X_test, Y_test, verbose=1)

def classify(feature_vector):
	# returns probability of parkinsons
	return model.predict(feature_vector)[0]