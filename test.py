from selenium import webdriver

driver=webdriver.Chrome("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
driver.close()
