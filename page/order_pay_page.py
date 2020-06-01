'''
order_pay_page.py 下单支付   需要继承Base类
2.封装表现层
3.封装操作层

author:llj
'''
import time

from ECShop.common.base import Base, open_browser
from ECShop.page.shopping_car_page import ShoppingCarPage
from ECShop.scripts.login_folw import LoginFlow

url='http://ecshop.itsoso.cn'  #前台被测地址

class OrderPay_page(Base):

    '''制作 订单页面定位器'''
    #商品列表--修改
    modify_list_loc=('css selector','#theForm > div:nth-child(2) > h6 > a')
    #收货人信息--修改
    modify_receiver_loc=('css selector','#theForm > div:nth-child(4) > h6 > a')
    #单选框--申通快递
    radio_ST_loc=('xpath','//*[@id="shippingTable"]/tbody/tr[2]/td[1]/input')
    #单选框--邮局平邮
    radio_post_loc = ('xpath', '//*[@id="shippingTable"]/tbody/tr[3]/td[1]/input')
    #复选框--配送是否需要保价-->不能使用
    # checkbox_Insured_loc=('xpath','//*[@id="shippingTable"]/tbody/tr[4]/td/label')

    #单选框--天工收银--支付宝
    alipay_loc = ('id','alipay')
    #单选框-- 天工收银--微信
    wxpay_loc = ('id','wxpay')
    #单选框--余额支付
    radio_balance_loc=('xpath','//*[@id="paymentTable"]/tbody/tr[4]/td[1]/input')
    #单选框--银行汇款/转帐
    radio_bank_loc=('xpath','//*[@id="paymentTable"]/tbody/tr[5]/td[1]/input')
    #单选框--货到付款----->不能使用
    radio_res_loc=('xpath','//*[@id="paymentTable"]/tbody/tr[6]/td[1]/input')
    # 单选框--支付宝
    z_loc = ('xpath','//*[@id="paymentTable"]/tbody/tr[7]/td[1]/input')

    #单选框--不要包装
    radio_nopack_loc=('xpath','//*[@id="packTable"]/tbody/tr[2]/td[1]/input')
    #单选框--精品包装
    radio_pack_loc=('xpath','//*[@id="packTable"]/tbody/tr[3]/td[1]/input')

    #单选框--不要贺卡
    radio_nocard_loc=('xpath','//*[@id="cardTable"]/tbody/tr[2]/td[1]/input')
    #单选框--祝福贺卡
    radio_card_loc=('xpath','//*[@id="cardTable"]/tbody/tr[3]/td[1]/input')
    #输入框--祝福语
    card_message_loc=('xpath','//*[@id="cardTable"]/tbody/tr[4]/td[3]/textarea')

    # 输入框--使用余额
    pay_balance_loc=('xpath','#ECS_SURPLUS')
    # 账户余额
    user_balance_loc=('xpath','#ECS_SURPLUS')

    # 下拉框--选择已有红包
    red_select_loc=('xpath','//*[@id="ECS_BONUS"]')
    # 输入框--红包序列号
    red_input_loc=('xpath','//*[@id="theForm"]/div[13]/table/tbody/tr[2]/td[2]/input[1]')
    # 按钮--验证红包
    red_submit_loc=('xpath','//*[@id="theForm"]/div[13]/table/tbody/tr[2]/td[2]/input[2]')

    #复选框--开发票
    bill_checkbox_loc=('xpath','//*[@id="ECS_NEEDINV"]')
    #下拉框--发票类型
    bill_select_loc=('xpath','//*[@id="ECS_INVTYPE"]')
    #输入框--发票抬头
    bill_title_loc=('xpath','//*[@id="ECS_INVPAYEE"]')
    #下拉框--发票内容
    bill_data_loc=('css selector','#ECS_INVCONTENT')
    #输入框--订单附言
    input_data_loc=('xpath','//*[@id="postscript"]')
    # 单选框--等待所有商品备齐后再发-缺货处理
    radio_allgood_loc=('xpath','//*[@id="theForm"]/div[13]/table/tbody/tr[5]/td[2]/label[1]/input')
    # 单选框--取消订单-缺货处理
    radio_cancel_loc = ('xpath','//*[@id="theForm"]/div[13]/table/tbody/tr[5]/td[2]/label[2]/input')
    # 单选框--与店主协商-缺货处理
    radio_Q_loc=('xpath','//*[@id="theForm"]/div[13]/table/tbody/tr[5]/td[2]/label[3]/input')

    # 应付款金额
    pay_money_loc=('xpath','//*[@id="ECS_ORDERTOTAL"]/table/tbody/tr[3]/td/font')
    # 按钮--提交订单
    submit_order_loc=('xpath','//*[@id="theForm"]/div[15]/div[2]/input[1]')

    '''提交订单后页面'''
    # 订单号
    order_no_loc = ('css selector', 'body > div:nth-child(7) > div > h6 > font')
    # 选择的配送方式
    Delivery_loc = ('xpath','/html/body/div[6]/div/table/tbody/tr[1]/td/strong[1]')
    # 选择的支付方式
    pay_loc = ('xpath','/html/body/div[6]/div/table/tbody/tr[1]/td/strong[2]')
    # 实际付款金额
    money_loc = ('xpath', '/html/body/div[6]/div/table/tbody/tr[1]/td/strong[3]')
    # 用户中心 按钮
    user_center_loc = ('link text', '用户中心')

    '''用户中心页面'''
    #我的订单
    my_order_loc = ('link text', '我的订单')
    #第一条订单号
    nu_loc = ('xpath', '/html/body/div[6]/div[2]/div/div/div/table/tbody/tr[1]/td[1]/a')


    '''操作层封装'''
    def modify_goodslist(self):
        '''
        点击商品列表 修改
        返回 订单页
        :return:
        '''
        self.click(self.modify_list_loc)
        self.back()
    def modify_remsg(self):
        '''
        收货人信息--修改
        返回 订单页
        :return:
        '''
        self.click(self.modify_receiver_loc)
        self.back()
    def click_radio_ST(self):
        '''
        判断快递方式: 申通快递 是否被选中
        没有选中就点击
        :return:
        '''
        ST=self.find_element(self.radio_ST_loc)
        if ST.is_selected():
            pass
        else:
            ST.click()

    def click_radio_post(self):
        '''
        判断快递方式: 邮政 是否被选中
        没有选中就点击
        :return:
        '''
        post=self.find_element(self.radio_post_loc)
        if post.is_selected():
            pass
        else:
            post.click()

    def click_alipay(self):
        '''
        判断支付方式:天工收银--支付宝 是否被选中
        没有选中就点击
        :return:
        '''
        alipay_pay=self.find_element(self.alipay_loc)
        if alipay_pay.is_selected():
            pass
        else:
            alipay_pay.click()

    def click_wxpay(self):
        '''
        判断支付方式:天工收银--微信 是否被选中
        没有选中就点击
        :return:
        '''
        wxpay_pay=self.find_element(self.wxpay_loc)
        if wxpay_pay.is_selected():
            pass
        else:
            wxpay_pay.click()


    def click_balance_pay(self):
        '''
        判断支付方式:余额支付 是否被选中
        没有选中就点击
        :return:
        '''
        balance_pay=self.find_element(self.radio_balance_loc)
        if balance_pay.is_selected():
            pass
        else:
            balance_pay.click()

    def click_bank_pay(self):
        '''
        判断支付方式:银行汇款/转账 是否被选中
        没有选中就点击
        :return:
        '''
        bank_pay=self.find_element(self.radio_bank_loc)
        if bank_pay.is_selected():
            pass
        else:
            bank_pay.click()

    def click_z_pay(self):
        '''
        判断支付方式:支付宝 是否被选中
        没有选中就点击
        :return:
        '''
        pay=self.find_element(self.z_loc)
        if pay.is_selected():
            pass
        else:
            pay.click()

    def click_nopack(self):
        '''
        判断 商品包装:不要包装 是否被选中
        没有选中就点击
        :return:
        '''
        nopack=self.find_element(self.radio_nopack_loc)
        if nopack.is_selected():
            pass
        else:
            nopack.click()

    def click_goods_pay(self):
        '''
        判断 商品包装:精品包装 是否被选中
        没有选中就点击
        :return:
        '''
        pack=self.find_element(self.radio_pack_loc)
        if pack.is_selected():
            pass
        else:
            pack.click()

    def click_nocard(self):
        '''
        判断 祝福贺卡:不要贺卡 是否被选中
        没有选中就点击
        :return:
        '''
        nocard=self.find_element(self.radio_nocard_loc)
        if nocard.is_selected():
            pass
        else:
            nocard.click()
    def click_card(self):
        '''
        判断 祝福贺卡:祝福贺卡 是否被选中
        没有选中就点击
        :return:
        '''
        card=self.find_element(self.radio_card_loc)
        if card.is_selected():
            pass
        else:
            card.click()
    def input_cardmsg(self,text):
        '''
         祝福贺卡:输入祝福贺卡文字
        :return:
        '''
        self.send_keys(self.card_message_loc,text)
    def input_pay_balance(self,price):
        '''
        输入余额支付金额
        :param pirce:  使用的余额
        :return:
        '''
        self.send_keys(self.pay_balance_loc, price)
    def get_user_money(self):
        '''
        获取当前账户可用余额
        :return:当前账户可用余额
        '''
        element=self.find_element(self.user_balance_loc)
        self.price = element.text  #账户余额值
        return self.price

    def select_redbag(self):
        '''
        下拉框  根据索引值选择红包
        :return:
        '''
        self.select_index(self.red_select_loc)
    def input_redbag_no(self,text):
        '''
        输入红包序列号
        :param text:  红包序列号
        :return:
        '''
        self.send_keys(self.red_input_loc,text)
    def chick_inspect(self):
        '''
        点击 检验红包
        :return:
        '''
        self.click(self.red_submit_loc)

    def click_checkbox_bill(self):
        '''
        不选择 开发票---复选框
        判断是否已被选择,已选就点击
        :return:
        '''
        nobill = self.find_element(self.bill_checkbox_loc)
        if nobill.is_selected():
            nobill.click()
        else:
            pass

    def click_checkbox_nobill(self):
        '''
        选择 开发票---复选框
        判断是否已被选择,已选不作操作
        :return:
        '''
        bill = self.find_element(self.bill_checkbox_loc)
        if bill.is_selected():
            pass
        else:
            bill.click()

    def choice_bill_type(self):
        '''
        下拉框 根据索引 选择发票类型
        :return:
        '''
        self.select_index(self.bill_select_loc)

    def input_bill_title(self,text):
        '''
        输入发票抬头
        :param text: 发票抬头内容
        :return:
        '''
        self.send_keys(self.bill_title_loc, text)
    def choice_bill_data(self):
        '''
        下拉框 根据索引 选择发票内容
        :return:
        '''
        self.select_index(self.bill_data_loc)
    def input_order_data(self,data):
        '''
        输入订单附言
        :param data: 订单附言
        :return:
        '''
        self.send_keys(self.input_data_loc,data)

    def wait_allgoods(self):
        '''
        选择  缺货处理--等商品备齐再发
        判断是否选择,没有选中就点击
        :return:
        '''
        wa = self.find_element(self.radio_allgood_loc)
        if wa.is_selected():
            pass
        else:
            wa.click()
    def chose_cancel(self):
        '''
        选择  缺货处理--取消订单
        判断是否选择,没有选中就点击
        :return:
        '''
        cancel = self.find_element(self.radio_cancel_loc)
        if cancel.is_selected():
            pass
        else:
            cancel.click()
    def chose_consult(self):
        '''
        选择  缺货处理--取消订单
        判断是否选择,没有选中就点击
        :return:
        '''
        consult = self.find_element(self.radio_Q_loc)
        if consult.is_selected():
            pass
        else:
            consult.click()

    def get_pay_money(self):
        '''
        获取应付款金额
        :return:应付款金额
        '''
        element = self.find_element(self.pay_money_loc)
        price = element.text  # 付款金额
        return price

    def click_submit(self):
        '''
        点击提交订单
        :return:
        '''
        self.click(self.submit_order_loc)

    """提交订单后页面 方法"""

    def get_order_nu(self):
        '''
        获取 订单号
        :return: 生成的订单号
        '''
        element = self.find_element(self.order_no_loc)
        nu= element.text  # 生成的订单号
        return nu

    def get_Delivery(self):
        '''
        获取 配送方式
        :return: 已选择的配送方式
        '''
        element = self.find_element(self.Delivery_loc)
        adds = element.text # 配送方式
        return adds

    def get_pay_type(self):
        '''
        获取 支付方式
        :return: 已选择支付方式
        '''
        element = self.find_element(self.pay_loc)
        pay_type = element.text  # 支付方式
        return pay_type

    def get_really_pay(self):
        '''
        获取 实际支付金额
        :return: 实际支付金额
        '''
        element = self.find_element(self.money_loc)
        really_pay = element.text  # 实际支付金额
        return really_pay

    def click_usercore(self):
        '''
        点击 用户中心
        :return:
        '''
        self.click(self.user_center_loc)

        #用户中心 订单号
    def click_userno(self):
        '''
        点击我的订单
        :return:
        '''
        self.click(self.my_order_loc)  #点击我的订单

    def get_order_no(self):
        '''
           获取生成的订单号
           :return: 生成的订单号
           '''
        element = self.find_element(self.nu_loc)
        new_nu = element.text   # 生成的订单号
        return new_nu

if __name__ == '__main__':
    driver = open_browser()
    OrderPay = OrderPay_page(driver)  # 下单支付对象
    car = ShoppingCarPage(driver)  # 购物车对象
    OrderPay.open_url(url)
    lf = LoginFlow(driver)
    lf.login_not_remember_password("user123", '123456')
    lf.back_homepage()
    time.sleep(3)
    car.item_click()  # 点击商品
    car.buy_click()  # 点击购买
    car.go_shopping_click()  # 点击去结算
    # 选择快递方式 申通
    OrderPay.click_radio_ST()
    # 选择 银行卡支付
    OrderPay.click_bank_pay()
    time.sleep(2)
    # 获取应付款金额
    price = OrderPay.get_pay_money()
    print(price)
    # 点击提交订单
    OrderPay.click_submit()



