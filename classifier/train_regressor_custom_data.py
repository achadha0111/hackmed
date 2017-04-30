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
from keras import optimizers

# df = pd.read_csv("data/labeled_train.csv", index_col=0)

# data = df.values
# X_train = data[:,0:-3]
# y_train = data[:,-1] # UPDRS
# one_hot = []

# patient_1 = np.load("npyarrs/1.npy")
# patient_2 = np.load("npyarrs/1.npy")
# patient_6 = np.load("npyarrs/1.npy")
# patient_7 = np.load("npyarrs/1.npy")
# patient_8 = np.load("npyarrs/1.npy")
# patient_9 = np.load("npyarrs/1.npy")
# patient_10 = np.load("npyarrs/1.npy")
# patient_11 = np.load("npyarrs/1.npy")
# patient_12 = np.load("npyarrs/1.npy")
# patient_13 = np.load("npyarrs/1.npy")
# patient_14 = np.load("npyarrs/1.npy")
# patient_16 = np.load("npyarrs/1.npy")
# patient_17 = np.load("npyarrs/1.npy")
# patient_18 = np.load("npyarrs/1.npy")
# patient_19 = np.load("npyarrs/1.npy")
# patient_25 = np.load("npyarrs/1.npy")
# patient_26 = np.load("npyarrs/1.npy")
# patient_27 = np.load("npyarrs/1.npy")
# patient_28 = np.load("npyarrs/1.npy")

# X_train = np.stack((patient_1, patient_2, patient_6, patient_7,patient_8,patient_9,patient_10,patient_11,patient_12,patient_13,patient_14,patient_16,patient_17, patient_18,patient_19,patient_25,patient_26,patient_27,patient_28), axis=0)

# X_train = X_train.reshape(len(X_train),25)

# np.save("npyarrs/train_arr.npy", X_train)

X_train = np.load("../npyarrs/train_arr.npy")

y_train = np.array([[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,1],[0,1],[0,1],[0,1]])


NUM_FEATURES = X_train.shape[1]

model = Sequential()
model.add(Dense(NUM_FEATURES,input_dim=NUM_FEATURES,init='glorot_normal', activation='sigmoid'))
model.add(Dense(300,init='glorot_normal', activation='sigmoid'))
model.add(Dense(2,init='glorot_normal', activation='softmax'))
optimizer=optimizers.SGD(lr=1e-7, decay=1e-6, momentum=0.9)
model.compile(loss='binary_crossentropy', optimizer=optimizer)


model.fit(X_train, y_train, nb_epoch=20000, batch_size=19,verbose=1)

# serialize model to JSON and save structure
model_json = model.to_json()
with open("../models/model.json", "w") as json_file:
    json_file.write(model_json)

# save weights of network
model.save_weights("../models/model.h5")

