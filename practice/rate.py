import requests
from bs4 import BeautifulSoup
import schedule
import time
from twilio.rest import Client


def job():
    response = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
    html = BeautifulSoup(response.text)
    rows = html.find("table").find("tbody").find_all("tr")
    for r in rows:
        tds = r.find_all("td")
        if "日圓" in tds[0].text:
            print("現金匯率:", tds[2].text)

            account_sid = "ACb3cf0ec8ec1c181e78f0ff062b025316"
            auth_token = "373b9662f3e5425032aa679c3c89d24d"
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to="+886932038305",
                from_="+12562578043",
                body="日圓匯率:" + tds[2].text)


schedule.every().day.at("11:26").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)