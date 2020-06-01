"""
1.login_page.py 需要继承Base类
2.封装表现层
3.封装操作层
"""
from ECShop.common.base import open_browser
from ECShop.common.base import Base

url = "http://ecshop.itsoso.cn/user.php"


class LoginPage(Base):
    '''封装表现层--制作定位器'''
    # 用户名输入框
    username_loc = ('name', 'username')
    # 密码输入框
    password_loc = ('name', 'password')
    # 点击记住密码
    remember_loc = ('id', 'remember')
    # 立即登录按钮
    submit_loc = ('name', 'submit')
    # 找回密码--密码问题
    find_pw_loc = ('link text', '密码问题')
    # 找回密码--邮箱
    find_email_loc = ('link text', '邮箱')
    # 找回密码--短信验证
    find_msg_loc = ('link text', '短信验证')
    # 立即注册按钮
    register_loc = ('xpath', "/html/body/div[6]/div[2]/a/img")
    # 返回首页链接
    homepage_loc = ('link text', '首页')

    '''封装操作层'''

    def input_username(self, text):
        '''输入用户名'''
        self.send_keys(self.username_loc, text)

    def input_password(self, text):
        '''输入密码'''
        self.send_keys(self.password_loc, text)

    def rem_password(self):
        '''点击记住密码'''
        self.click(self.remember_loc)

    def click_submit(self):
        '''点击登录'''
        self.click(self.submit_loc)

    def find_password(self):
        '''找回密码 密码问题'''
        self.click(self.find_pw_loc)

    def find_email(self):
        '''找回密码 邮箱'''
        self.click(self.find_email_loc)

    def find_msg(self):
        '''找回密码 短信验证'''
        self.click(self.find_msg_loc)

    def click_register(self):
        '''点击立即注册'''
        self.click(self.register_loc)

    def click_homepage(self):
        '''点击首页'''
        self.click(self.homepage_loc)


if __name__ == '__main__':
    import time

    driver = open_browser()
    login = LoginPage(driver)
    login.open_url(url)
    time.sleep(2)
    login.input_username('user123')
    login.input_password('123456')
    time.sleep(2)
    login.click_submit()

    time.sleep(2)
    login.close()
