from selenium import webdriver
import time
import json

d = webdriver.Chrome()
d.get('https://fly.layui.com/user/login/')
# driver.find_element_by_id("index_search_words").send_keys("BUG")
time.sleep(5)

#登录成功了
cookies = d.get_cookies()
print(cookies)

cookiesFile = json.dumps(cookies)
with open('cookiesFile.json', 'w') as filemy:
    filemy.write(cookiesFile)

cookiesInfo = json.loads(filemy.read())
for cc in range(0,len(cookiesInfo)):
    print(cookiesInfo[cc])
d.add_cookie(cookiesInfo[cc])
d.refresh()

d.quit()