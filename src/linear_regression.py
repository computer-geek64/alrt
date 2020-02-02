import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import math
from numpy import genfromtxt
import pandas as pd
import matplotlib.pyplot as plt

def predictPoint(latitudes, longitudes, radius):
    X = tf.placeholder("float")
    Y = tf.placeholder("float")

    W = tf.Variable(np.random.randn, name = 'W') #weight variable
    b = tf.Variable(np.random.randn, name = 'b')  #bias variable

    learning_rate = 0.01
    epochs = 1000
    n = len(latitudes)

    #Hypothesis or equation
    y_pred = tf.add(tf.multiply(X,W), b)

    #mean squared error cost function
    cost = tf.reduce_mean(tf.pow(y_pred-Y, 2)) / (2*n)

    #gradient descent optimizer
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

    with tf.Session() as session:

        session.run(tf.global_variables_initializer())

        for epoch in range(epochs):

            for(x,y) in zip(latitudes,longitudes):
                session.run(optimizer, feed_dict= {X:x, Y:y})
            if (epoch+1) % 50 == 0:
                c = session.run(cost, feed_dict={X:latitudes, Y:longitudes})
                print("Epoch: ", epoch+1, "cost: ", c, "W: ", session.run(W), "b: ", session.run(b))

        training_cost = session.run(cost, feed_dict={X:latitudes, Y:longitudes})
        weight = session.run(W)
        bias = session.run(b)

    latest_predicted_location = latitudes[-1]*weight+bias
    print(latitudes[-1], latest_predicted_location)
    # x= latitudes
    # y = latitudes*weight+bias
    # plt.scatter(x,y)
    # plt.show()
    degrees_of_latlong = radius/69.172
    change_in_y = math.sqrt((degrees_of_latlong)**2 / (1+(1/(weight**2))))
    change_in_x = change_in_y / weight
    if (latitudes[0] < latitudes[-1]):
        new_latitude = latitudes[-1] + change_in_x
    else:
        new_latitude = latitudes[-1] - change_in_x
    if (longitudes[0] < longitudes[-1]):
        new_longitude = longitudes[-1] + change_in_y
    else:
        new_longitude = longitudes[-1] - change_in_y
    return [new_latitude, new_longitude]

latitudes = np.array([29.652106, 29.652106, 29.652109, 29.652118, 29.652082, 29.652133, 29.652146, 29.652155, 29.652158, 29.652152, 29.652146, 29.652149, 29.652142, 29.652063, 29.652194])
longitudes = np.array([-82.350011, -82.350116, -82.350281, -82.35047, -82.350606, -82.350788, -82.350928, -82.351026, -82.351229, -82.351397, -82.351572, -82.351733, -82.35188, -82.352135, -82.352328])
plt.scatter(latitudes, longitudes)
point = predictPoint(latitudes, longitudes, 0.5)
plt.scatter(point[0], point[1])
plt.show()
print(point)