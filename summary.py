import os 
import pandas as pd 

mypath = "./2021record"
## 列出所有
files =  os.listdir(mypath)


filtered = []
for item in files:
    timean = item[0:4]
    if timean == "2021":
        filtered.append(item)
df = pd.read_csv('./2021record/2021-08-30 19_00.csv', encoding="utf-8", sep=",")
df = df[0:1]
df['year'] = df['record_time'].str[0:4]
df['month'] = df['record_time'].str[5:7]


for item in filtered:
    newdf = pd.read_csv("./2021record/" + item, encoding="utf-8", sep=",")
    newdf['year'] = newdf['record_time'].str[0:4]
    newdf['month'] = newdf['record_time'].str[5:7]
    newdf = newdf[newdf['name'] == '大潭CC#4']
    df = pd.concat([df, newdf], axis=0)
    print(item)

df.to_csv("summarylngadcc4.csv", encoding="utf-8", sep=",")

