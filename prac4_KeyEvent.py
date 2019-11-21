from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.baidu.com")
sleep(2)

driver.find_element_by_id("kw").send_keys("selenium+")
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
sleep(2)
driver.find_element_by_id("kw").send_keys("教程")
sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
sleep(2)#ctrl+a
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
sleep(2)#ctrl+x
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
sleep(2)#ctrl+v

driver.quit()
