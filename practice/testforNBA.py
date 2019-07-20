from urllib.request import urlopen
import pandas as pd  # 要改名的原因不可考
import json

c = ["選手", "每場得分", "投籃命中率", "三分球命中率", "罰球命中率"]
df = pd.DataFrame(columns=c)
for page in range(6):
    url = "https://tw.global.nba.com/stats2/league/playerstats.json?conference=All&country=All&individual=All&locale" \
          "=zh_TW&pageIndex=" + str(page) + "&position=All&qualified=false&season=2018&seasonType=4&split=All+Team" \
          "&statType=points&team=All&total=perGame"
    # print(url)
    response = urlopen(url)
    doodles = json.load(response)  # 轉成python格式
    i = 0
    while i >= 0:
        try:
            players = doodles["payload"]["players"][i]
            i += 1
        except:
            break
    # print(i)

    for m in range(i):
        name = doodles["payload"]["players"][m]["playerProfile"]["displayName"]
        # print(name, end=" ")
        pointsPg = doodles["payload"]["players"][m]["statAverage"]["pointsPg"]
        # print(pointsPg, end=" ")
        fgpct = doodles["payload"]["players"][m]["statAverage"]["fgpct"]
        # print(fgpct, end=" ")
        tppct = doodles["payload"]["players"][m]["statAverage"]["tppct"]
        # print(tppct, end=" ")
        ftpct = doodles["payload"]["players"][m]["statAverage"]["ftpct"]
        # print(ftpct)

        data = [name, pointsPg, fgpct, tppct, ftpct]

        s = pd.Series(data, index=c)
        df = df.append(s, ignore_index=True)
df.to_csv("stock.csv", encoding="utf-8", index=False)