from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pandas as pd     # 要改名的原因不可考

c = ["排名", "選手", "隊伍", "出賽數", "每場上場時間", "每場得分", "投籃進球數", "投籃出手數", "投籃命中率", "三分球進球數", "三分球投籃數", "三分球命中率", "罰球進球數", "罰球數", "罰球命中率"]
df = pd.DataFrame(columns=c)
url = "https://www.msn.com/zh-tw/sports/nba/player-stats"
try:
    response = urlopen(url)
except HTTPError:
    print("好像是最後一頁了")
html = BeautifulSoup(response)
print(html)
# find:找第一個符合條件的->盒子
# find_all:找所有符合條件的->list
# 用法:盒子.find_xx
player_statics = html.find_all("tr", class_="rowlink")  # 多加一個底線是為了避開關鍵字class
for r in player_statics:
    rk = r.find("td", class_="rank")    # 找出所有球員的排名
    # print(rk.text, end=" ")
    name = r.find("a")
    # print(name.text, end=" ")
    team = r.find("td", class_="teamname")
    # print(team.text, end=" ")
    append = r.find_all("td")[3]
    # print(append.text, end=" ")
    time = r.find_all("td")[4]
    # print(time.text, end=" ")
    score = r.find_all("td")[5]
    # print(score.text, end=" ")
    fg = r.find_all("td", class_="hide1")[1]
    # print(fg.text, end=" ")
    shoot = r.find_all("td", class_="hide1")[2]
    # print(shoot.text, end=" ")
    fgp = r.find_all("td")[8]
    # print(fgp.text, end=" ")
    tp = r.find_all("td", class_="hide1")[3]
    # print(tp.text, end=" ")
    tps = r.find_all("td", class_="hide1")[4]
    # print(tps.text, end=" ")
    tpp = r.find_all("td", class_="hide1")[5]
    # print(tpp.text, end=" ")
    fst = r.find_all("td", class_="hide123")[0]
    # print(fst.text, end=" ")
    fs = r.find_all("td", class_="hide123")[1]
    # print(fs.text, end=" ")
    fsp = r.find_all("td", class_="hide123")[2]
    # print(fsp.text)

    data = [rk.text, name.text, team.text, append.text, time.text, score.text, fg.text, shoot.text, fgp.text, tp.text, tps.text, tpp.text, fst.text, fs.text, fsp.text]
    s = pd.Series(data, index=c)
    df = df.append(s, ignore_index=True)

# df.to_csv("NBA.csv", encoding="utf-8", index=False)
