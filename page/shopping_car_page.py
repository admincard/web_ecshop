import time

from ECShop.common.base import Base
from ECShop.common.base import open_browser

# url = "http://localhost:8080/ecshop/"
url = "http://ecshop.itsoso.cn/"


class ShoppingCarPage(Base):
    """
    封装表现层
    制作定位器
    """
    # 商品定位
    item_loctor = ('class name', "goodsItem")

    # 购买按钮
    buy_locator = ('css selector', "td.td1 > a")

    # 购物车按钮
    # shop_car_link_locator = ("partial_link_text", "购物车")
    shop_car_link_locator = ("css selector", "a[title='查看购物车']")
    # 继续购物
    continue_shop_locator = (
        "css selector",
        "div.flowBox > table > tbody > tr > td:nth-child(1) > a"
    )
    # 清空购物车按钮
    clear_button_locator = ("css selector", "input[type='button']")
    # 更新购物车按钮
    update_button_locator = ("css selector", "input[name = 'submit']")
    # 结算按钮
    go_shopping_button_locator = (
        "css selector",
        "div.flowBox > table > tbody > tr > td:nth-child(2) > a"
    )
    # 商品列表
    shop_list_locator = (
        "css selector",
        "#formCart > table:nth-child(1) > tbody > tr"
    )
    # 修改购买数量输入框
    change_count_input_locator = (
        "css selector",
        "#formCart > table:nth-child(1) > tbody > tr> td:nth-child(5) > input"
    )
    # 删除按钮
    del_shop_button_locator = (
        "link text",
        "删除"
    )
    # 商品详情
    shop_img_locator = (
        "css selector",
        "#formCart > table:nth-child(1) > tbody > tr:nth-child > td:nth-child(1) > a:nth-child(1)"
    )

    def item_click(self):
        """
        点击商品
        :return:
        """
        self.click(self.item_loctor)

    def buy_click(self):
        """
        点击购买
        :return:
        """
        self.click(self.buy_locator)

    def shop_link_click(self):
        """
        点击购物车
        :return:
        """
        self.click(self.shop_car_link_locator)

    def continue_shop_click(self):
        """
        点击继续购物
        :return:
        """
        self.click(self.continue_shop_locator)

    def clear_button_click(self):
        """
        点击清空购物车
        :return:
        """
        self.click(self.clear_button_locator)

    def update_button_click(self):
        """
        点击更新购物车按钮
        :return:
        """
        self.click(self.update_button_locator)

    def go_shopping_click(self):
        """
        点击结算按钮
        :return:
        """
        self.click(self.go_shopping_button_locator)

    def shop_list(self):
        """
        获取购物车商品列表
        :return: 返回list,没有则返回False
        """
        shop_list = self.find_elements(self.shop_list_locator)
        if isinstance(shop_list, list) and len(shop_list) > 0:
            return shop_list
        else:
            return False

    def change_count_input(self, value):
        """
        获取数量输入框
        :return:
        """
        change_count_input = self.send_keys(self.change_count_input_locator, value)
        # if isinstance(change_count_input, list) and len(change_count_input) > 0:
        #     return change_count_input
        # else:
        return change_count_input

    def del_shop_button_click(self):
        """
        点击删除
        :return:
        """
        self.click(self.del_shop_button_locator)

    def shop_img_click(self):
        """
        点击商品图片
        :return:
        """
        self.click(self.shop_img_locator)


if __name__ == '__main__':
    driver = open_browser()
    sc = ShoppingCarPage(driver)
    sc.open_url(url)

    sc.item_click()
    time.sleep(2)

    sc.buy_click()
    time.sleep(2)

    # sc.clear_button_click()
    print(sc.shop_list())

    # sc.change_count_input('3')
    #
    # sc.update_button_click()
    # time.sleep(2)
    #
    # sc.go_shopping_click()
    # time.sleep(2)
    # sc.back()

    # sc.shop_img_click()
    # time.sleep(2)
    # sc.back()

    sc.del_shop_button_click()

    time.sleep(3)
    alert = sc.switch_to_alert
    print(alert)
    alert.accept()

    # sc.back()
    # time.sleep(2)

    # sc.shop_link_click()
    # time.sleep(2)
    #
    # sc.continue_shop_click()
    # time.sleep(2)
    #
    # sc.back()
    # time.sleep(2)
