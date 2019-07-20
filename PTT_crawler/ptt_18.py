import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/M.1561615239.A.103.html"
response = requests.get(url, cookies={"over18": "1"})   # 沒加cookie就只會顯示確認是否18歲
html = BeautifulSoup(response.text)
print(html)