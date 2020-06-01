'''
addgoods_tag4_page.py 后台-添加商品-商品类型 页面
2.封装表现层
3.封装操作层

author:llj
'''
from ECShop.common.base import Base
from ECShop.common.admin_method import open_browser,AddGoodsMethod
import time
from ECShop.common.constructdata import Constructdata

url='http://ecshop.itsoso.cn/admin'

class Addgoods_tag4_page(Base):

    '''封装表现层---制作定位器'''

    # 进入 新 商品属性 表单 定位器
    frame_loc = ('css selector', '#main-frame')
    #商品属性
    goods_types_loc=('css selector','#properties-tab')

    #商品类型下拉选择
    select_types_loc=('xpath','//*[@id="properties-table"]/tbody/tr[1]/td[2]/select')

    # 确定按钮
    Ysubmit_loc = ('css selector', '#tabbody-div > form > div > input:nth-child(2)')
    # 重置按钮
    Rsubmit_loc = ('css selector', '#tabbody-div > form > div > input:nth-child(3)')

    #ECShop管理中心
    backpage_frame_loc=('css selector','frameset')
    # ECShop管理中心 链接

    backpage_loc = ('link text', 'ECSHOP 管理中心')

    '''封装操作层'''

    def choice_frame(self):
        '''
           进入表单,进入商品管理-添加新商品首页,返回上层
           进入新商品内容 表单.--商品属性
            点击商品属性
           :return:
                '''
        login = AddGoodsMethod(driver)
        login.switch_menu_frame()  # 进入表单,进入商品管理-添加新商品首页,返回上层
        self.switch_to_frame(self.frame_loc)  # 进入进入新商品内容 表单
        self.click(self.goods_types_loc)  # 点击商品属性
    def choice_type(self):
        """
        选择商品属性
        :return:
        """
        choice = Constructdata()   #调用随机选择商品类型
        choice.random_choice()       #随机选择
    def click_Y(self):
        """
        主框架iframe
        点击 确定
        :return:
        """
        Ysubmit = AddGoodsMethod(driver)
        Ysubmit.click(self.Ysubmit_loc)
    def click_reset(self):
        """
           主框架iframe
           点击 重置
           :return:
                """
        Rsubmit = AddGoodsMethod(driver)
        Rsubmit.click(self.Rsubmit_loc)

    def click_back(self):
        """
        主框架iframe
        点击 ECShop管理中心
        :return:
        """
        back = AddGoodsMethod(driver)
        back.click(self.backpage_loc)

if __name__ == '__main__':
    driver = open_browser()
    type = Addgoods_tag4_page(driver)
    type.open_url(url)
    time.sleep(1)

    type.choice_frame()  #进入新商品内容 表单.--商品属性

    type.choice_type()  #随机选择
    time.sleep(2)
    type.click_Y()
    # type.click_back()  # 返回ECShop管理中心
    time.sleep(2)
    type.close()