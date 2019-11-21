from selenium import webdriver
from time import sleep

url = "https://qiye.163.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

js = "var q=document.documentElement.scrollTop=100000"#数值100000足够大
#移动到页面底部
driver.execute_script(js)
sleep(2)
#移动当前坐标移动到的坐标
driver.execute_script("window.scrollTo(0, document.body.scrollHeigth*0.5)")
sleep(2)
#移动到绝对坐标
driver.execute_script("window.scrollBy(0,900)")
sleep(2)
text = driver.find_element_by_css_selector(".copyright").text
print(text)
sleep(2)

js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)

sleep(3)
driver.quit()
