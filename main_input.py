import twstock
from twstock import BestFourPoint 
import time

#input stock number輸入股票代號
#output stock number and stock name輸出股票代號與公司名稱
def name(num):
    number = twstock.realtime.get(num)
    real = number['realtime']
    info = number['info']
    code = info['code']
    name = info['name']
    latest_price = real['latest_trade_price']
    print ( code , name )
    print ( "最後交易價格為：" , latest_price )

#Best Four Point Analysis
def best_four_point(num):
#   stock = twstock.Stock(num)
    bfp = twstock.BestFourPoint(stock)
    
    bestbuy = bfp.best_four_point_to_buy()
    bestsell = bfp.best_four_point_to_sell()
    if ( bestbuy == False ):
        print( "現在並非買點")
    else:
        print( "可以買，符合：" , bestbuy )
    if ( bestsell == False ):
        print( "現在並非賣點")
    else:
        print( "可以賣，符合：" , bestsell )

#calulate 30 days average 計算30日平均
def average_30(num):
    get_30_price = stock.price
    summary = 0
    for i in range(30):
        summary = summary + get_30_price[i]
    average = summary / 30  
    print( "30日平均價格為" , average )

if __name__ == "__main__":
    num = input("請輸入股票代號：")
    stock = twstock.Stock(num)
    name(num)
    best_four_point(num)
    average_30(num)
    print("")
    time.sleep(0.5)
