from selenium import webdriver
from time import sleep
import datetime


url = "http://47.104.84.186:8083/crm/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_name("userNum").send_keys("admin")
driver.find_element_by_name("userPw").send_keys("admin")
driver.find_element_by_id("in1").click()
sleep(2)
driver.switch_to.frame("topFrame")
aa = driver.find_element_by_link_text("公告信息").get_attribute("href")
print(aa)
# driver.get(aa)
driver.find_element_by_link_text("公告信息").click()
# sleep(2)
#返回主文档
driver.switch_to.default_content()
#进入mainFrame
driver.switch_to.frame("mainFrame")
#点击【添加】按钮
driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input").click()
sleep(2)
#清空时间戳属性
#方法一
# js = "document.getElementById('noticeEndTime').removeAttribute('readonly')"
#方法二
js = "document.getElementsByName('noticeEndTime')[0].removeAttribute('readonly')"
#方法三
#js = "document.getElementsByTagName('input')[0].removeAttribute('readonly')
driver.execute_script(js)

#输入的时间
now = datetime.datetime.now()
delta = datetime.timedelta(days=3)
print(now)
print(delta)
n_days = now+delta
print(n_days.strftime("%Y-%m-%d %H:%M%S"))
driver.find_element_by_name("noticeEndTime").send_keys(n_days.strftime("%Y-%m-%d %H:%M%S"))
ss = driver.find_element_by_name("noticeEndTime").get_attribute("value")
print(ss)


sleep(3)
driver.quit()