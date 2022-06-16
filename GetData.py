from datetime import datetime
from datetime import timedelta
import requests


# 897d3a412b1b4c6c8ca73939191911
# c44f34a43a754886ac080746191911
# 48a6ec88eef9463689062741190711
def request_data(start_date, stop_date):

    start = datetime.strptime(start_date, "%Y-%m-%d")  # and below- convert into datatype datetime
    key = '897d3a412b1b4c6c8ca73939191911'

    # key = "dcc2b4c7811149cea18190551190510"
    params = {"key": key, "format": "json", "q": "20.5,58.9", "time": "1800"}  # required parameters
    param2 = ["swellHeight_m", "windspeedKmph", "winddirDegree"]  # selected parameters, dependant on rest of key
    site = "http://api.worldweatheronline.com/premium/v1/past-marine.ashx"
    insert = []

    while str(start)[:10] != stop_date:  #datetime format has too much

        storage = []
        params["date"] = str(start)[:10]
        r = requests.get(site, params=params)
        x = r.json()
        storage = [str(start)[:10]]

        for i in param2:
            try:
                storage.append(x["data"]['weather'][0]["hourly"][12][i])  #"hourly"][0][i]["weather"]
            except KeyError:
                continue
        print(insert)
        insert.append(storage)
        start = start + timedelta(days=1)
        print(start)

    return insert
