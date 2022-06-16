import time
from urllib.request import urlopen
import json


def get_msw(location):
    if location == 557:
        url = "http://magicseaweed.com/api/c6ab2d38cfaad45602a4763035d1cc7c/forecast/?spot_id=557&fields=timestamp,wind.direction,wind.speed,swell.maxBreakingHeight&units=eu"
    elif location == 899:
        url = "http://magicseaweed.com/api/c6ab2d38cfaad45602a4763035d1cc7c/forecast/?spot_id=899&fields=timestamp,wind.direction,wind.speed,swell.maxBreakingHeight&units=eu"
    openurl = urlopen(url)
    data = json.loads(openurl.read())
    for i in data:
        i["timestamp"] = time.ctime(i['timestamp'])
    output = []

    for item in data:
        var = (item['timestamp'], item['swell']['maxBreakingHeight'], item['wind']['speed'], item['wind']['direction'])
        output.append(var)

    return output