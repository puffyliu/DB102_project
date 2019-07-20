from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.error import HTTPError

c = ["標題", "價格", "排名", "可否運送", "圖片", "連結"]
df = pd.DataFrame(columns=c)
page = 1

for page in range(1, 15):
    try:
        url = "https://www.amazon.com/s?k=%E7%90%83%E6%A3%92&i=sports-and-fitness&rh=n%3A10971181011%2Cn%3A5680491011" \
              "&dc&page=" + str(page) + "&language=zh_TW&qid=1562220914&rnid=2941120011&ref=sr_pg_" + str(page)
        print("page = ", str(page))
        head = {'accept-language': "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/75.0.3770.100 Safari/537.36'}
        r = requests.get(url, headers=head)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        bat_statics = soup.find_all("div", class_='sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item '
                                                  'sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32')
        for i in bat_statics:
            try:
                name = i.find('span', class_="a-size-base-plus a-color-base a-text-normal")
                print(name.text, end=" | ")
                if i.find('span', class_="a-offscreen") is None:
                    if i.find('div', class_="a-section a-spacing-none a-spacing-top-mini") is None:
                        price = i.find('span', class_="a-size-base a-color-base a-text-normal")
                    else:
                        price_div = i.find('div', class_="a-section a-spacing-none a-spacing-top-mini")
                        price = price_div.find('span', class_="a-color-base")
                else:
                    price = i.find('span', class_="a-offscreen")
                print(price.text, end=" | ")
                if i.find('span', class_="a-icon-alt") is not None:
                    rank = i.find('span', class_="a-icon-alt").text
                else:
                    rank = ""
                print(rank, end=" | ")
                if i.find('span', class_="a-size-small a-color-secondary") is not None:
                    eligible = i.find('span', class_="a-size-small a-color-secondary").text
                else:
                    eligible = ""
                print(eligible, end=" | ")
                img = i.find('img', class_="s-image")
                print(img['src'], end=" | ")
                link = "https://www.amazon.com/" + i.find('a', class_="a-link-normal a-text-normal")["href"]
                print(link)

            except:
                print("有錯誤!!")
                continue
            data = [name.text, price.text, rank, eligible, img['src'], link]
            s = pd.Series(data, index=c)
            df = df.append(s, ignore_index=True)
        page = page + 1
        df.to_csv("Amazon.csv", encoding="utf-8", index=False)

    except:
        # print("爬蟲失敗!", end=" ")
        # print("page = ", str(page))
        continue
