
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
    driver.get("http://mesplus.midea.com.cn/Account/Login?ReturnUrl=%2f")
    #find search_element
    driver.add_cookie({"name":"DB_DESC","value":"MES%E4%BA%A7%E5%93%81%E5%8C%96%E6%AD%A3%E5%BC%8F%E7%8E%AF%E5%A2%83"})
    driver.add_cookie({"name":"webIP","value":"109"})
    driver.add_cookie({"name":"RegisterUserName","value":"yanqc1"})
    driver.add_cookie({"name":"__RequestVerificationToken","value":"El_4J5cSj29Mh3o3y0kPyn-QKokIVuBcaRV_iAsP1awnBQxBS149aC1hQ2ABW1sqh-FIauueAcXEO5pf0nOuLEIele2tEhuyuTIJG4rhldH3JgZtZ95HIg36zz-ihh0qB64aRA2"})
    driver.add_cookie({"name":".ASPXAUTH","value":"1865833AB326820927233B561EF4B6C0BC5A44E90480D3D100EA56DA58D97F845E45B96DFB12DD0E6E66E9E6F935BB638FB2E66AC000379189AB73B91C6378F6A659BD1D4F2D467DA191E1EEBD774F6B6ADD20A43A4E4C7DC0684D6E200DDBB90C2C03FCE5C8DE47ED8CB90392F11C5FA2CF3A60"})
    #sleep 3s
    time.sleep(3)

    #refresh
    driver.refresh()
    driver.get("http://mesplus.midea.com.cn/zh-CN/MAP/TaskManager")


finally:
    time.sleep(5)
    # driver.quit()