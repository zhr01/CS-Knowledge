from keras.layers import Dense
from keras.models import Sequential
import numpy as np

def create_model():
    model = Sequential()
    model.add(Dense(3, input_shape=(3,), activation='relu'))
    model.add(Dense(3, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='rmsprop', loss='mse')
    return model

def crate_data():
    a1,a2,a3 = 1,1,1
    number = 1000
    x1 = np.random.rand(number,) * 100 + 100
    x2 = np.random.rand(number,) * 50 + 50
    x3 = np.random.rand(number,) * 1

    y = a1*x1 + a2*x2 + a3*x3 + np.random.randn(number,)*5
    x_train = np.array([x1,x2,x3]).T
    y_train = y
    print(x_train.shape, y_train.shape)

    return x_train, y_train

model = create_model()
x_train, y_train = crate_data()

model.fit(x_train, y_train,
          epochs=100,
          validation_split=0.1)