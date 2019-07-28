from selenium.webdriver import Chrome
import pandas as pd  # 要改名的原因不可考
import read_stock50 as stock50

col = ["代號", "交易日期", "外資庫存", "外資買賣超", "投信買賣超", "自營買賣超"]
df = pd.DataFrame(columns=col)
code_list = stock50.code_list()
stock_list = stock50.stock_list()
code_len = len(code_list)

for i in range(code_len):
    url = "http://pchome.megatime.com.tw/stock/sto1/sid" + code_list[i] + ".html"
    driver = Chrome("./chromedriver")
    driver.get(url)

    t_date = driver.find_element_by_xpath("//div[@id='bttb']/table[1]/tbody/tr[3]/td[1]").text
    fi_st = driver.find_element_by_xpath("//div[@id='bttb']/table[1]/tbody/tr[3]/td[5]").text  # 外資持股
    fi_netbs = driver.find_element_by_xpath("//div[@id='bttb']/table[1]/tbody/tr[3]/td[4]").text  # 外資買賣超
    it_netbs = driver.find_element_by_xpath("//div[@id='bttb']/table[2]/tbody/tr[3]/td[4]").text  # 投信買賣超
    sq_netbs = driver.find_element_by_xpath("//div[@id='bttb']/table[3]/tbody/tr[3]/td[4]").text  # 自營商買賣超

    data = [code_list[i], t_date, fi_st, fi_netbs, it_netbs, sq_netbs]
    s = pd.Series(data, index=col)
    df = df.append(s, ignore_index=True)
    df.to_csv("tech_analy.csv", encoding="Big5", index=False)
    driver.close()
