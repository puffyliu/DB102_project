from selenium import webdriver
from selenium.webdriver import Chrome
import time
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import pymongo

url = "https://rent.591.com.tw/?kind=0&region=3&shType=list"
driver = Chrome("./chromedriver")
driver.get(url)

# 點選新北市
driver.find_element_by_xpath('//*[@id="area-box-body"]/dl[1]/dd[2]').click()
# 點選台北市
# driver.find_element_by_xpath('//*[@id="area-box-body"]/dl[1]/dd[1]').click()
time.sleep(3)

c = ["出租者", "出租者身份"]
df = pd.DataFrame(columns=c)

all_url_list = []
identity_list = []
name_list = []
while True:
    # 判斷是否為最後一頁，不是就點及下一頁﹐是就停下
    pagenext = driver.find_element_by_xpath('//*[@id="container"]/section[5]/div/div[1]/div[5]/div/a[8]')
    page_href = pagenext.get_attribute("href")
    next_button = driver.find_element_by_class_name("pageNext")
    page_current = driver.find_element_by_class_name("pageCurrent").text

    # 把一頁中的連結都存到一個list中
    i = 1
    while i > 0:
        try:
            path = '//*[@id="content"]/ul' + str([i]) + '/li[2]/h3/a'
#             print(path)
            info = driver.find_element_by_xpath(path)
            inf = info.get_attribute("href")
#             print(inf)
            path2 = '//*[@id="content"]/ul' + str([i]) + '/li[2]/p[3]/em[1]'
            identity = driver.find_element_by_xpath(path2).text.split(" ")[0]
            name = driver.find_element_by_xpath(path2).text.split(" ")[1]
            all_url_list.append(inf)
            data = [name, identity]
            s = pd.Series(data, index=c)
            df = df.append(s, ignore_index=True)
            i += 1
        except:
            break

    next_button.click()
    time.sleep(3)


    if page_href is None:
        print("到最後一頁了")
        break

#     if page_current == '5':  # 測試用
#         break


c2 = ["聯絡電話", "型態", "現況", "性別要求"]
df2 = pd.DataFrame(columns=c2)
for url in all_url_list:
    try:
        response = urlopen(url)
    except HTTPError:
        print("好像是最後一頁了")
    html = BeautifulSoup(response)

    phone = html.find("span", class_="dialPhoneNum").attrs.get("data-value")
    building_type = html.find("ul", class_="attr")
    type_li = building_type.find_all("li")
    for t in type_li:
        if "型態" in t.text:
            build_type = t.text.replace("型態\xa0:\xa0\xa0", "")
        if "現況" in t.text:
            situation = t.text.replace("現況\xa0:\xa0\xa0", "")
    gender_limit = html.find_all("div", class_="one")
    for gl in gender_limit:
        if "性別要求" in gl.text:
            gender_limit2 = gl.find_next_sibling("div")
    #         print(gender_limit2.text)
            gender_limit3 = gender_limit2.text[1:]
        else:
            gender_limit3 = "無此限制"
    data2 = [phone, build_type, situation, gender_limit3]
    s2 = pd.Series(data2, index=c2)
    df2 = df2.append(s2, ignore_index=True)

df_final = pd.concat([df, df2], axis=1, ignore_index=False)
df_final.to_csv("新北_租屋物件資料2.csv", encoding="big5", index=False)

# 連線到MongoDB
conn = pymongo.MongoClient('localhost', 27017)
mydb = conn.HW_Cathay
myCollect = mydb.rentweb

records = df_final.to_dict('records')
myCollect.insert_many(records)
conn.close()