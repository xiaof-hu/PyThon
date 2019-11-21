from selenium import webdriver
from time import sleep
import json

url = "https://fly.layui.com/user/login/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

# cookies = driver.get_cookies()
# print(cookies)

# cookiesFile = json.dumps(cookies)
# with open('cookiesFile.json','w') as filemy:
#     filemy.write(cookiesFile)

with open('cookiesFile.json','r') as filemy:
    cookiesInfo = json.loads(filemy.read())
for cc in range(0,len(cookiesInfo)):
    print(cookiesInfo[cc])
    driver.add_cookie(cookiesInfo[cc])
driver.refresh()

sleep(3)
driver.quit()
