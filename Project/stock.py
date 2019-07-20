from urllib.request import urlopen
import pandas as pd  # 要改名的原因不可考
import json

c = ["證券代號", "證券名稱", "漲停價(本日)", "開盤競價基準(本日)", "跌停價(本日)", "開盤競價基準(前日)", "收盤價(前日)", "買進揭示價(前日)", "賣出揭示價(前日)", "最近成交日", "可否零股交易"]
df = pd.DataFrame(columns=c)

# 台灣證交所
url = "https://www.twse.com.tw/exchangeReport/TWT84U?response=json&date=20190712&selectType=ALL&_=1562915520190"

response = urlopen(url)
doodles = json.load(response)
# print(doodles)

i = 0
while i >= 0:
    try:
        stock_data = doodles["data"][i]
        # print(stock_data)
        i += 1
    except:
        break

for m in range(i):
    stockid = doodles["data"][m][0]  # 證券代號
    print(stockid, end=" ")
    name = doodles["data"][m][1]    # 證券名稱
    print(name, end=" ")
    limit_up_price = doodles["data"][m][2]  # 漲停價(本日)
    print(limit_up_price, end=" ")
    open_price_std = doodles["data"][m][3]  # 開盤競價基準(本日)
    print(open_price_std, end=" ")
    limit_down_price = doodles["data"][m][4]  # 跌停價(本日)
    print(limit_down_price, end=" ")
    open_price_std_y = doodles["data"][m][5]  # 開盤競價基準(昨日)
    print(open_price_std_y, end=" ")
    closing_price = doodles["data"][m][6]  # 收盤價
    print(closing_price, end=" ")
    buy_price = doodles["data"][m][7]  # 買進揭示價
    print(buy_price, end=" ")
    sell_price = doodles["data"][m][8]  # 賣出揭示價
    print(sell_price, end=" ")
    recent_date = doodles["data"][m][9]  # 最近成交日
    print(recent_date, end=" ")
    zero = doodles["data"][m][10]  # 可否零股交易
    print(zero)

    data = [stockid, name, limit_up_price, open_price_std, limit_down_price, open_price_std_y, closing_price, buy_price, sell_price, recent_date, zero]

    s = pd.Series(data, index=c)
    df = df.append(s, ignore_index=True)

df.to_csv("stock.csv", encoding="utf-8", index=False)
