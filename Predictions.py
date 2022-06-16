from GradientByHand import predict_lrbyhand, renew_lrbyhand
from GradientDescentUpdateModel import predict_gradientdescent, renew_gradientdescent
from MultiScikit import predict_multivariate, renew_multivariate
from MagicSeaweed import get_msw
import _sqlite3


# output from get_msw is in form [(timestamp,height,windspeed,dir)]
# database structure is Timestamp, MSW, GD, MV, BH


def sqlinsertA(values, c, conn):
    c.execute('INSERT INTO PredictionsA(Timestamp,MagicSeaWeed,GradientDescent,MultiVariate,ByHand) VALUES(?,?,?,?,?)',
              values)
    conn.commit()


def sqlinsertM(values, c, conn):
    c.execute('INSERT INTO PredictionsM(Timestamp,MagicSeaWeed,GradientDescent,MultiVariate,ByHand) VALUES(?,?,?,?,?)',
              values)
    conn.commit()


def filltable(location):
    conn = _sqlite3.connect('Predictions.db')
    c = conn.cursor()
    if location == 557:
        c.execute('DELETE FROM PredictionsA')
    elif location == 899:
        c.execute('DELETE FROM PredictionsM')
    gdGradient, gdBias = renew_gradientdescent()
    bhGradient, bhBias = renew_lrbyhand()
    for i in get_msw(location):
        row = ((i[0])[:4] + (i[0])[12:16] + "h", i[1],
               round(gdGradient * i[2] + gdBias, 3), round(predict_multivariate(i[2], i[3], renew_multivariate()), 3)
               , round(bhGradient * i[2] + bhBias, 3))
        if location == 557:
            sqlinsertA(row, c, conn)
        elif location == 899:
            sqlinsertM(row, c, conn)


filltable(557)
filltable(899)
