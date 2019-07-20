import requests
from bs4 import BeautifulSoup
import re
import os
from datetime import datetime

url = "https://www.ptt.cc/bbs/Beauty/M.1561379833.A.267.html"
response = requests.get(url)
# print(response.text)
html = BeautifulSoup(response.text)
content = html.find("div", id="main-content")

metas = content.find_all("span", class_="article-meta-value")
print("ID: ", metas[0].text)
print("看板: ", metas[1].text)
print("標題: ", metas[2].text)
category = re.match(r"\[.+\]", metas[2].text).group(0)  # 不會的話上網找python regex
print("類別: ", category)   # r表示不做轉換，因為有些字條會有\n，沒打r就會變成換行
post_time = datetime.strptime(metas[3].text, "%a %b %d %H:%M:%S %Y")  # 上網找python datetime
print("時間: ", post_time)

# 刪除前萃取圖片
anchors = content.find_all("a")
for a in anchors:
    img_url = a["href"]
    last = img_url.split("/")[-1]
    if "." in last and ".html" not in last:
        dir = "ptt/" + metas[2].text.replace("/", "") + "/"
        if not os.path.exists(dir):
            os.makedirs(dir)
        fp = dir + last
        img_response = requests.get(img_url, stream=True)
        # 純文字: "r", "w" + encoding
        # 非純文字: "rb", "wb"
        f = open(fp, "wb")
        # 如果你非純文字 要加.raw
        f.write(img_response.raw.read())
        f.close()

# 丟掉盒子: extract()
metas = content.find_all("div", class_="article-metaline")
for m in metas:
    m.extract()
metas = content.find_all("div", class_="article-metaline-right")
for m in metas:
    m.extract()


pushes = content.find_all("div", class_="push")
score = 0
for p in pushes:
    tag = p.find("span", class_="push-tag").text
    if "推" in tag:  # 不用等於是因為實際上他是推+空白
        score = score + 1
    elif "噓" in tag:
        score = score - 1
    p.extract()
print("分數: ", score)

spans = content .find_all("span")
deletes_span = ["發信站:", "編輯:", "的推文:"]
for s in spans:
    if "來自:" in s.text:     # 丟掉前把IP抓出來
        ip = s.text.split("來自:")[-1].split(" ")[1]
    for d in deletes_span:
        if d in s.text:
            s.extract()
print("IP: ", ip)
print("內容: ", content.text)
f = open(dir + "post.txt", "w", encoding="utf-8")
f.write(content.text)
f.close()