'''
browse_goods_page.py 测试类
封装业务层

author:llj
'''
import time
import unittest
import ddt
import xlrd

from ECShop.common.base import open_browser
from ECShop.page.browse_goods_page import BrowseGoods,url
from ECShop.common.operationexcel import OperationExcel




class TestBrowseGoods(unittest.TestCase):
    # 特殊方法
    def setUp(self) -> None:
        """
        执行每个用例之前执行
        打开浏览器,打开被测网址
        :return:
        """
        driver = open_browser()
        self.browse = BrowseGoods(driver)
        self.browse.open_url(url)
    def tearDown(self) -> None:
        """
        执行每个用例之后执行
        关闭浏览器
        :return:
        """
        self.browse.close()
    # 测试用例---浏览所有的商品

    def test_all_goods(self):
        """
        浏览所有商品
        :return:
        """
        self.browse.browse_all_goods()


    # def test_click_goods(self):
    #     """
    #     点击任意商品
    #     :param goods_name:
    #     :return:
    #     """
    #     try:
    #         self.browse.chioce_goods(names["goodsname"])
    #     except AssertionError:
    #         print(f'没有{names["goodsname"]}商品')
    #         raise AssertionError



if __name__ == '__main__':
    unittest.main()