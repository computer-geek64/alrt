import tensorflow as tf
import numpy as np
import math

def predictPoint(latitudes, longitudes, radius):
    X = tf.placeholder("float")
    Y = tf.placeholder("float")

    W = tf.Variable(np.random.randn, name = 'W') #weight variable
    b = tf.Variable(np.randm.randn, name = 'b')  #bias variable

    learning_rate = 0.001
    epochs = 1000
    n = 30

    #Hypothesis or equation
    y_pred = tf.add(tf.multiply(X,W), b)

    #mean squared error cost function
    cost = tf.reduce_sum(tf.pow(y_pred-longitudes, 2) / 2*n)

    #gradient descent optimizer
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

    #global variable initializer
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)

        for epoch in range(epochs):

            for(x,y) in zip(latitudes,longitudes):
                sess.run(optimizer, feed_dict= {X:x, Y:y})

            if (epoch+1 % 50 == 0):
                c = sess.run(cost, feed_dict={X:latitudes, Y:longitudes})
                print("Epoch: ", epoch+1, "cost: ", cost, "W: ", sess.run(W), "b: ", sess.run(b))

        training_cost = sess.run(cost, feed_dict={X:x, Y:y})
        print(training_cost)
        weight = sess.run(W)
        bias = sess.run(b)

    latest_predicted_location = latitudes[29]*weight+bias
    degrees_of_latlong = radius/69.172
    change_in_y = math.sqrt(radius**2 / (1+(1/(weight**2))))
    change_in_x = change_in_y / weight
    if (latitudes[0] < latitudes[29]):
        new_latitude = latitudes[29] + change_in_x
    else:
        new_latitude = latitudes[29] - change_in_x
    if (longitudes[0] < longitudes[29]):
        new_longitude = longitudes[29] + change_in_y
    else:
        new_longitude = longitudes - change_in_y
    return [new_latitude, new_longitude]
