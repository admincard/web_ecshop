'''
1.addgoods_tag2_page.py  后台添加商品-详细描述 页面
2.封装表现层
3.封装操作层

author:llj
'''

from ECShop.common.base import Base
from ECShop.common.admin_method import open_browser,AddGoodsMethod
import time

url='http://ecshop.itsoso.cn/admin'

class Addgoods_tag2_page(Base):
    '''封装表现层---制作定位器'''

    #进入新商品内容 表单 定位器
    frame_loc= ('css selector','#main-frame')

    #详细描述
    description_loc=('css selector','#detail-tab')
    # 格式 下拉框
    format_loc=('xpath','//*[@id="xToolbar"]/table[4]/tbody/tr/td[2]/table/tbody/tr/td[2]/div/table/tbody/tr/td[2]')

    # 大小 下拉框
    size_loc=('xpath','//*[@id="xToolbar"]/table[4]/tbody/tr/td[3]/table/tbody/tr/td[2]/div/table/tbody/tr/td[2]')

    #进入输入框所属表单 在详细描述下面第二层
    input_frame_loc1=('css selector','#goods_desc___Frame')
    input_frame_loc=('xpath','//*[@id="xEditingArea"]/iframe')
    # 内容输入框
    input_loc=('css selector','html[dir="ltr"]>body')
    # 确定按钮
    Ysubmit_loc=('css selector','#tabbody-div > form > div > input:nth-child(2)')
    # 重置按钮
    Rsubmit_loc = ('css selector', '#tabbody-div > form > div > input:nth-child(3)')

    # ECShop管理中心 链接
    backpage_loc=('link text','ECSHOP 管理中心')


    '''封装操作层'''

    #点击 详细描述
    def description(self):
        '''
            进入表单,进入商品管理-添加新商品首页,返回上层
            进入新商品内容 表单.--详情描述
            点击详细描述,进入详细描述页面
        :return:
        '''
        login = AddGoodsMethod(driver)
        login.switch_menu_frame()  #进入表单,进入商品管理-添加新商品首页,返回上层
        self.switch_to_frame(self.frame_loc)  #进入进入新商品内容 表单
        self.click(self.description_loc) #点击详细描述
    '''
    #选择文本格式
    def Choice_format_0(self):
        """
        选择文本格式-普通
        :return:
        """
        self.select_text(self.format_loc,'普通')
    def Choice_format_1(self):
        #选择文本格式-标题 1
        self.select_text(self.format_loc,'标题 1')
    def Choice_format_2(self):
        #选择文本格式-标题 2
        self.select_text(self.format_loc,'标题 2')
    def Choice_format_3(self):
        #选择文本格式-标题 3
        self.select_text(self.format_loc,'标题 3')
    def Choice_format_4(self):
        #选择文本格式-标题 4
        self.select_text(self.format_loc,'标题 4')
    def Choice_format_5(self):
        #选择文本格式-标题 5
        self.select_text(self.format_loc,'标题 5')
    def Choice_format_6(self):
        #选择文本格式-标题 6
        self.select_text(self.format_loc,'标题 6')
    def Choice_format_7(self):
        #选择文本格式-已编排格式
        self.select_text(self.format_loc,'已编排格式')
    def Choice_format_8(self):
        #选择文本格式-地址
        self.select_text(self.format_loc,'地址')
    def Choice_format_9(self):
       #选择文本格式-段落(DIV)
        self.select_text(self.format_loc,'段落(DIV)')

    #选择字体
    def Choice_size_0(self):
        #选择字体 smaller
        self.select_text(self.size_loc,'smaller')

    def Choice_size_1(self):
        #选择字体 larger
        self.select_text(self.size_loc, 'larger')
    def Choice_size_3(self):
        #选择字体 xx-small
        self.select_text(self.size_loc,'xx-small')

    def Choice_size_4(self):
        #选择字体 x-small
        self.select_text(self.size_loc, 'x-small')
    def Choice_size_5(self):
        #选择字体 small
        self.select_text(self.size_loc,'small')

    def Choice_size_6(self):
        #选择字体 medium
        self.select_text(self.size_loc, 'medium')
    def Choice_size_7(self):
        #选择字体 large
        self.select_text(self.size_loc,'large')

    def Choice_size_8(self):
        #选择字体 x-large
        self.select_text(self.size_loc, 'x-large')
    def Choice_size_9(self):
        #选择字体 xx-large
        self.select_text(self.size_loc,'xx-large')
    '''

    #输入内容
    def input_date(self,data):
        """
        进入第三层iframe
        进入第四层iframe
        输入商品介绍
        退出表单到详细页面 iframe
        :param data: 描述商品详细内容
        :return:
        """
        self.switch_to_frame(self.input_frame_loc1)  # 进入第三层
        self.switch_to_frame(self.input_frame_loc)  # 进入输入框 表单
        self.send_keys(self.input_loc,data)         #输入内容
        self.switch_to_parent_frame()            #退出到第三层
        self.switch_to_parent_frame()            #退出到详细页面 第二层

    def click_Y(self):
        #点击确定
        self.click(self.Ysubmit_loc)
    def click_reset(self):
        #点击重置
        self.click(self.Rsubmit_loc)
    def click_back(self):
        """
        主框架iframe
        点击 ECShop管理中心
        :return:
        """
        login = AddGoodsMethod(driver)
        login.click(self.backpage_loc)

if __name__ == '__main__':

    driver = open_browser()
    login = Addgoods_tag2_page(driver)
    login.open_url(url)
    time.sleep(3)
    login.description()
    time.sleep(3)
    login.input_date('详细描述')
    login.click_Y()
    # login.click_back()  #返回ECShop管理中心
    time.sleep(2)
    login.close()