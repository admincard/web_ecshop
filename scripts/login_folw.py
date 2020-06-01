"""
login_flow.py 封装登录页面的业务层
"""
import time

from ECShop.page.login_page import LoginPage
from ECShop.common.base import open_browser
from ECShop.page.login_page import url


class LoginFlow:
    def __init__(self, driver):
        self.driver = driver
        self.loginpage = LoginPage(self.driver)
        self.loginpage.open_url(url)

    def login_remember_password(self, username, password):
        """记住密码登录"""
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.rem_password()
        self.loginpage.click_submit()

    def login_not_remember_password(self, username, password):
        """不记住密码登录"""
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_submit()

    def back_homepage(self):
        """返回首页"""
        self.loginpage.click_homepage()


if __name__ == '__main__':
    driver = open_browser()
    loginflow = LoginFlow(driver)
    username = "诸葛亮_9"
    password = "Test123456"
    loginflow.login_remember_password(username, password)
    time.sleep(3)
