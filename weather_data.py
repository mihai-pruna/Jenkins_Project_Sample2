#!/bin/python3

import time
import urllib.request


DOMAIN = "https://weerindelft.nl"
ENDPOINT = "clientraw.txt"
url = DOMAIN + "/" + ENDPOINT

def main():
    try:
        weather_data = urllib.request.urlopen(url).read().decode()
    except:
        print("Unable to establish connection")
        exit()

    data_points = weather_data.split()
    print("Current weather is: ", data_points[4])

if __name__=="__main__":
    while True:
        main()
        time.sleep(5)


