'''
user_address_page.py   个人中心收货地址
封装业务层

author:llj
'''
import unittest
import time
import ddt
from ECShop.common.admin_method import open_browser
from ECShop.page.user_address_page import Address
from ECShop.common.operationexcel import OperationExcel

oper_excel=OperationExcel(r'E:\个人练习\12_自动化项目_llj\ECShop\data\useraddress.xlsx')
text_data=oper_excel.get_data_for_dict()

url = "http://ecshop.itsoso.cn/user.php?act=address_list"

@ddt.ddt
class UserAddress(unittest.TestCase):
    # 特殊方法
    def setUp(self) -> None:
        '''
        打开浏览器,打开测试网址
        登录被测网址进入个人中心,收货地址
        '''
        driver = open_browser()
        self.address = Address(driver)
        self.address.open_url(url)
        time.sleep(1)

    def tearDown(self) -> None:
        '''关闭浏览器'''

        self.address.close()

    '''编写测试用例'''

    @ddt.data(*text_data)
    def test_case_1(self, data: dict):
        '''新增收货地址'''
        """
        新增收货地址
        :param data:读取表格内容
        :return:
        """
        nu = self.address.count()
        print(f'新增之前地址数量:{nu}')
        if nu<5:

            self.address.choice_conutry(data["country"], 'add')
            time.sleep(3)
            self.address.choice_province(data["province"], 'add')
            time.sleep(3)
            self.address.choice_city(data["city"], 'add')
            time.sleep(3)
            self.address.choice_district(data["district"], 'add')
            self.address.input_user(data["user"], 'add')
            self.address.input_mail(data["mail"], 'add')
            self.address.input_address(data["address"], 'add')
            self.address.input_post(data["post_nu"], 'add')
            self.address.input_tel(data["tel"], 'add')
            self.address.input_phone(data["phone"], 'add')

            time.sleep(3)
            self.address.click_add()
            time.sleep(3)
            new_nu = self.address.count()
            print(f'新增之后地址数量:{new_nu}')
            # 以时间为图片命名
            now = time.strftime("%Y_%m_%d %H_%M_%S")
            file_path = f"../image/{now}.jpg"
            try:
                self.assertEqual(nu + 1, new_nu, msg='操作失败')  # 断言
            except AssertionError:
                self.address.screenshot(file_path)
                raise AssertionError
        else:
            print('收货地址添加已达上限')


    @ddt.data(*text_data)
    def test_case_2(self,data:dict):
        '''修改收货地址'''
        """
        修改收货地址
        :param data:读取表格内容
        :return:
        """
        #输入修改内容
        self.address.choice_conutry(data["country"], 'rec')
        time.sleep(3)
        self.address.choice_province(data["province"], 'rec')
        time.sleep(3)
        self.address.choice_city(data["city"], 'rec')
        time.sleep(3)
        self.address.choice_district(data["district"], 'rec')
        self.address.input_user(data["user"], 'rec')
        self.address.input_mail(data["mail"], 'rec')
        self.address.input_address(data["address"],'rec')
        self.address.input_post(data["post_nu"],'rec')
        self.address.input_tel(data["tel"],'rec')
        self.address.input_phone(data["phone"],'rec')
        self.address.click_modify()

        #定位修改后的 地址信息
        result_loc = ("name", "address")
        #修改的地址信息--vlaue值与输入的相同
        result = self.address.is_value_in_element(result_loc,data["address"])
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        file_path = f"../image/{now}.jpg"
        try:
            self.assertTrue(result, msg="断言失败")
        except AssertionError:
            self.login.screenshot(file_path)
            raise AssertionError


    def test_case_3(self):
        '''删除一条地址,并确认'''
        nu = self.address.count()
        print(f'删除之前地址数量:{nu}')
        self.address.click_del()
        time.sleep(3)
        new_nu = self.address.count()
        print(f'删除之后地址数量:{new_nu}')
        # 以时间为图片命名
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        file_path = f"../image/{now}.jpg"
        try:
            self.assertEqual(nu-1,new_nu, msg='操作失败')  # 断言
        except AssertionError:
            self.address.screenshot(file_path)
            raise AssertionError

    def test_case_4(self):
        '''删除一条地址,并取消'''
        nu = self.address.count()
        print(f'删除之前地址数量:{nu}')
        self.address.click_nodel()
        time.sleep(3)
        new_nu = self.address.count()
        print(f'取消删除之后地址数量:{new_nu}')
        # 以时间为图片命名
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        file_path = f"../image/{now}.jpg"
        try:
            self.assertEqual(nu,new_nu, msg='操作失败')  # 断言
        except AssertionError:
            self.address.screenshot(file_path)
            raise AssertionError

if __name__ == '__main__':
    unittest.main()