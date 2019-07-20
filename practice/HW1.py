from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pandas as pd     # 要改名的原因不可考
page = 1
# PD!
c = ["分數", "價格", "英文", "日文", "網站"]
df = pd.DataFrame(columns=c)
while True:
    url = "https://tabelog.com/tw/tokyo/rstLst/" + str(page) + "/?SrtT=rt"
    print(url)
    try:
        response = urlopen(url)
    except HTTPError:
        print("好像是最後一頁了")
        break
    html = BeautifulSoup(response)
    # find:找第一個符合條件的->盒子
    # find_all:找所有符合條件的->list
    # 用法:盒子.find_xx
    restaurants = html.find_all("li", class_="list-rst")  # 多加一個底線是為了避開關鍵字class
    for r in restaurants:
        ja = r.find("small", class_="list-rst__name-ja")    # 找出所有店名
        # print(ja.text)
        en = r.find("a", class_="list-rst__name-main")
        rating = r.find("b", class_="c-rating__val")
        prices = r.find_all("span", class_="c-rating__val")
        # 特徵: 盒子["href"]
        # 紙條: .text
        pt = prices[0].text
        pt2 = ""
        if pt == "-":
            continue
        else:
            pt2 = pt
        pt3 = pt2.replace("￥", "").replace("～", " ").replace(",", "")
        pt4 = pt3.split(" ")
        pt5 = ""
        if pt4[0] == "":
            pt5 = "0"
        elif int(pt4[0]) > 10000:
            continue
        else:
            pt5 = pt4[0]

        # PD!!
        data = [rating.text, pt5, en.text, ja.text, en["href"]]
        s = pd.Series(data, index=c)
        df = df.append(s, ignore_index=True)
    page += 1
df.to_csv("HW1.csv", encoding="utf-8", index=False)