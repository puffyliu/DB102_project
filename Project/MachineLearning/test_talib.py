import pandas as pd
from talib import abstract

code_name = "5880"
read_name = code_name + ".csv"
df = pd.read_csv(read_name)
len_date = len(df['t_date'])
df['t_date'] = pd.to_datetime(df['t_date'])
df.set_index("t_date", inplace=True)

col = ["MACD", "K", "D", "RSI"]
df2 = pd.DataFrame(columns=col)

MACD = abstract.MACD(df)["macdsignal"]
# print(MACD)

# print(abstract.STOCH)
K = abstract.STOCH(df, fastk_period=9, slowk_period=3, slowd_period=3)["slowk"]
D = abstract.STOCH(df, fastk_period=9, slowk_period=3, slowd_period=3)["slowd"]
# print(abstract.RSI)
RSI = abstract.RSI(df, timeperiod=6)

# '''
for j in range(len_date):
    data = [round(MACD[j], 3), round(K[j], 3), round(D[j], 3), round(RSI[j], 3)]
    s = pd.Series(data, index=col)
    df2 = df2.append(s, ignore_index=True)
    # df_append = df.join(df2, how='left')
to_name = code_name + "_Index.csv"
df2.to_csv(to_name, encoding="Big5", index=False)  # Big5不會變亂碼 LOL
# '''