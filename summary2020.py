import os
import pandas as pd

mypath = "./2020record"
## 列出所有
files = os.listdir(mypath)


filtered = []
for item in files:
    timean = item[13:]
    if timean == "_00.csv":
        filtered.append(item)
df = pd.read_csv('./2020record/2020-08-30 19_00.csv',
                 encoding="utf-8", sep=",")
df['year'] = df['record_time'].str[0:4]
df['month'] = df['record_time'].str[5:7]


for item in filtered:
    newdf = pd.read_csv("./2020record/" + item, encoding="utf-8", sep=",")
    newdf['year'] = newdf['record_time'].str[0:4]
    newdf['month'] = newdf['record_time'].str[5:7]
    df = pd.concat([df, newdf], axis=0)
    print(item)

df.to_csv("summary2020.csv", encoding="utf-8", sep=",")
