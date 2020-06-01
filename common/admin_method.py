from ECShop.common.base import Base
from selenium import webdriver
import time

url = "http://ecshop.itsoso.cn/admin"


def open_browser(browser='chrome'):
    '''
    封装浏览器,可以选 谷歌/火狐/ie
    :param browser:  浏览器名字
    :return:
    '''
    browser = browser.lower()
    if browser == 'chrome':
        #对谷歌浏览器进行加载项配置
        user_data = '--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\'
        # 加载配置数据
        option = webdriver.ChromeOptions()
        option.add_argument(user_data)
        # 启动浏览器
        driver = webdriver.Chrome(chrome_options=option)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'ie':
        driver = webdriver.Ie()
    else:
        print('请选择正确的浏览器,例如:Chrome')
        driver = None

    driver.switch_to.default_content()
    return driver

#menu-ul > li.icon-promotion.active

class AddGoodsMethod(Base):

    menu_list_loc = ("css selector", "#menu-ul>li.icon-goods")  # 商品管理
    goods_list_loc = ("link text", "添加新商品")  # 添加新商品
    menu_frame_loc = ("xpath", "//*[@id='menu-frame']")  # 商品管理表单

    def switch_menu_frame(self):
        """
        进入商品管理表单进行操作,并返回上一层表单
        :return:
        """
        self.switch_to_frame(self.menu_frame_loc)
        self.click(self.menu_list_loc)

        self.click(self.goods_list_loc)
        self.switch_to_parent_frame()


if __name__ == '__main__':
    driver = open_browser()
    login = AddGoodsMethod(driver)
    login.open_url(url)
    login.switch_menu_frame()
