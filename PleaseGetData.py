import sqlite3
from GetData import request_data

start_date = "2016-01-01"
stop_date = "2016-01-20"


def insert_historical_data(start_date, stop_date):
    data_list = request_data(start_date, stop_date)
    print(data_list)
    # swellHeight_m, windspeedKmph, swellDir, winddirDegree

    conn = sqlite3.connect("Database.db")
    c = conn.cursor()
    for i in range(len(data_list)):
        x = data_list.pop()
        try:
            c.execute("INSERT INTO `Historical Data`(Date,swellHeight_m,windspeedKmph,winddirDegree) VALUES (?,?,?,?)",
                      (x[0], x[1], x[2], x[3]))
        except IndexError:
            continue
    conn.commit()
