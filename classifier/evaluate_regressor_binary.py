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

df = pd.read_csv("data/labeled_test.csv", index_col=0)

data = df.values

X_test = data[:,0:-2]
# y_test = data[:,-1] # UPDRS

NUM_FEATURES = X_test.shape[1]

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

# each test subject has 6 voice samples, so average over these to obtain prediction
UPDRS_predictions = model.predict(X_test, batch_size=6, verbose=1)

# print(UPDRS_predictions)

correct_pred = 0

for i in range(len(UPDRS_predictions)):
	if UPDRS_predictions[i][0] > 0.5:
		correct_pred+=1

print(correct_pred)
print("Accuracy = {}".format(correct_pred/len(UPDRS_predictions)))

hard_code = np.array([0.792,0.000076198,0.411,0.333,1.234,4.136,0.391,2.202,2.552,3.181,6.607,0.972431,0.035008,18.596,103.774,103.862,1.73,98.743,110.597,147,146,0.009623447,0.000203128,0,0])
hard_code = hard_code.reshape(1, hard_code.shape[0])
print(hard_code.shape)
print("Prediction PWOP: {}".format(model.predict(hard_code)))

def classify(feature_vector):
	# returns probability of parkinsons
	return model.predict(feature_vector)[0]


# model.fit(X_train, y_train, nb_epoch=1, batch_size=26,verbose=1)
# score = model.evaluate(X_test, y_test, batch_size=16)
