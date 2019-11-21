from selenium import webdriver
from time import sleep

url = 'http://47.104.84.186:8080'
driver = webdriver.Chrome()
driver.get(url)
sleep(2)
#截图操作与保存路径
driver.get_screenshot_as_file("E://testo/PyThon/selenium/test_png/screen_test.png")
#注意：在alert界面无法截图
driver.quit()