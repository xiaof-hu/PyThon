#coding:utf-8
from selenium import webdriver
from time import sleep

url = 'https://mail.163.com'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
sleep(2)

driver.find_element_by_xpath("//div[@id='commonOperation']/a").click()
# driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input").send_keys("testonline_hu")
#第一种方式
# driver.switch_to.frame("x-URS-iframe")#有id,name,如id是变化的则不适用
#第二种方式
# dd = driver.find_element_by_xpath("//div[@id='loginDiv']/iframe")
# driver.switch_to.frame(dd)
#第三种方式
iframes = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframes[0])

emailName = driver.find_element_by_name('email')
emailName.send_keys("testonline_hu")
password = driver.find_element_by_name('password')
password.send_keys("Hu19891229?")
button = driver.find_element_by_id('dologin')
button.click()


#从子frame切回到父frame
driver.switch_to.parent_frame()
#切回到主文档
driver.switch_to.default_content()

sleep(2)
driver.quit()
