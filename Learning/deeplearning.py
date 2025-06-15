import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_diabetes
import tensorflow as tf

X, y_numeric = load_diabetes(return_X_y=True)

y = np.array([ 0 if y_numeric[i]<140 else 1 for i in range(len(y_numeric)) ])
xtrain, xtest, ytrain, ytest = train_test_split(X,y,test_size=0.4,random_state=42)

f = MLPClassifier(
        hidden_layer_sizes = (10,5),
        activation = 'logistic',
        solver = 'lbfgs',
        alpha = 0.01,
        batch_size = 'auto',
        learning_rate = 'constant',
        learning_rate_init = 0.001,
        random_state = 0,
        max_iter = 10000)

f.fit(xtrain,ytrain)
print( f.score(xtrain,ytrain), f.score(xtest,ytest) )

model = tf.keras.models.Sequential()
model.add( tf.keras.layers.Input(shape=(10,)) )
model.add( tf.keras.layers.Dense(10,activation='sigmoid') )
model.add( tf.keras.layers.Dense(5,activation='sigmoid') )
model.add( tf.keras.layers.Dense(2,activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(xtrain,ytrain,epochs=5)
model.fit(xtrain,ytrain,epochs=1000)
model.fit(xtrain,ytrain,epochs=5)

model.summary()

print(xtrain[0])

model.predict(xtrain[[0]])

model.evaluate(xtrain,ytrain)
model.evaluate(xtest,ytest)