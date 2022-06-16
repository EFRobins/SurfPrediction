from urllib.error import URLError, HTTPError
from datetime import date
from urllib.request import urlopen, urlretrieve
from Predictions import filltable


def create_source():
    url = 'https://magicseaweed.com/Northern-Indian-Ocean-Surf-Chart/43/?type=swell'
    page = urlopen(url)
    source = str(page.read())
    return source


def find_str(source):
    index = 0
    url2 = "https://charts-s3.msw.ms/live/wave/"
    if url2 in source:
        c = url2[0]
        for ch in source:
            if ch == c:
                if source[index:index + len(url2)] == url2:
                    return index

            index += 1

    return -1


def find_gif(source, start_point):
    x = True
    while x:
        if source[start_point: start_point + 3] == "gif":
            x = False
            return start_point + 3
        else:
            start_point += 1


def update_app():
    f = open("Date.txt", "w+")
    lastdate = f.read()
    if str(date.today()) != str(lastdate):
        try:
            source = create_source()
            start_point = find_str(source)
            end_point = find_gif(source, start_point)
            image_url = source[start_point:end_point]
            urlretrieve(image_url, r"C:\Users\robin\PycharmProjects\NEA\Images\condition.png")
            f.write(str(date.today()))
            filltable(899)
            filltable(557)
        except URLError or HTTPError:
            print("Connect to the internet:")
            exit()


update_app()
