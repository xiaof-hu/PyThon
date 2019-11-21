#coding=utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

url = 'https://www.ctrip.com/'
driver =webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

#通过text：select_by_visible_text()
s = driver.find_element_by_id("J_roomCountList")
#通过参数值select
# Select(s).select_by_visible_text("2间")
driver.implicitly_wait(5)
#通过索引select
# Select(s).select_by_index(3)
#通过value值select
Select(s).select_by_value("5")

sleep(3)
driver.quit()