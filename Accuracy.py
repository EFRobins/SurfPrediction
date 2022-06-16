import _sqlite3

# database structure is Timestamp, MSW, GD, MV, BH
from math import sqrt


def Acc():
    conn = _sqlite3.connect('Predictions.db')
    c = conn.cursor()
    c.execute("SELECT * FROM PredictionsM INNER JOIN PredictionsA PA on PredictionsM.Timestamp = PA.Timestamp")
    rows = c.fetchall()
    vals = []
    for x in range(1, 4):
        total_e = 0
        for i in rows:
            total_e += abs((i[1] - i[x + 1]) / i[1]) * 100 and abs((i[1] - i[x + 6]) / i[1]) * 100
        vals.append(total_e / 80)
    return vals


"""
def SD():
    conn = _sqlite3.connect('Predictions.db')
    c = conn.cursor()
    c.execute("SELECT * FROM PredictionsM INNER JOIN PredictionsA PA on PredictionsM.Timestamp = PA.Timestamp")
    rows = c.fetchall()
    Sum_X = 0
    xSqr = 0
    for i in rows:
        Sum_X += i[2] + i[3] + i[4] + i[7] + i[8] + i[9]
        xSqr += i[2] ** 2 + i[3] ** 2 + i[4] ** 2 + i[7] ** 2 + i[8] ** 2 + i[9] ** 2
    f = len(rows) * 6
    mean = Sum_X / f
    Standard_d = sqrt(abs(((xSqr * f) / f) - ((Sum_X * f / f) ** 2)))
    deviation = 0
    for i in rows:
        deviation += i[2] + i[3] + i[4] + i[7] + i[8] + i[9]

    return mean, deviation, Sum_X, f, mean * f, Standard_d

"""