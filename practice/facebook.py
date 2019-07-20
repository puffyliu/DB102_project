from selenium.webdriver import Chrome
import time
from practice import secret

driver = Chrome("./chromedriver")    # 加./是為了讓程式知道driver是在專案底下，沒加的話就會去找環境變數

driver.get("https://www.facebook.com")

# BeautifulSoup: find, find_all
# selenium: find_element, find_elements
driver.find_element_by_id("email").send_keys(secret.username)
driver.find_element_by_id("pass").send_keys(secret.password)
driver.find_element_by_id("loginbutton").click()

# 有些會需要輸入驗證碼
# s = input("請輸入安全碼")
# driver.find_element_by_id("approvals_code").send_keys(s)
# driver.find_element_by_id("checkpointSubmitButton").click()
#
# time.sleep(1)
# driver.find_element_by_id("checkpointSubmitButton").click()

time.sleep(5)
post = driver.find_element_by_class_name("userContent")
# 紙條:
print(post.text)

time.sleep(3)
driver.close()