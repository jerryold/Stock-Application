
import twstock
import requests
import schedule
import time
import pycron
import pytz
from datetime import datetime, timedelta




def get_two_float(f_str, n):
    a, b, c = f_str.partition('.')
    c = c[:n]
    return ".".join([a, c])

def sendToLine():
    
    stock2330 = twstock.realtime.get('2330')
    open2330=  stock2330['realtime']['open']
    low2330 = stock2330['realtime']['low']
    high2330 = stock2330['realtime']['high']
    ltr2330 = stock2330['realtime']['latest_trade_price']
    
    # msg2330=(f' \n 台積電 2330 \n {get_two_float(low2330, 2)} ||{get_two_float(high2330, 2)} \n 現價 {get_two_float(ltr2330, 2)} \n')
    # print(msg2330)
    msg2330=(f' \n 台積電 2330 \n||開盤價:{get_two_float(open2330, 2)} \n||最低價 {get_two_float(low2330, 2)} ||最高價 {get_two_float(high2330, 2)} \n||現價:{get_two_float(ltr2330, 2)} \n')
    print(msg2330)
    # current=float(get_two_float(ltr2330, 2))
   

    stock2454 = twstock.realtime.get('2454')
    open2454=  stock2454['realtime']['open']
    low2454 = stock2454['realtime']['low']
    high2454 = stock2454['realtime']['high']
    ltr2454 = stock2454['realtime']['latest_trade_price']
    msg2454=(f' \n 聯發科 2454 \n||開盤價:{get_two_float(open2454, 2)} \n||最低價:{get_two_float(low2454, 2)} ||最高價:{get_two_float(high2454, 2)} \n||現價:{get_two_float(ltr2454, 2)} \n')
    print(msg2454)

    stock2379 = twstock.realtime.get('2379')
    open2379= stock2379['realtime']['open']
    low2379 = stock2379['realtime']['low']
    high2379 = stock2379['realtime']['high']
    ltr2379 = stock2379['realtime']['latest_trade_price']
    msg2379=(f' \n 瑞昱 2379 \n||開盤價:{get_two_float(open2379, 2)} \n||最低價:{get_two_float(low2379, 2)} ||最高價:{get_two_float(high2379, 2)} \n||現價:{get_two_float(ltr2379, 2)} \n')
    print(msg2379)

    stock8299 = twstock.realtime.get('8299')
    open8299= stock8299['realtime']['open']
    low8299 = stock8299['realtime']['low']
    high8299 = stock8299['realtime']['high']
    ltr8299 = stock8299['realtime']['latest_trade_price']
    msg8299=(f' \n 群聯 8299 \n||開盤價:{get_two_float(open8299, 2)} \n||最低價:{get_two_float(low8299, 2)} ||最高價:{get_two_float(high8299, 2)} \n||現價:{get_two_float(ltr8299, 2)} \n')
    print(msg8299)

    url = "https://notify-api.line.me/api/notify"
    payload1={'message':{msg2330}} #台積電message
    headers = {'Authorization': 'Bearer ' + '2ewKp4GssKQH9zY2VAwj07WMKxWYj3Ij6n5j1S0vSxV'}
    response = requests.request("POST", url, headers=headers, data=payload1)
    print(response.text)

    payload2={'message':{msg2454,msg2379,msg8299}} #聯發科 and 瑞昱 and 群聯message
    response = requests.request("POST", url, headers=headers, data=payload2)
    print(response.text)

#設定特定時間執行
now1=datetime.now()
timezone=pytz.timezone('Asia/Singapore')
current_time=now1.astimezone(timezone)
datetime.today().toordinal()%7 + 1


def weekday_job(x):
    week = datetime.today().weekday()
    if week<5 and 1<=current_time.now().hour<=6:
        schedule.every(30).seconds.do(x)
     
        


weekday_job(sendToLine)

while True:
    schedule.run_pending()
    time.sleep(60)

  

# schedule.every(20).seconds.do(sendToLine) # 每20秒執行一次
# schedule.every(5).minutes.do(sendToLine)  # 每20秒執行一次


# while True:
#     schedule.run_pending()
#     time.sleep(1)