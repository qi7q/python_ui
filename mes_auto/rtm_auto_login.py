from selenium import webdriver
import json
import os
import time

#chrome
path='D:\python_work\python_ui\chromedriver.exe'
driver=webdriver.Chrome(path)

#maxsize window
driver.maximize_window()



def save_cookies():
    project_path=os.path.dirname(os.getcwd())
    file_path=project_path+"\\cookies\\"

    #如果不存在则创建文件路径
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    cookies_file=file_path+"jd.cookies"

    #获取cookies
    cookies=driver.get_cookies()
    print(cookies)

    #保存cookies到文件
    with open(cookies_file,"w") as f:
        json.dump(cookies,f)

    print(cookies)


def login():

    try:
        #进入RTM登录页面
        driver.get("http://10.16.193.194:8080/Account/Login?ReturnUrl=%2f")
        time.sleep(2)

        driver.find_element_by_id("userinput").send_keys("qqcc")
        driver.find_element_by_id("passwordinput").send_keys("1")

        time.sleep(2)
        driver.find_element_by_id("btnlogin").click()
        time.sleep(3)

        driver.get("http://10.16.193.194:8080/zh-CN/MES/SfcWorkCenter")
        time.sleep(3)
        save_cookies()
    finally:
        time.sleep(3)

#使用cookies跳过登录验证
def get_login_with_cookies():
    project_path=os.path.dirname(os.getcwd())
    file_path=project_path+"\\cookies\\"
    cookies_file=file_path+"jd.cookies"

    mes_cookies_file=open(cookies_file,"r")
    mes_cookies_str=mes_cookies_file.readline()

    mes_cookies_dict=json.loads(mes_cookies_str)

    driver.get("http://10.16.193.194:8080/Account/Login?ReturnUrl=%2f")
    driver.delete_all_cookies()

    for cookie in mes_cookies_dict:
        driver.add_cookie(cookie)

    #验证是否登录成功
    login_success_url="http://10.16.193.194:8080/zh-CN/MES/SfcWorkCenter"
    driver.get(login_success_url)
    if driver.current_url==login_success_url:
        print("恭喜 登录成功~~~~~")

    #调用截图方法
    screenshot(driver)


#截图方法
def screenshot(driver,path=None):
    project_path=os.path.dirname(os.getcwd())
    file_path=project_path+"\\images\\"

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    image_name=time.strftime("%Y%m%d-%H%M%S",time.localtime())+".png"

    if path==None:
        driver.save_screenshot(file_path+image_name)

#主入口
if __name__=="__main__":
    # login()
    get_login_with_cookies()