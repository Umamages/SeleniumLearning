from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

ser_obj=Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
a = webdriver.Chrome(service=ser_obj)
a.get("http://www.leafground.com/")
a.maximize_window()
print(a.title)
e = a.find_element_by_xpath("//*[@id='post-153']/div[2]/div/ul/li[1]/a")
e.click()
a.close()


