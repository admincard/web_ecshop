'''
1.知识点:

test_login.py 测试类 封装业务层

'''
import time
import ddt
import unittest
from ECShop.common.base import open_browser
from ECShop.page.login_page import LoginPage,url
from ECShop.common.operationexcel import OperationExcel

oper_excel=OperationExcel(r'E:\个人练习\12_自动化项目_llj\ECShop\data\textdata.xlsx')
text_data=oper_excel.get_data_for_dict()

@ddt.ddt
class TestLogin(unittest.TestCase):
    #特殊方法
    def setUp(self) -> None:
        '''打开浏览器,打开测试网址'''
        driver =open_browser()
        self.login=LoginPage(driver)
        self.login.open_url(url)
    def tearDown(self) -> None:
        '''关闭浏览器'''
        self.login.close()

    '''编写测试用例---登录验证'''
    @ddt.data(*text_data)
    def test_login(self,data:dict):
        self.login.input_username(data["username"])
        self.login.input_password(data["password"])
        self.login.click_submit()  # 点击登录
        #判断--已经登录的账户
        res_loc=("class name","f4_b")
        result=self.login.is_text_in_element(res_loc,data["username"])
        #以时间为图片命名
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        file_path = f"../image/{now}.jpg"
        try:
            self.assertEqual(result,data["expect"],msg='登录失败')  #断言
        except AssertionError:
            self.login.screenshot(file_path)
            raise AssertionError


if __name__ == '__main__':
    unittest.main()







