import pandas as pd  # 要改名的原因不可考
from decimal import Decimal
import datetime
csv_name = "5880"
input_name = csv_name + ".csv"
df = pd.read_csv(input_name, encoding='big5', low_memory=False)
pd.set_option('display.max_rows', None)
# df_close = df["p_close"]
df_close = df["close"]
len_close = len(df_close)
col = ["pred_days"]
# col = ["y_future", "y_result", "pred_days"]
df2 = pd.DataFrame(columns=col)
# print(df_close)

def predict_date(n, k):
    pred_list = []
    future_list = []
    result_list = []
    for i in range(len_close):
        if i < len_close - n:
            y_now = Decimal(str(df_close[i]))
            y_future = Decimal(str(df_close[i+n]))
            future_list.append(y_future)
            y_result = (y_future - y_now)/y_now
            result_list.append(y_result)
            if y_result > Decimal(str(0.025)):
                y_finally = "A"
            # elif y_result < Decimal(str(0.05)) and y_result > Decimal(str(0.01)):
            #     y_finally = "B"
            # elif y_result <= 0.01 and y_result >= -0.01:
            #     y_finally = "C"
            # elif y_result < -0.01 and y_result >= -0.04:
            #     y_finally = "D"
            elif y_result <= Decimal(str(0.025)) and y_result >= Decimal(str(-0.025)):
                y_finally = "B"
            elif y_result < -0.025:
                y_finally = "C"
        else:
            y_finally = "-"
            future_list.append("-")
            result_list.append("-")
        pred_list.append(y_finally)
    if k == 1:
        return pred_list
    elif k == 2:
        return future_list
    elif k == 3:
        return result_list


pred_1 = predict_date(20, 1)   # 看你是要跟幾個交易日後比
# pred_2 = predict_date(20, 2)
# pred_3 = predict_date(20, 3)

for j in range(len_close):
    data = [pred_1[j]]
    # data = [pred_2[j], pred_3[j], pred_1[j]]
    s = pd.Series(data, index=col)
    df2 = df2.append(s, ignore_index=True)
    df_append = df.join(df2, how='left')  # append是加在下面 join才是新增欄位

output_name = csv_name + "_talib_pred_C3.csv"
df_append.to_csv(output_name, encoding="Big5", index=False)
