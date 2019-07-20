from pytube import Playlist
from selenium.webdriver import Chrome
from practice import secret
import time
import os
driver = Chrome("./chromedriver")

driver.get("https://www.youtube.com/view_all_playlists")
driver.find_element_by_id("identifierId").send_keys(secret.username)
driver.find_element_by_id("identifierNext").click()
time.sleep(3)

driver.find_element_by_class_name("whsOnd").send_keys(secret.pwd)
driver.find_element_by_id("passwordNext").click()
time.sleep(5)

ps = driver.find_elements_by_class_name("vm-video-title-text")
for p in ps:
    # 特徵: bs的["href"] -> get_attribute("href")
    # print(p.text)
    purl = p.get_attribute("href")
    # print(purl)
    pl = Playlist(purl, suppress_exception=True)
    dirname = "yt/" + p.text + "/"
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    try:
        # 歌單裡的歌會被擋所以沒有下載成功
        pl.download_all(dirname)
    # 403先略過去
    except:
        print("略過", purl)
