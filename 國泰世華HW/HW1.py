import pandas as pd
import os
import numpy as np

os.chdir("D:\Andy\Desktop\lvr_landcsv")
df_a = pd.read_csv("a_lvr_land_a.csv", encoding='UTF-8', low_memory=False)
df_b = pd.read_csv("b_lvr_land_a.csv", encoding='UTF-8', low_memory=False)
df_e = pd.read_csv("e_lvr_land_a.csv", encoding='UTF-8', low_memory=False)
df_f = pd.read_csv("f_lvr_land_a.csv", encoding='UTF-8', low_memory=False)
df_h = pd.read_csv("h_lvr_land_a.csv", encoding='UTF-8', low_memory=False)

df_all = pd.concat([df_a,df_b,df_e,df_f,df_h],axis=0)
df_all = df_all[df_all.duplicated()==False]
# df_all.drop(axis=0, index=0, inplace=True)  # 去掉第一行英文

filter1 = df_all["主要用途"] == "住家用"
filter2 = df_all["建物型態"] == "住宅大樓(11層含以上有電梯)"
df_filt1 = df_all[filter1 & filter2]
# 第三個條件碰到問題，因為沒有辦法直接比較中文數字大小
# 先過濾掉前兩個條件後在過濾第三個

total_floor = np.array(df_filt1["總樓層數"])
floor_list = total_floor.tolist()

def transform(s):
    num = 0
    dict1 = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    if s: # 確保傳入的值恆為true
        idx_s = s.find('十')   # 找有沒有'十'
        if idx_s != -1:
            num += dict1.get(s[0], 1) * 10    # 十位數的值乘上10，沒有一十所以預設值為1
        if s[-1] in dict1:   # 個位數
            num += dict1[s[-1]]
    return num

def transform2(l):
    list1 = []
    for x in l:
        x = str(x)
        if '層' in x:
            x = transform(x[:-1])
            if x >= 13:
                x = 'True'
        list1.append(x)
    return list1

def unique_index(L, e):
    return [i for (i, j) in enumerate(L) if j == e]

floor_index = unique_index(transform2(floor_list), 'True')
df_filt2 = df_filt1.iloc[floor_index]
df_filt2.to_csv("filter_a.csv", encoding="big5", index=False)
