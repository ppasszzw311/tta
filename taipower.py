### import 相關
import os
import pandas as pd
import json
import requests

### 建立每天
datedaily = []

for i in range(24):
    for j in range(6):
        if i < 10:
            item = '/0' + str(i) + '_' + str(j) + '0.log'
            datedaily.append(item)
        else:
            item = '/' + str(i) + '_' + str(j) + '0.log'
            datedaily.append(item)
### 設定網頁爬蟲變數
### 製作一年

datelist2021 = []
month_l = ['01', '02', '03', '04', '05',
           '06', '07', '08', '09', '10', '11', '12']
day_l = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
         '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
for i in month_l:
    for j in day_l:
        item = '2021-' + i + '-' + j
        datelist2021.append(item)

### 去除沒資料的日期
### 去除沒資料的日期

### 2021-03-31 2021-04-01 ~ 07 2021-05-02 2021-12-10~12
### 2020-01-28 ~ 31 2020-05-19 2020-05-29 ~31 2020-06-01 ~ 02 2020-12-03
### 2019-02-01 ~ 04
### 2018-12-26

#### 另案處理
### 2021-03-01 地熱
### 2021-12-23 other renewable energy
### 2020-07-20 地熱 其他
### 2019-01-24 改中文
### 2019-01-31 02-06 water



errorlist = []

for date in datelist2021:
    for item in datedaily:
        url_link = "https://raw.githubusercontent.com/apan1121/powerInfo/gh-pages/log/history/" + date + item
        try:
            result = requests.get(url_link)
            daily = pd.DataFrame(json.loads(result.text))
            data = daily['info']
            dailyitii = []
            for i in range(len(daily)):
                newdata = {
                    "record_time": daily['time'][i],
                    "type": data[i]['type'],
                    "name": data[i]['name'],
                    "mappingName": data[i]['mappingName'],
                    'capacity': data[i]['capacity'],
                    'used': data[i]['used'],
                    'percent': data[i]['percent'],
                    'gov': data[i]['gov'],
                    'status': data[i]['status'],
                    'note': data[i]['note'],
                    'noteId': data[i]['noteId']
                }
                dailyitii.append(newdata)
            dailypandas = pd.json_normalize(dailyitii)
            name_a = item[1:6]
            dailypandas.to_csv('2019record/' + date + ' ' +
                               name_a + '.csv', sep=",", header=True, encoding="utf-8")
        except:
            print("錯誤", date, item)
            ist = date + item
            errorlist.append(ist)
