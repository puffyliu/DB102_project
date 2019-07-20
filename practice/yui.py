import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.request import urlretrieve
url = "https://www.google.com/search?ei=GnkUXbWYG5LM-Qby9q9I&rlz=1C1SQJL_zh-TWTW836TW836&yv=3&q=%E6%96%B0%E5%9E%A3%E7%B5%90%E8%A1%A3&tbm=isch&vet=10ahUKEwi1jY-nmonjAhUSZt4KHXL7CwkQuT0ITygB.GnkUXbWYG5LM-Qby9q9I.i&ved=0ahUKEwi1jY-nmonjAhUSZt4KHXL7CwkQuT0ITygB&ijn=1&start=100&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc"
headers = {"accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/75.0.3770.100 Safari/537.36 "
           }
response = requests.get(url, headers=headers)
# urlretrieve(url, "a.txt")
html = BeautifulSoup(response.text)
metas = html.find_all("div", class_="rg_meta")
# print(metas)
for m in metas[:10]:
    picture = json.loads(m.text)
    # print(picture.keys())
    img_url = picture["ou"]
    print(img_url)
    dirname = "yui/"
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    fp = dirname + img_url.split("/")[-1]
    img_response = requests.get(img_url, headers=headers, stream=True)
    try:
        f = open(fp, "wb")
        f.write(img_response.raw.read())
        f.close()
    except:
        print("放過")
