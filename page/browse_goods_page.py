'''
browse_goods_page.py 浏览所有商品

author:llj
'''
import time
from ECShop.common.base import Base

url='http://ecshop.itsoso.cn/search.php?'

class BrowseGoods(Base):
    """制作定位器"""
    #一个页面所有的商品
    all_goods_loc =('css selector','div.goodsItem>a>img')

    #翻页选择器
    choice_page_loc=('css selector','a.lis')

    """操作"""
    def get_all_goods_name(self):
        """
        获取所有商品的名称
        :return:所有商品的名称 alt属性值
        """
        elements = self.find_elements(self.all_goods_loc)
        goods_alt = []
        for element in elements:
            alt = element.get_attribute('alt')  #获取商品的名称
            goods_alt.append(alt)
        print(goods_alt)
        return goods_alt

    def make_all_goods_loc(self):
        """
        重新制作所有商品的定位器
        商品名称来定位  alt属性值
        :return: 所有商品按alt属性值定位的定位器
        """
        goods_alts=self.get_all_goods_name()
        all_goods_loc=[]
        for alt in goods_alts:
            goods_loc = ('css selector',f'img[alt="{alt}"]')  #商品名称来定位  alt属性值
            all_goods_loc.append(goods_loc)
        # print(all_goods_loc)
        return all_goods_loc

    def get_all_page_nu(self):
        """
        获取所有翻页按钮
        :return:
        """
        submit_all = self.find_elements(self.choice_page_loc)
        submit_loc = []
        for submit in submit_all:
            link_text = submit.text
            submit_loc.append(link_text)
        # print(submit_loc)
        return submit_loc

    def click_sumbit(self):
        """
        重新制作所有翻页按钮的定位器
        :return: 每个页面翻页定位器
        """
        nus = self.get_all_page_nu()
        page_sumbit = []
        for nu in nus:
            page_loc = ('link text',f'{nu}')
            page_sumbit.append(page_loc)
        # print(page_sumbit)
        return page_sumbit

    def click_onepage_goods(self):
        """
        点击一页上面所有的商品
        :return:
        """
        all_goods_loc = self.make_all_goods_loc()
        for goods_loc in all_goods_loc:  # 每个商品的新定位器
            self.click(goods_loc)  # 点击商品 进入商品详细页
            time.sleep(3)
            self.back()  # 返回商品列表页面

    def browse_all_goods(self):
        """
        浏览所有商品
        :return:
        """
        click_loc = self.click_sumbit()
        for loc in click_loc:  #遍历出每个翻页按钮的定位器
            self.click_onepage_goods()  #浏览页面所有商品
            time.sleep(3)
            self.click(loc)    #点击翻页按钮
            time.sleep(3)


    def chioce_goods(self,goods_name):
        """
        根据商品名称,选择一个商品
        :param goods_name: 商品名称
        :return:
        """
        all_goods_name = self.get_all_goods_name()
        for goods_name in all_goods_name:
            goods_loc = ('css selector',f'img[alt *="{goods_name}"]')
            self.click(goods_loc)
        else:
            print(f'没有{goods_name}商品')

if __name__ == '__main__':
    from ECShop.common.base import open_browser
    driver = open_browser()
    browse = BrowseGoods(driver)
    browse.open_url(url)

    browse.browse_all_goods()


    # browse.get_all_goods_name()
    # browse.click_sumbit()
    time.sleep(3)
    browse.close()