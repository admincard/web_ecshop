'''
order_pay_page.py 测试类
封装业务层

author:llj
'''
import time
import unittest

from ECShop.common.base import open_browser
from ECShop.page.order_pay_page import OrderPay_page
from ECShop.page.shopping_car_page import ShoppingCarPage
from ECShop.scripts.login_folw import LoginFlow

url = "http://ecshop.itsoso.cn/"

class TestOrderPay(unittest.TestCase):
    # 特殊方法
    def setUp(self) -> None:
        '''
        打开浏览器,打开测试网址
        登录被测网址
        '''
        driver = open_browser()
        self.orderPay = OrderPay_page(driver)  #下单支付对象
        self.car = ShoppingCarPage(driver)     #购物车对象
        self.orderPay.open_url(url)
        lf = LoginFlow(driver)
        lf.login_not_remember_password("user123", '123456')
        lf.back_homepage()
        time.sleep(3)

    def tearDown(self) -> None:
        '''关闭浏览器'''

        self.orderPay.close()

    '''编写测试用例'''

    def test_orderpay(self):
        """
        添加商品入购物车进行结算
        :return:
        """
        # 点击购物车
        self.car.item_click()  # 点击商品
        self.car.buy_click()  # 点击购买
        self.car.go_shopping_click()  # 点击去结算
        # 选择快递方式 申通
        self.orderPay.click_radio_ST()
        # 选择 银行卡支付
        self.orderPay.click_bank_pay()
        time.sleep(2)
        # 获取应付款金额
        price = self.orderPay.get_pay_money()
        # 点击提交订单
        self.orderPay.click_submit()
        time.sleep(3)


        '''提交订单后页面'''

        # 获取生成的订单号
        num = self.orderPay.get_order_nu()
        # 获取实际付款金额
        really_price = self.orderPay.get_really_pay()
        #进入用户中心
        self.orderPay.click_usercore()
        #点击我的订单号
        self.orderPay.click_userno()
        #获取订单列表-订单号
        really_num = self.orderPay.get_order_no()

        # 以时间为图片命名
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        file_path = f"../image/{now}.jpg"
        try:
            self.assertEqual(price, really_price) and self.assertEqual(num,really_num)
        except AssertionError:
            self.orderPay.screenshot(file_path)
            raise AssertionError


if __name__ == '__main__':
    unittest.main()
