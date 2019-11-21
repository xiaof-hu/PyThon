from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("E://testo/PyThon/selenium/prac_html/aa.html")
sleep(1)

driver.find_element_by_xpath("//input[@value='cv1']").click()
driver.find_element_by_xpath("//input[@value='cv2']").send_keys(Keys.SPACE)
if driver.find_element_by_xpath("//input[@value='cv2']").is_selected():
    print("select!")
else:
    print("not select!")
sleep(1)
driver.find_element_by_xpath("//input[@value='rv1']").click()
sleep(1)
driver.find_element_by_xpath("//input[@value='rv2']").send_keys(Keys.SPACE)
sleep(2)



driver.quit()
