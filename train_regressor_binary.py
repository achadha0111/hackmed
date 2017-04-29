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

df = pd.read_csv("data/labeled_train.csv", index_col=0)

data = df.values
X_train = data[:,0:-3]
y_train = data[:,-1] # UPDRS
one_hot = []

for label in y_train:
	if label == 0:
		one_hot.append([0,1])
	elif label == 1:
		one_hot.append([1,0])

one_hot = np.array(one_hot)

NUM_FEATURES = X_train.shape[1]

model = Sequential()
model.add(Dense(NUM_FEATURES,input_dim=NUM_FEATURES,init='normal', activation='relu'))
model.add(Dense(100,init='normal', activation='relu'))
model.add(Dense(2,init='normal', activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam')

model.fit(X_train, one_hot, nb_epoch=1000, batch_size=26,verbose=1)

# serialize model to JSON and save structure
model_json = model.to_json()
with open("model_binary.json", "w") as json_file:
    json_file.write(model_json)

# save weights of network
model.save_weights("model_binary.h5")

