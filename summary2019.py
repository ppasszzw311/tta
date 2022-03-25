import os
import pandas as pd

mypath = "./2020record"
## 列出所有
files = os.listdir(mypath)


filtered = []
for item in files:
    timean = item[13:]
    yearmonth = item[:7]
    if yearmonth == "2020-12":
      if timean == "_00.csv":
        filtered.append(item)
df = pd.read_csv('./2020record/2020-07-30 00_00.csv',
                 encoding="utf-8", sep=",")
df['year'] = df['record_time'].str[0:4]
df['month'] = df['record_time'].str[5:7]
df = df[0:1]


for item in filtered:
    newdf = pd.read_csv("./2020record/" + item, encoding="utf-8", sep=",")
    newdf['year'] = newdf['record_time'].str[0:4]
    newdf['month'] = newdf['record_time'].str[5:7]
    df = pd.concat([df, newdf], axis=0)
    print(item)

df.to_csv("2020_12.csv", encoding="utf-8", sep=",")
