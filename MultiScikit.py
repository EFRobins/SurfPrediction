import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression




def renew_multivariate():
    conn = sqlite3.connect('Database.db')
    df = pd.read_sql_query('SELECT * FROM `Historical Data`', conn)
    X = df[['windspeedKmph', 'winddirDegree']]
    Y = df['swellHeight_m']

    regr = LinearRegression().fit(X, Y)
    regr.fit_intercept = True
    regr.fit(X, Y)

    return regr


def predict_multivariate(WindSpeed, WindDir, regr):
    # prediction with sklearn
    NewWindSpeedKmph = WindSpeed
    NewWindDir = WindDir
    x = regr.predict([[NewWindSpeedKmph, NewWindDir]])
    x = x[0]

    return x
