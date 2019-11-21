import time
import pytesseract
from PIL import Image, ImageEnhance
from selenium import webdriver
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying

url = "https://www.hfax.com/login.html#/"
# 1、打开浏览器，最大化浏览器
driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(10)#隐式等待时间
driver.maximize_window()

# 用户名元素
userElement = driver.find_element(By.XPATH, "//input[@id = 'userName']")
# 密码元素
passElement = driver.find_element(By.XPATH, "//input[@id = 'passWord']")
# 验证码输入框元素
codeElement = driver.find_element(By.XPATH, "//div[@id ='wrapper']/div[4]/div[5]/div/input")
# 验证图片元素
imgElement = driver.find_element(By.XPATH, "//div[@id ='wrapper']/div[4]/div[5]/img")

# 2、截取屏幕内容，保存到本地
driver.save_screenshot("E://testo/PyThon/selenium/test_png/01.png")

# 3、打开截图，获取验证码位置，截取保存验证码
ran = Image.open("E://testo/PyThon/selenium/test_png/01.png")
location = imgElement.location # 定位验证码位置及大小
size = imgElement.size
#定位到截图位置
# 获取图片x轴位置
left = location['x']*1.00 #1.00表示本地计算机屏幕缩放比例
# 获取图片y轴位置
top = location['y']*1.00
# 获取图片右边界
right = (location['x'] + size['width'])*1.00
# 获取图片下边界
bottom = (location['y'] + size['height'])*1.00
box = (left, top, right, bottom)
# box = (1120, 280, 1180, 310) # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
ran.crop(box).save("E://testo/PyThon/selenium/test_png/02.png")

# 4、获取验证码图片，读取验证码
imageCode = Image.open("E://testo/PyThon/selenium/test_png/02.png")  # 图像增强，二值化
# imageCode.load()
sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
sharp_img.save("E://testo/PyThon/selenium/test_png/03.png")
sharp_img.load()  # 对比度增强
time.sleep(2)
print(sharp_img)
code = pytesseract.image_to_string(sharp_img).strip()
# 5、收到验证码，进行输入验证
print(code)

userElement.send_keys('13128712049')
passElement.send_keys('hxf00001')

# time.sleep(3)
codeElement.send_keys(code)
click_login = driver.find_element(By.XPATH, "//div[@id ='wrapper']/div[4]/div[8]")
click_login.click()
