# John Vogel 02/28/2025 john.vogel123@gmail.com

#MNIST code comes from here
#https://www.kaggle.com/code/ashishk1331/mnist-dataset?scriptVersionId=224441574&cellId=3

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import struct

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

#for dirname, _, filenames in os.walk('/kaggle/input'):
for dirname, _, filenames in os.walk('/home/jvogel/Documents/aiWorkrepo/mnistWork/data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

def read_idx(filename):
    with open(filename, 'rb') as f:
        zero, dtype, dims = struct.unpack('>HBB', f.read(4))
        shape = tuple(struct.unpack('>I', f.read(4))[0] for _ in range(dims))
        return np.frombuffer(f.read(), dtype=np.uint8).reshape(shape)

# Load the training images and labels
train_images_file = '../data/train-images.idx3-ubyte'
train_labels_file = '../data/train-labels.idx1-ubyte'

train_images = read_idx(train_images_file)
train_labels = read_idx(train_labels_file)

# Flatten the images (important for using them in many machine learning models)
num_samples = train_images.shape[0]
image_size = train_images.shape[1] * train_images.shape[2]
train_images_flat = train_images.reshape(num_samples, image_size)

# Create Pandas DataFrames
train_images_df = pd.DataFrame(train_images_flat)
train_labels_df = pd.DataFrame(train_labels, columns=['label'])  # Give the label column a name
# Combine into a single DataFrame (optional but often useful)
train_df = pd.concat([train_images_df, train_labels_df], axis=1)

# Now you can work with the DataFrames
print(train_df.head()) # Print the first few rows
print(train_df.shape)  # Print the shape of the DataFrame


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

random_state = 42

X = train_df.drop('label', axis=1).values
y = pd.get_dummies(train_df['label'], dtype=int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=random_state)

inp_shape = X.shape[1]
out_shape = y.shape[1]

nodes = 300
layers = 3

model = Sequential()
model.add(Input(shape=(inp_shape, )))

for _ in range(layers):
    model.add(Dense(nodes, activation="relu"))

model.add(Dense(out_shape, activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy'])

model.fit(X_train, y_train, validation_split=.2)

model.summary()

y_pred = model.predict(X_test)

predicted_labels = np.argmax(y_pred, axis=1)
test_labels = np.argmax(y_test, axis=1)

print(classification_report(test_labels, predicted_labels))

