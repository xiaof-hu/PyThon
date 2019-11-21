#coding:utf-8
from selenium import webdriver
from time import sleep

url = 'https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

ele = driver.find_element_by_id('HD_CheckIn')
ele.clear()
ele.send_keys("2019-11-12")

eleOut = driver.find_element_by_id("HD_CheckOut")
eleOut.clear()
eleOut.send_keys("2019-11-13")

driver.find_element_by_xpath("//form[@id='chinaHotelForm']/div[5]/input").click()

sleep(5)
driver.quit()