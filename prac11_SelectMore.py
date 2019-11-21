from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

url = 'file:///E://testo/PyThon/selenium/prac_html/moreSelect.html'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(3)
#多选实现
s = driver.find_element_by_id("all")
Select(s).select_by_index(0)
Select(s).select_by_index(1)
sleep(3)
#取消先择
Select(s).deselect_by_index(1)
#获取选框里的所有option
txt = Select(s).all_selected_options
print(txt[0].text)


sleep(3)
driver.quit()