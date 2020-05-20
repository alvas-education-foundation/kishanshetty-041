import time
import os
import pandas

while True:
    if os.path.exists("temperature.csv"):
        data = pandas.read_csv("temperature.csv")
        print(data.mean())
    else:
        print("File does not exists.")
    time.sleep(5)
