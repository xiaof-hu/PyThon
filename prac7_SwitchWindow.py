from selenium import webdriver
from time import sleep

url = "http://www.baidu.com"
driver =webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element_by_id("kw").send_keys("好123")
driver.find_element_by_id("su").click()
#获取当前所有的窗体信息
print(driver.window_handles)
sleep(3)
driver.find_element_by_partial_link_text("hao123").click()
print(driver.window_handles)
#显示当前所在的窗体
print(driver.current_window_handle)

#切换到目标窗体
driver.switch_to.window(driver.window_handles[1])
print(driver.current_window_handle)

sleep(2)
driver.quit()#关闭所有窗体，close只关闭当前所在的窗体
