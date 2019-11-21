from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
#***********************滑块的处理******************************
driver = webdriver.Chrome()
driver.get("http://www.huodongxing.com/login")
driver.maximize_window()
sleep(2)

driver.find_element_by_link_text("登录").click()
driver.implicitly_wait(10)
driver.find_element_by_id("txtName").send_keys("13128712049")
driver.find_element_by_id("txtPwd").send_keys("qwe123")
driver.find_element_by_id("Remember1").click()
sleep(3)
source = driver.find_element_by_xpath("//div[@id='geetest_captcha']/div/div[2]/div/div[3]")
driver.find_element_by_xpath("//div[@id='geetest_captcha']/div/div[2]/div/div[3]").click()
sleep(5)
track = driver.find_element_by_xpath("//div[@class='geetest_slider_track']").size
print(track)
source1 = driver.find_element_by_xpath("//div[@class='geetest_slider_button']")
ActionChains(driver).drag_and_drop_by_offset(source1,130,0).perform()
sleep(5)

# sleep(30)·

# sourse = driver.find_element_by_xpath(".//*")

driver.quit()