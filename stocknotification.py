
import twstock
import requests
import schedule
import time
import pycron
import pytz
import lxml
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler




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
    

    stock0056 = twstock.realtime.get('0056')
    open0056=  stock0056['realtime']['open']
    low0056 = stock0056['realtime']['low']
    high0056 = stock0056['realtime']['high']
    ltr0056 = stock0056['realtime']['latest_trade_price']
       
    msg0056=(f' \n 元大高股息 \n||開盤價:{get_two_float(open0056, 2)} \n||最低價 {get_two_float(low0056, 2)} ||最高價 {get_two_float(high0056,2)} \n||現價:{get_two_float(ltr0056, 2)} \n')
   
    
   

    stock0050 = twstock.realtime.get('0050')
    open0050=  stock0050['realtime']['open']
    low0050 = stock0050['realtime']['low']
    high0050 = stock0050['realtime']['high']
    ltr0050 = stock0050['realtime']['latest_trade_price']
    msg0050=(f' \n 元大台灣 0050 \n||開盤價:{get_two_float(open0050, 2)} \n||最低價:{get_two_float(low0050, 2)} ||最高價:{get_two_float(high0050, 2)} \n||現價:{get_two_float(ltr0050, 2)} \n')
    
    stock006208 = twstock.realtime.get('006208')
    open006208=  stock006208['realtime']['open']
    low006208 = stock006208['realtime']['low']
    high006208 = stock006208['realtime']['high']
    ltr006208 = stock006208['realtime']['latest_trade_price']
    msg006208=(f' \n 富邦台50 \n||開盤價:{get_two_float(open006208, 2)} \n||最低價:{get_two_float(low006208, 2)} ||最高價:{get_two_float(high006208, 2)} \n||現價:{get_two_float(ltr006208, 2)} \n')
    

    

    url = "https://notify-api.line.me/api/notify"
    payload1={'message':{msg00878,msg0056,msg0050,msg006208}} 
    headers = {'Authorization': 'Bearer ' + '2ewKp4GssKQH9zY2VAwj07WMKxWYj3Ij6n5j1S0vSxV'}
    response = requests.request("POST", url, headers=headers, data=payload1)
    # print(response.text)

   
#半導體股
def sendToLine2():
    
    stock2330 = twstock.realtime.get('2330')
    open2330=  stock2330['realtime']['open']
    low2330 = stock2330['realtime']['low']
    high2330 = stock2330['realtime']['high']
    ltr2330 = stock2330['realtime']['latest_trade_price']   
    msg2330=(f' \n 台積電 2330 \n||開盤價:{get_two_float(open2330, 2)} \n||最低價 {get_two_float(low2330, 2)} ||最高價 {get_two_float(high2330, 2)} \n||現價:{get_two_float(ltr2330, 2)} \n')
    
    
   

    stock2454 = twstock.realtime.get('2454')
    open2454=  stock2454['realtime']['open']
    low2454 = stock2454['realtime']['low']
    high2454 = stock2454['realtime']['high']
    ltr2454 = stock2454['realtime']['latest_trade_price']
    msg2454=(f' \n 聯發科 2454 \n||開盤價:{get_two_float(open2454, 2)} \n||最低價:{get_two_float(low2454, 2)} ||最高價:{get_two_float(high2454, 2)} \n||現價:{get_two_float(ltr2454, 2)} \n')
    

    stock2379 = twstock.realtime.get('2379')
    open2379= stock2379['realtime']['open']
    low2379 = stock2379['realtime']['low']
    high2379 = stock2379['realtime']['high']
    ltr2379 = stock2379['realtime']['latest_trade_price']
    msg2379=(f' \n 瑞昱 2379 \n||開盤價:{get_two_float(open2379, 2)} \n||最低價:{get_two_float(low2379, 2)} ||最高價:{get_two_float(high2379, 2)} \n||現價:{get_two_float(ltr2379, 2)} \n')
    

    stock8299 = twstock.realtime.get('8299')
    open8299= stock8299['realtime']['open']
    low8299 = stock8299['realtime']['low']
    high8299 = stock8299['realtime']['high']
    ltr8299 = stock8299['realtime']['latest_trade_price']
    msg8299=(f' \n 群聯 8299 \n||開盤價:{get_two_float(open8299, 2)} \n||最低價:{get_two_float(low8299, 2)} ||最高價:{get_two_float(high8299, 2)} \n||現價:{get_two_float(ltr8299, 2)} \n')
    

    url = "https://notify-api.line.me/api/notify"
    payload2={'message':{msg2330,msg2454,msg2379,msg8299}} #台積電 and 聯發科 and 瑞昱 and 群聯message
    headers = {'Authorization': 'Bearer ' + '2ewKp4GssKQH9zY2VAwj07WMKxWYj3Ij6n5j1S0vSxV'}
    response = requests.request("POST", url, headers=headers, data=payload2)
    
    # print(response.text)
    
def sendToLine3():#AI相關股票
    
    stock2356 = twstock.realtime.get('2356')
    open2356=  stock2356['realtime']['open']
    low2356 = stock2356['realtime']['low']
    high2356 = stock2356['realtime']['high']
    ltr2356 = stock2356['realtime']['latest_trade_price']   
    msg2356=(f' \n 英業達 2356 \n||開盤價:{get_two_float(open2356, 2)} \n||最低價 {get_two_float(low2356, 2)} ||最高價 {get_two_float(high2356, 2)} \n||現價:{get_two_float(ltr2356, 2)} \n')
    
      

    stock3231 = twstock.realtime.get('3231')
    open3231=  stock3231['realtime']['open']
    low3231 = stock3231['realtime']['low']
    high3231 = stock3231['realtime']['high']
    ltr3231 = stock3231['realtime']['latest_trade_price']
    msg3231=(f' \n 緯創 3231 \n||開盤價:{get_two_float(open3231, 2)} \n||最低價:{get_two_float(low3231, 2)} ||最高價:{get_two_float(high3231, 2)} \n||現價:{get_two_float(ltr3231, 2)} \n')
    

    stock2382 = twstock.realtime.get('2382')
    open2382= stock2382['realtime']['open']
    low2382 = stock2382['realtime']['low']
    high2382 = stock2382['realtime']['high']
    ltr2382 = stock2382['realtime']['latest_trade_price']
    msg2382=(f' \n 廣達 2382 \n||開盤價:{get_two_float(open2382, 2)} \n||最低價:{get_two_float(low2382, 2)} ||最高價:{get_two_float(high2382, 2)} \n||現價:{get_two_float(ltr2382, 2)} \n')
    

    stock4938 = twstock.realtime.get('4938')
    open4938= stock4938['realtime']['open']
    low4938 = stock4938['realtime']['low']
    high4938 = stock4938['realtime']['high']
    ltr4938 = stock4938['realtime']['latest_trade_price']
    msg4938=(f' \n 和碩 4938 \n||開盤價:{get_two_float(open4938, 2)} \n||最低價:{get_two_float(low4938, 2)} ||最高價:{get_two_float(high4938, 2)} \n||現價:{get_two_float(ltr4938, 2)} \n')
    
    stock2324 = twstock.realtime.get('2324')
    open2324= stock2324['realtime']['open']
    low2324 = stock2324['realtime']['low']
    high2324 = stock2324['realtime']['high']
    ltr2324 = stock2324['realtime']['latest_trade_price']
    msg2324=(f' \n 仁寶 2324 \n||開盤價:{get_two_float(open2324, 2)} \n||最低價:{get_two_float(low2324, 2)} ||最高價:{get_two_float(high2324, 2)} \n||現價:{get_two_float(ltr2324, 2)} \n')

    stock3515 = twstock.realtime.get('3515')
    open3515= stock3515['realtime']['open']
    low3515 = stock3515['realtime']['low']
    high3515 = stock3515['realtime']['high']
    ltr3515 = stock3515['realtime']['latest_trade_price']
    msg3515=(f' \n 華擎 3515 \n||開盤價:{get_two_float(open3515, 2)} \n||最低價:{get_two_float(low3515, 2)} ||最高價:{get_two_float(high3515, 2)} \n||現價:{get_two_float(ltr3515, 2)} \n')


    url = "https://notify-api.line.me/api/notify"
    payload3={'message':{msg2356,msg3231,msg2382,msg4938,msg2324,msg3515}} #AI相關股票
    headers = {'Authorization': 'Bearer ' + '2ewKp4GssKQH9zY2VAwj07WMKxWYj3Ij6n5j1S0vSxV'}
    response = requests.request("POST", url, headers=headers, data=payload3)

    

#設定特定時間執行
now1=datetime.now()
timezone=pytz.timezone('Asia/Singapore')
current_time=now1.astimezone(timezone)

week = datetime.today().weekday()
   


# Creating a scheduler object.
scheduler = BlockingScheduler()
# scheduler.add_job(sendToLine1, "cron", minute='20',hour='7',day_of_week='mon-fri')
scheduler.add_job(sendToLine2, "cron", minute='25,45',hour='1-6',day_of_week='mon-fri')
scheduler.add_job(sendToLine3, "cron", minute='10,30,50',hour='1-6',day_of_week='mon-fri')
# Starting the scheduler in a separate thread.
scheduler.start()
      





  
