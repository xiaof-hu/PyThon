from selenium import webdriver
from time import sleep

url = 'file:///E://testo/PyThon/selenium/prac_html/task_python.html'
driver = webdriver.Chrome()
driver.get(url)
sleep(2)
#触发alert
driver.execute_script("prom()")
sleep(2)
#输入alert文字信息
driver.switch_to.alert.send_keys("test_TT")
sleep(2)
#获取输入的alert文字信息
print(driver.switch_to.alert.text)
#对页面展示的alert执行确认按钮操作
driver.switch_to.alert.accept()
print(driver.switch_to.alert.text)
#解除alert弹出
driver.switch_to.alert.dismiss()

sleep(2)

driver.quit()



