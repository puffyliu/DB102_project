from jieba.analyse import extract_tags
from jieba import cut, set_dictionary, load_userdict
from urllib.request import urlretrieve
import os

if not os.path.exists("dict.txt.big"):
    print("幫你下載大辭典!")
    url = "https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big"
    urlretrieve(url, "dict.txt.big")
else:
    print("已經下載過了!")

set_dictionary("dict.txt.big")
# load_userdict("mydict.txt")   # 如果要新增辭典內容就加這行

f = open("b.txt", "r", encoding="utf-8")
article = f.read()
f.close()

print(" ".join(cut(article)))
print(extract_tags(article, 10))