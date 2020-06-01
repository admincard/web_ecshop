'''
register_page.py   个人中心收货地址
继承base类
封装表现层
封装操作层

author:llj
'''
import time

from ECShop.common.base import Base,open_browser

url = "http://ecshop.itsoso.cn/user.php?act=register"

class RegsiterPage(Base):
    '''封装表现层---制作定位器'''

    # 用户名的输入框
    username_loc = ("id", "username")
    # 邮箱的输入框
    email_loc = ("id", "email")
    # 密码的输入框
    password_loc = ("name", "password")
    # 确认密码的输入框
    conformpassword_loc = ("name", "confirm_password")
    # 手机的输入框
    phone_loc = ("name", "extend_field5")
    # 密码提示问题 下拉框
    selquestion_loc = ("name", "sel_question")
    # 密码问题的输入框
    passwd_answer_loc = ("name", "passwd_answer")
    # 用户协议 复选框
    checked_loc = ("name", "agreement")
    # 用户协议 链接
    read_checked_loc = ('link text','用户协议')
    # 确认注册的按钮
    submit_loc = ("name", "Submit")

    # 注册后页面登陆账户
    use_loc= ('class name','f4_b')

    # 我已有账号，我要登录的链接
    relogin_loc = ("link text", "我已有账号，我要登录")
    # 您忘记密码了吗？的链接
    Misspassword_loc = ("link text", "您忘记密码了吗？")

    """封装操作层"""
    def input_username(self, text):
        """
        输入注册用户名
        :param text: 用户名
        :return:
        """
        self.send_keys(self.username_loc, text)

    def input_email(self, text):
        """
        输入邮箱号
        :param text: 邮箱号
        :return:
        """
        self.send_keys(self.email_loc, text)

    def input_password(self, text):
        """
        输入注册密码
        :param text: 密码
        :return:
        """
        self.send_keys(self.password_loc, text)

    def input_confrompw(self, text):
        """
        输入确认密码
        :param text: 密码
        :return:
        """
        self.send_keys(self.conformpassword_loc, text)

    def input_phone(self, text):
        """
        输入手机号码
        :param text: 手机号
        :return:
        """
        self.send_keys(self.phone_loc, text)

    def select_selquestion(self,index):
        """
        根据索引进行密保问题的选择
        :param index:索引值
        :return:
        """
        self.select_index(self.selquestion_loc,index)

    def input_passwd_answer(self,text):
        """
        输入密保问题的回答
        :param text:密保预置问题答案
        :return:
        """
        self.send_keys(self.passwd_answer_loc,text)

    def select_checked(self):
        """
        选择已阅用户协议
        先判断,未选就点击,已选则不操作
        :return:
        """
        element = self.find_element(self.checked_loc)
        if element.is_selected():
            pass
        else:
            element.click()
    def red_checked(self):
        """
        阅读用户协议,并返回
        :return:
        """
        element = self.find_element(self.read_checked_loc)
        element.click()
        element.back()

    def click_register(self):
        """点击登录按钮"""
        self.click(self.submit_loc)

    def get_user(self):
        """
        获取注册成功后,登录的账户名 文本信息
        :return:
        """
        element = self.find_element(self.use_loc)
        result = element.text
        return result

if __name__ == '__main__':

    driver = open_browser()
    register = RegsiterPage(driver)
    register.open_url(url)
    time.sleep(2)
    register.input_username("b123")
    register.input_email("34353334@123.com")
    time.sleep(2)
    register.input_password("123456")
    register.input_confrompw("123456")
    time.sleep(2)
    register.input_phone("13398878787")
    time.sleep(2)
    register.click_register()
    time.sleep(3)

    register.close()