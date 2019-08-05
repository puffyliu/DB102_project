import pandas as pd  # 要改名的原因不可考
from decimal import Decimal
import datetime
csv_name = "2454"
input_name = csv_name + ".csv"
df = pd.read_csv(input_name, encoding='big5', low_memory=False)
pd.set_option('display.max_rows', None)
df_close = df["p_close"]
len_close = len(df_close)
col = ["pred_days"]
df2 = pd.DataFrame(columns=col)
# print(df_close)

def predict_date(n):
    pred_list = []
    for i in range(len_close):
        if i < len_close - n:
            y_now = Decimal(str(df_close[i]))
            y_future  = Decimal(str(df_close[i+n]))
            y_result = y_future - y_now
            if y_result > 0:
                y_finally = "up"
            elif y_result == 0:
                y_finally = "same"
            else:
                y_finally = "down"
        else:
            y_finally = "-"
        pred_list.append(y_finally)
    return pred_list


pred_1 = predict_date(20)   # 看你是要跟幾個交易日後比

for j in range(len_close):
    data = [pred_1[j]]
    s = pd.Series(data, index=col)
    df2 = df2.append(s, ignore_index=True)
    df_append = df.join(df2, how='left')  # append是加在下面 join才是新增欄位

output_name = csv_name + "_pred.csv"
df_append.to_csv(output_name, encoding="Big5", index=False)