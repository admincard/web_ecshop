'''
register_page.py   用户注册页面
封装业务层

author:llj
'''
import time
import unittest

import ddt

from ECShop.common.base import open_browser
from ECShop.common.constructdata import Constructdata
from ECShop.common.operationexcel import OperationExcel
from ECShop.page.register_page import RegsiterPage

url = "http://ecshop.itsoso.cn/user.php?act=register"

class TestRegister(unittest.TestCase):
    # 特殊方法
    def setUp(self) -> None:
        '''
        打开浏览器,打开测试网址
        登录被测网址
        '''
        file = Constructdata()
        # 获取必填项的随机注册数据----字典格式
        self.require_datas = file.get_require_options_register_data()
        # print(self.require_datas)
        # 把字典格式转为列表格式
        require_data_list = file.get_dict_value_to_list(self.require_datas)
        # 把数据写入表格中
        OperationExcel(r"E:\个人练习\12_自动化项目_llj\ECShop\data\registerdata.xls").wirte_excel(require_data_list)
        driver = open_browser()
        self.register = RegsiterPage(driver)
        self.register.open_url(url)

    def tearDown(self) -> None:
        '''关闭浏览器'''

        self.register.close()

    '''编写测试用例'''
    def test_register(self):
        """
        输入合法数据注册---必填项
        :return:
        """
        self.register.input_username(self.require_datas["username"])  # 输入用户名
        self.register.input_email(self.require_datas["email"])        # 输入邮箱
        self.register.input_password(self.require_datas["password"])  # 输入随机密码
        self.register.input_confrompw(self.require_datas["password"]) # 再次输入刚刚生成的随机密码
        self.register.input_phone(self.require_datas["mobile"])       # 输入电话号码
        self.register.select_checked()                  # 勾选阅读用户协议
        time.sleep(4)
        self.register.click_register()                  # 点击确认按钮
        time.sleep(4)

        # 对注册成功进行断言--注册成功,自动登录
        element= self.register.get_user()
        print(element)

        # 以时间为图片命名
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        file_path = f"../image/{now}.jpg"
        try:
            self.assertEqual(element,self.require_datas["username"], msg="没有注册成功")  #断言
        except AssertionError:
            self.register.screenshot(file_path)
            raise AssertionError


if __name__ == '__main__':
    unittest.main()
