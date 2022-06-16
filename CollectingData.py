from datetime import datetime
from datetime import timedelta
import requests

key = '48a6ec88eef9463689062741190711'  # api key
# key = "dcc2b4c7811149cea18190551190510"                                 #2nd api key if 1st doesnt work
params = {"key": key, "format": "json", "q": "20.5,58.9", "date": "2016-01-01"}  # required parameters
param2 = ["swellHeight_m", "windspeedKmph", "swellDir",
          "winddirDegree"] # selected parameters, dependant on rest of key

site = "http://api.worldweatheronline.com/premium/v1/past-marine.ashx"  # api url


def request_from_api(start_date, stop_date):  # YY-MM-DD
    output = []
    start = datetime.strptime(start_date, "%Y-%m-%d")  # converts date into a datetime datatype

    while start != stop_date:
        storage = []
        start = start + timedelta(days=1)  # adds to the date then removes formatting issues otherwise time is included
        params["date"] = str(start)[:10]   # changes date to a day forward
        r = requests.get(site, params)     # actually getting the data
        x = r.json()                       # converts to json format
        storage.append(start)              #
        print(x)
        for i in range(len(param2)):
            try:
                storage.append()
            except KeyError:
                continue
        print(start, storage)
        output.append(storage)
    print(output)
    return output
