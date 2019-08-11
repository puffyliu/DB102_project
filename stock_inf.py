import datetime
from selenium import webdriver
import pandas as pd  # 要改名的原因不可考
import read_stock50 as stock50
from sqlalchemy import create_engine

csv_name = str(datetime.date.today()) + "_inf.csv"
col = ["id", "t_date", "code", "name", "p_open", "p_high", "p_low", "p_close", "volume"]
df = pd.DataFrame(columns=col)
code_list = stock50.code_list()
stock_list = stock50.stock_list()
code_len = len(code_list)

engine = create_engine(
    "mysql+pymysql://{user}:{pw}@{localhost}:{port}/{db}".format(user="db102stock", pw="db102stock_pwd",
                                                                 localhost="10.120.14.18", port=3307, db="stock"))

for i in range(code_len):
    try:
        url = "https://www.cnyes.com/twstock/ps_historyprice/" + str(code_list[i]) + ".htm"
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver = webdriver.Chrome(chrome_options=option)
        # driver = Chrome("./chromedriver")
        driver.get(url)

        table_data = driver.find_element_by_class_name("tab")
        table_tr = table_data.find_elements_by_tag_name("tr")
        table_tr.pop(0)
        # 表的內容
        # 將表的每一行的每一列內容存在table_td_list中，從第1列開始
        table_td = table_tr[0].text
        # print(table_td)
        table_td_list = table_td.split(" ")
        # 排掉不要的欄位
        table_td_list.pop(5)
        table_td_list.pop(5)
        table_td_list.pop()
        table_td_list.pop()
        # 設計id的格式
        td_year = str(table_td_list[0][:4])
        td_month = str(table_td_list[0][5:7])
        td_day = str(table_td_list[0][8:])
        td_id = code_list[i] + td_year + td_month + td_day
        # 把數字欄位的逗號去掉，否則會無法匯入DB(資料型態不對)
        for j in range(6):
            table_td_list[j] = table_td_list[j].replace(",", "")

        data = [td_id, table_td_list[0], code_list[i], stock_list[i], table_td_list[1], table_td_list[2],
                table_td_list[3], table_td_list[4], table_td_list[5]]
        s = pd.Series(data, index=col)
        df = df.append(s, ignore_index=True)

    finally:
        driver.close()

# 儲存表格至csv
df.to_csv(csv_name, encoding="Big5", index=False)  # Big5不會變亂碼 LOL
# print(df)
df.to_sql(con=engine, name='stock_inf', if_exists='append', index=False)
