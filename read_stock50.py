import csv

fn = 'stock50.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)


# 把代碼存在一個串列
def code_list():
    code = []
    for i in range(len(listReport)):
        code.append(listReport[i][0])
    return code

# 把名稱存在一個串列
def stock_list():
    stock = []
    for i in range(len(listReport)):
        stock.append(listReport[i][1])
    return stock
