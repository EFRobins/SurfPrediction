import sqlite3
from GradientDescent import cleanlist


def renew_lrbyhand():
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    Y = list(c.execute("SELECT swellHeight_m FROM `Historical Data`"))
    X = list(c.execute("SELECT windspeedKmph FROM `Historical Data`"))

    Y = cleanlist(Y)
    X = cleanlist(X)

    sigmaY = sum(Y)
    sigmaX = sum(X)
    n = len(X)

    X_sqr = 0
    for i in X:
        X_sqr += i ** 2

    XY = 0
    for i in range(n):
        XY += X[i] * Y[i]

    intercept = (sigmaY * X_sqr - sigmaX * XY) / (n * X_sqr - sigmaX ** 2)
    slope = (n * XY - sigmaX * sigmaY) / (n * X_sqr - sigmaX ** 2)
    return intercept, slope


def predict_lrbyhand(WindSpeed):
    intercept, gradient = renew_lrbyhand()
    return WindSpeed * gradient + intercept
