from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://47.104.84.186:8080/'
driver = webdriver.Chrome()
driver.get(url)

sleep(2)
#隐式等待时间
driver.implicitly_wait(3)

#显式等待时间
test = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(
    (By.XPATH,"//input[@name='search' and @autocomplete='off']")))
test.send_keys("BUG")
sleep(2)
driver.quit()