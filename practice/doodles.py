# [MAC]SSL Certificate FAIL  這句是MAC電腦才要加的
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# 上面兩行都是MAC要加的
from urllib.request import urlopen, urlretrieve
import json
import os
years = ["2018", "2019"]
for y in years:
    for m in range(12):
        url = "https://www.google.com/doodles/json/" + str(y) + "/" + str(m + 1) + "?hl=zh_TW"
        response = urlopen(url)
        # print(response.read())    read讀完就會去掉裡面的資料，若讀第二次就是空的
        doodles = json.load(response)   # 轉成python格式
        for d in doodles:
            url = "https:" + d["url"]
            # print(d["title"], url)
            # print(url.split("/")[-1])     # 把url分割然後只取最後一段
            dirname = "doodles/" + str(y) + "/" + str(m + 1) + "/"
            path = dirname + url.split("/")[-1]
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            urlretrieve(url, path)      # 下載

