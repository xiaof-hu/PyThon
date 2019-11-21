#coding=utf-8
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

#binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe")
#driver = webdriver.Firefox(firefox_binary=binary)

# driver = webdriver.Firefox()
# chrome
driver = webdriver.Chrome()

driver.get('http://47.104.84.186:8080/')
# driver.find_element_by_id("index_search_words").send_keys("BUG")
time.sleep(2)
# driver.find_element_by_id("index_search_words").clear()
# driver.find_element_by_name("search").send_keys("task_python")
# time.sleep(2)
# driver.find_element_by_name("search").clear()
# # driver.find_element_by_class_name("layui-input").send_keys("python")
# # driver.find_element_by_link_text("林俊杰").click()
# # driver.find_element_by_partial_link_text("发布测试").click()
s = driver.find_element_by_id("index_search_words").size
# text = driver.find_element_by_css_selector('.fly-tip>a').text
text = driver.find_element_by_xpath("//div[@id='postss']/ul/li[2]/h2/a").text
# print(s)
# print(text)
# at = driver.find_element_by_css_selector(".fly-tip>a").get_attribute('href')#定位控件属性
at = driver.find_element_by_id("index_search_words").get_attribute('href')
dis = driver.find_element_by_id("index_search_words").is_displayed()#判断界面的控件是否显示出来
print(at)
print(type(dis))
print(dis)
if dis == True:
    driver.find_element_by_id("index_search_words").send_keys("BUG")
    text = driver.find_element_by_id("index_search_words").get_attribute("value")#验证输入的内容的值
    print(text)
else:
    time.sleep(1)
    driver.find_element_by_id("index_search_words").send_keys("task_python")
print(type(s))
print(text)
# driver.find_element_by_xpath('//input[@value="cv1"]').click()#定位选择控件并点击
# driver.find_element_by_xpath('//input[@value="cv2"]').send_keys(Keys.SPACE)#选择控件传值
# if driver.find_element_by_xpath('//input[@value="cv2"]').is_selected():#判断选择控件是否传值选中
#     print('selected!')
# else:
#     print('not selected!')
# time.sleep(2)
# driver.find_element_by_id("index_search_words").clear()
# driver.find_element_by_name("search").send_keys("python")
# driver.find_element_by_name("layui-input").send_keys("python")
# driver.find_element_by_xpath("html/body/div[2]/div/div/ul/div/ul/li[3]/h2/a").click()#绝对路径
# driver.find_element_by_xpath("//input[@id='index_search_words']").size
# driver.find_element_by_xpath("//input[@id='index_search_words']").send_keys("test1")
# driver.find_element_by_xpath("//*[@id='index_search_words']").send_keys("test2")
# driver.find_element_by_xpath("//form[@id='postsSearch']/input").send_keys("test3")
# driver.find_element_by_xpath("//input[contains(@placeholder,'输入内容')]").send_keys("test4")
# driver.find_element_by_css_selector("html>body>div>div>div>div>form>input").send_keys("test5")
# driver.find_element_by_css_selector("html body div div div div form input").send_keys("test6")
# driver.find_element_by_css_selector("input#index_search_words").send_keys("test7")
# driver.find_element_by_css_selector("input.layui-input").send_keys("test8")
# driver.find_element_by_css_selector("input[autocomplete='off'][placeholder='输入内容，点击搜索'][name='search']").send_keys("test9")
# driver.find_element_by_css_selector("form#postsSearch>input").send_keys("test10")
# driver.find_element_by_css_selector("form[id='postsSearch']>input").send_keys("test11")
# driver.find_element_by_css_selector("form#postsSearch>input:nth-child(2)").send_keys("test12")


# driver.back()#返回上一页
# driver.forward()#前进下一页
# driver.refresh()#刷新页面
#获取title
title = driver.title
print(title)
#设置窗口尺寸
driver.set_window_size(980,1000)#设置浏览器窗口尺寸
driver.maximize_window()#浏览器窗口最大化
time.sleep(2)
driver.quit()
