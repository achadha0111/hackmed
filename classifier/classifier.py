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

def classify():
	feature_vector_custom = extract_features()
	feature_vector = np.array([0.1350000,0.0000073,0.0670000,0.0780000,0.2020000,2.0330000,0.1780000,1.0740000,1.3360000,1.5760000,3.2230000,0.9960500,0.0039670,24.2040000,186.2660000,186.3000000,0.8590000,184.5020000,187.8800000,183.0000000,182.0000000,0.0053680,0.0000255,0.0000000,0.0000000]).reshape(1,25)
	print(feature_vector)
	print(feature_vector_custom)
	# returns probability of parkinsons
	print("Our extracted feature prediction")
	print(model.predict(feature_vector_custom))

classify()