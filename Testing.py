import sqlite3

from GradientByHand import renew_lrbyhand
from GradientDescentUpdateModel import renew_gradientdescent
from MultiScikit import renew_multivariate
import pandas as pd
from pandas import DataFrame

m = round(float(input(" gradient ")), 2)
m1 = round(float(input(" gradient ")), 2)
c = round(float(input("intercept")), 2)
xval, y, z = [], [], []
for x in range(35):
    equation = m * x + m1 * x + c
    y.append(equation)
    z.append(x)
    xval.append(x)

dependants = DataFrame({'x': xval, 'z': z})
regr = renew_multivariate(dependants,y)
print(regr.coef_, regr.intercept_)
