
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#chrome
path='D:\python_work\python_ui\chromedriver.exe'
driver=webdriver.Chrome(path)

#maxsize window
driver.maximize_window()
try:
    #open url
    driver.get("http://www.runoob.com/python3/python3-module.html")
    #find search_element
    search_webelement=driver.find_element_by_id('s')
    search_webelement.send_keys('python')
    #keyboard enter
    search_webelement.send_keys(Keys.RETURN)


finally:
    time.sleep(3)
    driver.quit()