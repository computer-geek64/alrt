#!/usr/bin/python3
# predict.py

import geopy.distance
import tensorflow as tf
import numpy as np
import statistics
from sympy import Symbol
from sympy.solvers import solve


def predict_point(x_data, y_data, radius, disaster_coords):
    x_data = np.array(x_data)
    y_data = np.array(y_data)

    x = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32)

    w = tf.Variable(np.random.randn(), name="W")
    b = tf.Variable(np.random.randn(), name="b")

    learning_rate = 0.0001
    epochs = 1000

    # Hypothesis
    hypothesis = tf.add(tf.multiply(x, w), b)

    # Mean squared error cost function
    cost = tf.reduce_sum(tf.pow(hypothesis - y, 2)) / (2 * len(x_data))

    # Gradient Descent Optimizer
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

    # Global variables initializer
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)

        for epoch in range(epochs):
            for (_x, _y) in zip(x_data, y_data):
                sess.run(optimizer, feed_dict={x: _x, y: _y})

            if (epoch + 1) % 50 == 0:
                c = sess.run(cost, feed_dict={x: x_data, y: y_data})

        training_cost = sess.run(cost, feed_dict={x: x_data, y: y_data})
        weight = sess.run(w)
        bias = sess.run(b)

    print(weight)
    print(bias)
    var = Symbol("x")
    results = solve((var - x_data[-1]) ** 2 + (weight * var + bias - y_data[-1]) ** 2 - radius ** 2, var)
    distances = [geopy.distance.distance((x_data[0], y_data[0]), (x, weight * x + bias)).mi for x in results]
    if distances[0] > distances[1]:
        predicted_regression_point = (float(results[0]), float(weight * results[0] + bias))
    else:
        predicted_regression_point = (float(results[1]), float(weight * results[1] + bias))

    print(disaster_coords)
    print(y_data[-1])
    print(x_data[-1])
    m = (disaster_coords[1] - y_data[-1]) / (disaster_coords[0] - x_data[-1])
    b = y_data[-1] - m * x_data[-1]
    var = Symbol("x")
    results = solve((var - x_data[-1]) ** 2 + (m * var + b - y_data[-1]) ** 2 - radius ** 2, var)
    distances = [geopy.distance.distance(disaster_coords, (x, m * x + b)).mi for x in results]
    if distances[0] > distances[1]:
        predicted_disaster_point = (float(results[0]), float(m * results[0] + b))
    else:
        predicted_disaster_point = (float(results[1]), float(m * results[1] + b))
    return statistics.mean((predicted_regression_point[0], predicted_disaster_point[0])), statistics.mean((predicted_regression_point[1], predicted_disaster_point[1]))


#latitudes = np.array([1, 2, 3, 4, 5, 6, 7])
#longitudes = np.array([1, 2, 3, 4, 5, 6, 7])

#print(predict_point(latitudes, longitudes, 1.41, (10, 4)))