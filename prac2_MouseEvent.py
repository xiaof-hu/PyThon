from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.maximize_window()
sleep(2)

ele = driver.find_element_by_link_text("更多产品")
sleep(2)

# ActionChains(driver).move_to_element(ele).perform()
# sleep(2)
# ActionChains(driver).move_to_element_with_offset(ele,0,100).perform()
# sleep(2)
ActionChains(driver).context_click(ele).perform() #右击
ActionChains(driver).double_click(ele).perform() #双击
sleep(2)
driver.close()