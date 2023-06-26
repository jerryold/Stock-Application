
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

def sendToLine1(): #ETF
    
    stock00878 = twstock.realtime.get('00878')
    open00878=  stock00878['realtime']['open']
    low00878 = stock00878['realtime']['low']
    high00878 = stock00878['realtime']['high']
    ltr00878 = stock00878['realtime']['latest_trade_price']
       
    msg00878=(f' \n 國泰永續高股息 \n||開盤價:{get_two_float(open00878, 2)} \n||最低價 {get_two_float(low00878, 2)} ||最高價 {get_two_float(high00878,2)} \n||現價:{get_two_float(ltr00878, 2)} \n')
    print(msg00878)

    stock0056 = twstock.realtime.get('0056')
    open0056=  stock0056['realtime']['open']
    low0056 = stock0056['realtime']['low']
    high0056 = stock0056['realtime']['high']
    ltr0056 = stock0056['realtime']['latest_trade_price']
       
    msg0056=(f' \n 元大高股息 \n||開盤價:{get_two_float(open0056, 2)} \n||最低價 {get_two_float(low0056, 2)} ||最高價 {get_two_float(high0056,2)} \n||現價:{get_two_float(ltr0056, 2)} \n')
    print(msg0056)
    
   

    stock0050 = twstock.realtime.get('0050')
    open0050=  stock0050['realtime']['open']
    low0050 = stock0050['realtime']['low']
    high0050 = stock0050['realtime']['high']
    ltr0050 = stock0050['realtime']['latest_trade_price']
    msg0050=(f' \n 元大台灣 0050 \n||開盤價:{get_two_float(open0050, 2)} \n||最低價:{get_two_float(low0050, 2)} ||最高價:{get_two_float(high0050, 2)} \n||現價:{get_two_float(ltr0050, 2)} \n')
    print(msg0050)

    stock006208 = twstock.realtime.get('006208')
    open006208=  stock006208['realtime']['open']
    low006208 = stock006208['realtime']['low']
    high006208 = stock006208['realtime']['high']
    ltr006208 = stock006208['realtime']['latest_trade_price']
    msg006208=(f' \n 富邦台50 \n||開盤價:{get_two_float(open006208, 2)} \n||最低價:{get_two_float(low006208, 2)} ||最高價:{get_two_float(high006208, 2)} \n||現價:{get_two_float(ltr006208, 2)} \n')
    print(msg006208)

    

    url = "https://notify-api.line.me/api/notify"
    payload1={'message':{msg00878,msg0056,msg0050,msg006208}} 
    headers = {'Authorization': 'Bearer ' + '2ewKp4GssKQH9zY2VAwj07WMKxWYj3Ij6n5j1S0vSxV'}
    response = requests.request("POST", url, headers=headers, data=payload1)
    print(response.text)

   

def sendToLine2():
    
    stock2330 = twstock.realtime.get('2330')
    open2330=  stock2330['realtime']['open']
    low2330 = stock2330['realtime']['low']
    high2330 = stock2330['realtime']['high']
    ltr2330 = stock2330['realtime']['latest_trade_price']   
    msg2330=(f' \n 台積電 2330 \n||開盤價:{get_two_float(open2330, 2)} \n||最低價 {get_two_float(low2330, 2)} ||最高價 {get_two_float(high2330, 2)} \n||現價:{get_two_float(ltr2330, 2)} \n')
    print(msg2330)
    
   

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
    payload1={'message':{msg2330,msg2454,msg2379,msg8299}} #台積電 and 聯發科 and 瑞昱 and 群聯message
    headers = {'Authorization': 'Bearer ' + '2ewKp4GssKQH9zY2VAwj07WMKxWYj3Ij6n5j1S0vSxV'}
    response = requests.request("POST", url, headers=headers, data=payload1)
    print(response.text)

    

#設定特定時間執行
now1=datetime.now()
timezone=pytz.timezone('Asia/Singapore')
current_time=now1.astimezone(timezone)


def weekday_job1(x):
    week = datetime.today().weekday()
    if week<5 and 1<=current_time.now().hour<=6:        
       schedule.every().hours.at(":20").do(x) 

def weekday_job2(x):
    week = datetime.today().weekday()
    if week<5 and 1<=current_time.now().hour<=6:        
       schedule.every().hours.at(":40").do(x) 


      


weekday_job1(sendToLine2)
weekday_job2(sendToLine1)
while True:
    try:
        schedule.run_pending()
        time.sleep(60)
    except Exception as e:
        sendToLine1(e)
        sendToLine2(e)
        time.sleep(60)



  
