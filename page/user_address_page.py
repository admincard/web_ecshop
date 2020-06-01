'''
user_address_page.py   个人中心收货地址
继承base类
封装表现层
封装操作层

author:llj
'''
import time

from ECShop.common.base import Base
from ECShop.common.admin_method import open_browser

url = 'http://ecshop.itsoso.cn/user.php?act=address_list'

class Address(Base):

    """封装表现层---制作定位器"""
    #配送区域-国家-下拉框
    country_loc = ('name','country')
    #配送区域-省份-下拉框
    province_loc = ('name', 'province')
    #配送区域-市-下拉框
    city_loc = ('name', 'city')
    #配送区域-区-下拉框
    district_loc = ('name', 'district')
    #收货人姓名
    user_loc = ('name','consignee')
    #电子邮件地址
    mail_loc = ('name','email')
    #详细地址
    address_loc = ('name','address')
    #邮政编码
    post_nu_loc = ('name','zipcode')
    #电话
    tel_loc = ('name','tel')
    #手机
    phone_loc = ('name','mobile')
    #新增收货地址 按钮
    add_address_loc = ('css selector','input[value="新增收货地址"]')
    #确认修改 按钮
    confirm_loc = ('css selector','input[value="确认修改"]')
    #删除按钮
    del_loc = ('css selector','input[value="删除"]')

    """封装操作层"""
    def count(self):
        '''统计当前收货地址条数'''
        nos = self.find_elements(self.user_loc)
        num_value = []
        for i  in nos:
            values = i.get_attribute('value')
            num_value.append(values)
        num = len(num_value)
        return num

    def choice_conutry(self,country,method):
        """
        下拉框根据选项值 选择国家
        :param country: 国家名
        :param method: 操作的方式,rec-->修改,add-->新增
        :return:
        """
        cs = self.find_elements(self.country_loc)  #所有配送区域-国家-下拉框 定位器
        num = len(cs)
        if method=='rec' and num > 1:
            self.select_text(self.country_loc,country)  #已存在地址,修改地址列表第一条
        elif method=='add':
            loc = ("id",f"selCountries_{num-1}")  # 重新制定新增操作的定位器
            self.select_text(loc,country)

    def choice_province(self,province,method):
        """
         下拉框根据选项值 选择省份
        :param province: 省份
        :param method: 操作的方式,rec-->修改,add-->新增
        :return:
        """
        provinces = self.find_elements(self.province_loc)
        num = len(provinces)
        if method == 'rec' and num > 1:
            self.select_text(self.province_loc,province)  # 已存在地址,修改地址列表第一条
        elif method == 'add':
            loc = ("id", f"selProvinces_{num - 1}")  # 重新制定新增操作的定位器
            self.select_text(loc,province)

    def choice_city(self,city,method):
        """
        下拉框根据选项值 选择市
        :param city: 市
        :param method: 操作的方式,rec-->修改,add-->新增
        :return:
        """
        citys = self.find_elements(self.city_loc)
        num = len(citys)
        if method == 'rec' and num > 1:
            self.select_text(self.city_loc,city)  # 已存在地址,修改地址列表第一条
        elif method == 'add':
            loc = ("id", f"selCities_{num - 1}")  # 重新制定新增操作的定位器
            self.select_text(loc,city)

    def choice_district(self,district,method):
        """
        下拉框根据选项值 选择区
        :param district: 区名
        :param method: 操作的方式,rec-->修改,add-->新增
        :return:
        """
        districts = self.find_elements(self.district_loc)
        num = len(districts)
        if method == 'rec' and num > 1:
            self.select_text(self.district_loc,district)  # 已存在地址,修改地址列表第一条
        elif method == 'add':
            loc = ("id", f"selDistricts_{num - 1}")  # 重新制定新增操作的定位器
            self.select_text(loc,district)

    def input_user(self,name,method):
        """
        输入收货人姓名
        :param name: 收货人姓名
        :param method: 操作的方式,rec-->修改,add-->新增
        :return:
        """
        user = self.find_elements(self.user_loc)
        num = len(user)
        if method == 'rec' and num > 1:
            self.send_keys(self.user_loc,name)  # 已存在地址,修改地址列表第一条
        elif method == 'add':
            loc = ("id", f"consignee_{num - 1}")  # 重新制定新增操作的定位器
            self.send_keys(loc,name)

    def input_mail(self,data,method):
        """
        输入邮箱号
        :param mail:邮箱号
        :param method: 操作的方式,rec-->修改,add-->新增
        :return:
        """
        mails = self.find_elements(self.mail_loc)  #所有邮箱输入框
        num = len(mails)
        if method == 'rec' and num > 1:
            self.send_keys(self.mail_loc,data)  # 已存在地址,修改地址列表第一条
        elif method == 'add':
            loc = ("id", f"email_{num - 1}")  # 重新制定新增操作的定位器
            self.send_keys(loc,data)

    def input_address(self,text,method):
        """
        输入收货地址
        :param text:收货地址
        :param method: 操作的方式,rec-->修改,add-->新增
        :return:
        """
        address = self.find_elements(self.address_loc)
        num = len(address)
        if method == 'rec' and num > 1:
            self.send_keys(self.address_loc,text)  # 已存在地址,修改地址列表第一条
        elif method == 'add':
            loc = ("id", f"address_{num - 1}")  # 重新制定新增操作的定位器
            self.send_keys(loc,text)

    def input_post(self,nu,method):
        """
        输入邮政编码
        :param nu:邮政编码
        :param method: 操作的方式,rec-->修改,add-->新增
        :return:
        """
        posts = self.find_elements(self.post_nu_loc)
        num = len(posts)
        if method == 'rec' and num > 1:
            self.send_keys(self.post_nu_loc,nu)  # 已存在地址,修改地址列表第一条
        elif method == 'add':
            loc = ("id", f"zipcode_{num - 1}")  # 重新制定新增操作的定位器
            self.send_keys(loc,nu)

    def input_tel(self,tel,method):
        """
        输入电话号码
        :param tel:电话号码
        :param method: 操作的方式,rec-->修改,add-->新增
        :return:
        """
        nus = self.find_elements(self.tel_loc)
        num = len(nus)
        if method == 'rec' and num > 1:
            self.send_keys(self.tel_loc,tel)  # 已存在地址,修改地址列表第一条
        elif method == 'add':
            loc = ("id", f"tel_{num - 1}")  # 重新制定新增操作的定位器
            self.send_keys(loc,tel)

    def input_phone(self,phone,method):
        """
        输入手机号码
        :param phone:手机号码
        :param method: 操作的方式,rec-->修改,add-->新增
        :return:
        """
        phones = self.find_elements(self.phone_loc)
        num = len(phones)
        if method == 'rec' and num > 1:
            self.send_keys(self.phone_loc,phone)  # 已存在地址,修改地址列表第一条
        elif method == 'add':
            loc = ("id", f"tel_{num - 1}")  # 重新制定新增操作的定位器
            self.send_keys(loc,phone)

    def click_add(self):
        """
        点击 新增收货地区
        :return:
        """
        self.click(self.add_address_loc)

    def click_modify(self,index=0):
        """
        点击 确认修改
        :param index: 根据索引选择的操作项,默认第一条
        :return:
        """
        self.find_element(self.confirm_loc).click()


    def click_del(self):
        """
        点击 删除并确认删除
        :param index: 根据索引选择的操作项,默认第一条
        :return:
        """
        self.click(self.del_loc)
        time.sleep(3)
        self.switch_to_alert_accept()

    def click_nodel(self):
        """
        点击 删除并取消操作
        :param index: 根据索引选择的操作项,默认第一条
        :return:
        """
        self.click(self.del_loc)
        time.sleep(3)
        self.switch_to_alert_dismiss()

if __name__ == '__main__':
    driver = open_browser()
    add = Address(driver)
    add.open_url(url)

    # add.choice_conutry('中国','add')
    # time.sleep(3)
    # add.choice_province("北京",'add')
    # time.sleep(3)
    # add.choice_city("北京市",'add')
    # time.sleep(3)
    # add.choice_district("东城区",'add')
    # time.sleep(3)
    # add.input_user("11111",'add')
    # time.sleep(3)
    # add.input_mail("admin123@qq.com",'add')
    # time.sleep(3)
    # add.input_address("00000000000",'add')
    # time.sleep(3)
    # add.input_tel("133333",'add')
    # time.sleep(3)
    # add.input_phone("13375554555",'add')
    # add.click_add()
    # add.click_modify()
    # add.click_nodel()