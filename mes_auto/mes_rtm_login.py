from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import json

#Chrome
path="D:\python_work\python_ui\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.maximize_window()

def save_cookies(driver):
    project_path=os.path.dirname(os.getcwd())
    file_path=project_path+"\\cookies\\"

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    cookies_file=file_path+"mes.cookies"

    cookies=driver.get_cookies()
    with open(cookies_file,"w") as f:
        json.dump(cookies,f)

    print(cookies)

def login():
    driver.get("http://10.16.193.194:8080/Account/Login?ReturnUrl=%2f")

    time.sleep(2)
    driver.find_element_by_id("userinput").send_keys("qqcc")
    driver.find_element_by_id("passwordinput").send_keys("1")

    driver.find_element_by_id("btnlogin").click()
    #保存cookies到文件

    time.sleep(3)
    driver.get("http://10.16.193.194:8080/zh-CN/MES/SfcWorkCenter")
    save_cookies(driver)


def get_url_with_cookies():
    project_path=os.path.dirname(os.getcwd())
    file_path=project_path+"\\cookies\\"
    cookies_file=file_path+"mes.cookies"

    mes_cookies_file=open(cookies_file,"r")

    mes_cookies_str=mes_cookies_file.readline()

    mes_cookies_dict=json.loads(mes_cookies_str)

    driver.get("http://10.16.193.194:8080/Account/Login?ReturnUrl=%2f")
    driver.delete_all_cookies()

    for cookie in mes_cookies_dict:
        driver.add_cookie(cookie)

    #验证
    sucess_url="http://10.16.193.194:8080/"
    driver.get(sucess_url)

    # print(driver.current_url)

    time.sleep(2)
    if driver.current_url==sucess_url:
        print("login sucess !!!")


if __name__=='__main__':
    # login()
    get_url_with_cookies()
    driver.close()