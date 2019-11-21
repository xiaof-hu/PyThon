from selenium import webdriver
import time

d = webdriver.Chrome()
d.get('https://www.ctrip.com/')
# driver.find_element_by_id("index_search_words").send_keys("BUG")
time.sleep(5)

d.find_element_by_xpath("//input[@id = 'HD_CityName']").send_keys("武汉")

time.sleep(2)
d.find_element_by_xpath("//form[@id ='chinaHotelForm']/div[5]/input").click()

#页面滚动条滑动到最底部
js="var q=document.documentElement.scrollTop=100000"
d.execute_script(js)
time.sleep(2)
#页面滚动条移动到页面的50%高度
d.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5)")
time.sleep(3)
#页面偏移到相对位置
d.execute_script("window.scrollBy(0, 900)");
time.sleep(2)
#页面偏移到绝对位置
d.execute_script("window.scrollTo(0, 1500)");
time.sleep(2)
#页面滚动条滑动到最顶部
js="var q=document.documentElement.scrollTop=0"
d.execute_script(js)

# js = "document.getElementById('noticeEndTime').removeAttribute('readonly')"
# js = "document.getElementsById('noticeEndTime')[0].removeAttribute('readonly')"
# d.execute_script(js)
time.sleep(3)
d.quit()