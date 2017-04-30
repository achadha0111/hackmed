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
from keras import optimizers

# load json and create model
json_model = open('model_binary_our_features.json', 'r')
loaded_model_json = json_model.read()
json_model.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("model_binary_our_features.h5")
print("Loaded model from disk")
 
optimizer=optimizers.SGD(lr=1e-7, decay=1e-6, momentum=0.9)
# evaluate loaded model on test data
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
# score = model.evaluate(X_test, Y_test, verbose=1)


def classify():

	feature_vector_custom = extract_features()

	for j in feature_vector_custom:
		print(j)
		
	# returns probability of parkinsons
	# print("Our extracted feature prediction")
	print(model.predict(feature_vector_custom))

classify()