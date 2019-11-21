import time
from selenium import webdriver

# # driver = webdriver.firefox()
# driver = webdriver.Chrome()
# driver.get("www.baidu.com")
# print(driver.title)
# time.sleep(5)
# driver.quit


from selenium import webdriver
import sys
driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(3)  # 等待3秒

driver.get("https://www.hfax.com/login.html")
print(driver.title)
driver.find_element_by_id("userName").send_keys("13128712049")
driver.find_element_by_id("passWord").send_keys("hxf00001")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.close()
