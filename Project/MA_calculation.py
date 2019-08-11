import pandas as pd  # 要改名的原因不可考
from decimal import Decimal
import datetime

# df = pd.read_csv("history_stock.csv", encoding='big5', low_memory=False)
df = pd.read_csv("2881.csv", encoding='big5', low_memory=False)
pd.set_option('display.max_rows', None)
df_close = df["p_close"]
len_close = len(df_close)
# close_re = df_close.str.replace(",", "")  # 把千分位數去掉
close_re = df_close.replace(",", "")  # 有的不用轉str

def moving_average(n):
    avg_list = []
    for i in range(len_close):
        total_close = 0
        if i in range(len_close - (n - 1)):
            for k in range(n):
                total_close += Decimal(close_re[i + k])
            avg_close = round(total_close / n, 2)
            avg_list.append(str(avg_close))
        else:
            avg_list.append("-")
    return avg_list


try:
    col = ["ma5", "ma10", "ma20", "ma60", "ma22", "ma46", "ma92", "ma95", "ma200", "ma400"]
    df2 = pd.DataFrame(columns=col)
    print(datetime.datetime.now(), " 開始計算MA")
    MA5 = moving_average(5)
    print(datetime.datetime.now(), " 已算完MA5")
    MA10 = moving_average(10)
    print(datetime.datetime.now(), " 已算完MA10")
    MA20 = moving_average(20)
    print(datetime.datetime.now(), " 已算完MA20")
    MA60 = moving_average(60)
    print(datetime.datetime.now(), " 已算完MA60")
    MA22 = moving_average(22)  # 週5週
    print(datetime.datetime.now(), " 已算完MA22")
    MA46 = moving_average(46)
    print(datetime.datetime.now(), " 已算完MA46")
    MA92 = moving_average(92)
    print(datetime.datetime.now(), " 已算完MA92")
    MA95 = moving_average(95)  # 月5月
    print(datetime.datetime.now(), " 已算完MA95")
    MA200 = moving_average(200)
    print(datetime.datetime.now(), " 已算完MA200")
    MA400 = moving_average(400)
    print(datetime.datetime.now(), " 已算完MA400")
    for j in range(len_close):
        print("開始時間: ", datetime.datetime.now())
        data = [MA5[j], MA10[j], MA20[j], MA60[j], MA22[j], MA46[j], MA92[j], MA95[j], MA200[j], MA400[j]]
        s = pd.Series(data, index=col)
        df2 = df2.append(s, ignore_index=True)
        print("做到第{}個".format(j), end=" ")
        print("結束時間: ", datetime.datetime.now())
    df_append = df.join(df2, how='left')  # append是加在下面 join才是新增欄位
finally:
    # df_append.to_csv("history_stock_MA.csv", encoding="Big5", index=False)
    df_append.to_csv("2881_MA.csv", encoding="Big5", index=False)
