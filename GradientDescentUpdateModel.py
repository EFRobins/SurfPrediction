import sqlite3
from GradientDescent import find_cost, update_gradient, update_bias, deriv_weight, derivative_bias, cleanlist


def renew_gradientdescent():
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    Y = list(c.execute("SELECT swellHeight_m FROM `Historical Data`"))
    X = list(c.execute("SELECT windspeedKmph FROM `Historical Data`"))

    Y = cleanlist(Y)
    X = cleanlist(X)

    gradient = 1
    bias = 1
    lr = 0.0001
    epochs = 10000
    # 0.0001

    for i in range(epochs):
        cost = find_cost(X, Y, gradient, bias)
        if abs(cost) <= 0.001:
            break
        else:
            dB = derivative_bias(X, Y, gradient, bias)
            dW = deriv_weight(X, Y, gradient, bias)
            bias = update_bias(bias, lr, dB)
            gradient = update_gradient(gradient, lr, dW)
    return gradient, bias


def predict_gradientdescent(WindSpeed):
    gradient, bias = renew_gradientdescent()
    return WindSpeed * gradient + bias
