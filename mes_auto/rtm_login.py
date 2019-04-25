from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#chrome
path="D:\python_work\python_ui\chromedriver.exe"
driver=webdriver.Chrome(path)

#maxsize windows
driver.maximize_window()

try:
    driver.get("http://10.16.193.194:8080/Account/Login?ReturnUrl=%2f")

    #add cookies
    driver.add_cookie({"name":"DB_DESC","value":"MES%E4%BA%A7%E5%93%81%E5%8C%96RTM%E7%8E%AF%E5%A2%83"})
    driver.add_cookie({"name":"webIP","value":"RTM"})
    driver.add_cookie({"name":"RegisterUserName","value":"qqcc"})
    driver.add_cookie({"name":"__RequestVerificationToken","value":"PyKkBwW7Ud2cHVj1zEb0GnjYfN5vG3AZZa-0zCCMZxq33mfxDu5jiXVt6xCqOPgd9GSwwJJ9llYMITrSox4Z2Oqnz3I39EnwgCLhPrbuoUYy02U-J_htzs-pMCPUqpb1Gwi7zA2"})
    driver.add_cookie({"name":".ASPXAUTH","value":"E189E6DDCB1FF7B7C0B310A6A99083C4E479111C15AD4CC3A97CE748E988CC3B7EE296AD0E9BFEC4AACE0AACD5373FACE46FE8170CD880789DADDA0E5EBA68D055A9333F3D44E38EB2862929759E1A7209A37E95A29BEA786FD491731860E004D8782B94"})

    time.sleep(3)

    #refresh
    driver.refresh()
    driver.get("http://10.16.193.194:8080")

    time.sleep(5)
    #change org
    change_org_element=driver.find_element_by_class_name("cd-invorg-icon")
    change_org_element.click()
    new_org_element=driver.find_element_by_partial_link_text("INV_M81")
    new_org_element.click()

    time.sleep(3)

    #change menu
    select_memu=driver.find_element_by_partial_link_text("业务中心")
    select_memu.click()
    time.sleep(3)
    search_element=driver.find_element_by_id("businessfilter")
    search_element.send_keys("目视化")
    search_element.send_keys(Keys.RETURN)

finally:
    time.sleep(5)
    #driver.quit()



