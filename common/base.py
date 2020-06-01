'''
base.py
    1.对浏览器进行封装
    2.对selenium方法进行二次封装
'''
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_browser(browser='chrome'):
    '''
    封装浏览器,可以选 谷歌/火狐/ie
    :param browser:  浏览器名字
    :return:
    '''
    browser = browser.lower()
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'ie':
        driver = webdriver.Ie()
    else:
        print('请选择正确的浏览器,例如:Chrome')
        driver = None
    return driver


class Base:
    """
    封装selenium的基础操作
    """

    def __init__(self, driver):  # 选择浏览器
        self.driver = driver

    def open_url(self, url):
        """
        打开被测的网址,并将其最大化
        :param url: 被测试的网址
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, locator, timeout=5):
        """
        定位单个元素,返回元素
        :param locator: 元素定位器
        :param timeout: 最大等待时间
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f'没有找到目标元素{locator}')

    def find_elements(self, locator, timeout=5):
        """
        定位一组元素,返回元素
        :param locator: 元素定位器
        :param timeout: 最大等待时间
        :return:
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return elements
        except:
            print(f'没有找到目标元素{locator}')

    def click(self, locator, timeout=5):
        """
        点击元素
        :param locator:
        :param timeout:
        :return:
        """
        self.find_element(locator, timeout=timeout).click()

    def send_keys(self, locator, text, timeout=5):
        """
        输入内容
        :param locator:
        :param text:
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断元素的文本是否存在,如果存在返回true,不存在返回false
        :param locator: 元素定位器
        :param text:元素需要判断的文本--预期结果
        :param timeout: 超时时间
        :return: bool值
        """

        element = self.find_element(locator, timeout)
        try:
            text1 = element.text
            if text1 == text:
                return True
            else:

                return False
        except:
            return False

    def is_value_in_element(self, locator, value, timeout=10):
        '''
        判断元素的value值,存在返回true,不存在返回false
        :param locator:
        :param value:  元素的value值
        :param timeout:
        :return:
        '''
        element = self.find_element(locator, timeout)
        try:
            value1 = element.get_attribute('value')
            if value1 == value:
                return True
            else:
                return False
        except:
            print('未找到元素value值')
            return False

    def screenshot(self, file_path):
        """
        截屏
        :param file_path:
        :return:
        """
        self.driver.get_screenshot_as_file(file_path)

    def back(self):
        """
        返回
        :return:
        """
        self.driver.back()

    def refresh(self):
        """
        刷新
        :return:
        """
        self.driver.refresh()

    def select_index(self, locator, index=0):
        """
        下拉框选择---通过 索引 选择值
        :param locator:
        :param index:
        :return:
        """
        select_element = self.find_element(locator)
        select = Select(select_element)
        select.select_by_index(index)

    def select_text(self, locator, text):
        """
        下拉框选择---通过 选项值 选择值
        :param locator:
        :param text:
        :return:
        """
        select_element = self.find_element(locator)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def switch_to_frame(self, locator):
        """
        切换iframe
        :param locator:
        :return:
        """
        element = self.find_element(locator)
        self.driver.switch_to.frame(element)

    def switch_to_parent_frame(self):
        """
        切换回父级iframe
        :return:
        """
        self.driver.switch_to.parent_frame()

    def switch_to_default_content(self):
        """
        切换回主框架
        :return:
        """
        self.driver.switch_to.default_content()

    def switch_to_alert_print(self):
        """
        捕获弹窗元素并打印内容
        :return: 捕获到弹窗返回弹窗元素,反之返回而False
        """
        try:
            alert = self.driver.switch_to.alert
            print(alert.text)
            return alert
        except:
            print('未找到alert元素')
            return False

    def switch_to_alert_accept(self):
        """
        捕获弹窗元素并确认
        :return: 捕获到弹窗返回弹窗元素,反之返回而False
        """
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            return alert
        except:
            print('未找到alert元素')
            return False

    def switch_to_alert_dismiss(self):
        """
        捕获弹窗元素并取消
        :return: 捕获到弹窗返回弹窗元素,反之返回而False
        """
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
            return alert
        except:
            print('未找到alert元素')
            return False

    def switch_to_alert_send_keys(self,text):
        """
        捕获弹窗元素并输入内容
        :return: 捕获到弹窗返回弹窗内容,反之返回而False
        """
        try:
            alert = self.driver.switch_to.alert
            alert.send_keys(text)
            return alert
        except:
            print('未找到alert元素')
            return False
    def close(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()


if __name__ == '__main__':
    import time

    driver = open_browser()
    base = Base(driver)
    url = "http://localhost:8080/ecshop/"
    base.open_url(url)
    zhuce = base.click(('link text', '免费注册'))

    select1 = base.select_index(("tag name", "select"), 1)

    time.sleep(3)

    select2 = base.select_text(("tag name", "select"), "我的座右铭是？")
    # input_loc = ("id", "kw")
    # base.send_keys(input_loc,"自动化测试")
    # time.sleep(2)
    # button_loc = ("id", "su")
    # base.click(button_loc)

    # '''
    # 判断元素文本 value值
    # '''
    # link_loc = ('link text', '新闻')
    # print(base.is_text_in_element(link_loc, '新闻'))
    #
    # # button_loc = ("id", "su")
    # # print(base.is_value_in_element(button_loc,'百度'))
    #
    # button_loc = ("id", "su1")
    # print(base.is_value_in_element(button_loc, '百度一下'))
    #
    # time.sleep(2)
    # base.close()
