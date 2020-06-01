"""
构造测试数据
    注册数据
"""
import random
from ECShop.common.operationexcel import OperationExcel


class Constructdata(object):
    def __init__(self):
        self.oper_excel = OperationExcel(r"E:\个人练习\12_自动化项目_llj\ECShop\data\registerdata.xls",0)

    @staticmethod
    def random_username():
        """随机生成用户名"""
        frist_name = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王", "Tom", "Jerry", "Kitty", "冯", "陈", "楚", "卫"]
        last_name = ["芷荷", "怀瑶", "慕易", "若芹", "紫安", "曼冬", "寻巧", "寄波", "尔槐",
                     "以旋", "初夏", "依丝", "怜南", "傲菡", "谷蕊", "笑槐", "飞兰", "笑卉",
                     "迎荷", "元冬", "痴安", "妙绿", "觅雪", "寒安", "沛凝", "白容", "乐蓉",
                     "映安", "依云", "映冬", "凡雁", "梦秋", "梦凡", "秋巧", "若云", "元容",
                     "怀蕾", "灵寒", "天薇", "翠安", "乐琴", "宛南", "怀蕊", "白风", "访波",
                     "亦凝", "易绿", "夜南", "曼凡", "亦巧", "青易。冰真", "白萱", "友安",
                     "海之", "小蕊", "又琴", "天风", "若松", "盼菡", "秋荷", "香彤", "语梦",
                     "惜蕊", "迎彤", "沛白", "雁山", "易蓉", "雪晴", "诗珊", "春冬", "又绿",
                     "冰绿", "半梅", "笑容", "沛凝", "映秋", "盼烟", "晓凡", "涵雁", "问凝",
                     "冬萱", "晓山", "雁蓉", "梦蕊", "山菡", "南莲", "飞双", "凝丝", "思萱",
                     "怀梦", "雨梅", "冷霜", "向松", "迎丝", "迎梅", "雅彤", "香薇", "以山",
                     "碧萱", "寒云", "向南", "书雁", "怀薇", "思菱", "忆文", "翠巧", "怀山",
                     "若山", "向秋", "凡白", "绮烟", "从蕾", "天曼", "又亦", "从安", "绮彤",
                     "之玉", "凡梅", "依琴", "沛槐", "又槐", "元绿", "安珊", "夏之", "易槐",
                     "宛亦", "白翠", "丹云", "问寒", "易文", "傲易", "青旋", "思真", "雨珍",
                     "幻丝", "代梅", "盼曼", "妙之", "半双", "若翠", "初兰", "惜萍", "初之",
                     "宛丝", "寄南", "小萍", "静珊", "千风", "天蓉", "雅青", "寄文", "涵菱",
                     "香波", "青亦", "元菱", "翠彤", "春海", "惜珊", "向薇", "冬灵", "惜芹",
                     "凌青", "谷芹", "雁桃", "映雁", "书兰", "盼香", "向山", "寄风", "访烟",
                     "绮晴", "映之", "醉波", "幻莲", "谷冬", "傲柔", "寄容", "以珊", "紫雪",
                     "芷容", "书琴", "寻桃", "涵阳", "怀寒", "易云", "代秋", "惜梦", "尔烟",
                     "谷槐", "怀莲", "夜山", "芷卉", "向彤", "新巧", "语海", "灵珊", "凝丹",
                     "小蕾", "迎夏"]
        return random.choice(frist_name)+"".join(random.choice(last_name))

    @staticmethod
    def random_email():
        """随机生成邮箱"""
        email_type = ["@qq.com","@163.com","@126.com","@189.com"]
        number = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # 邮箱长度4--10位
        lang = random.randint(4,10)
        return "".join(random.choice(number) for i in range(lang))+random.choice(email_type)

    @staticmethod
    def random_password():
        """随机生成密码"""
        number = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # 密码长度6--18位
        long = random.randint(6,18)
        return "".join(random.choice(number) for i in range(long))

    @staticmethod
    def random_mobile():
        """随机生成手机号"""
        phone_head = ["133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","180","186","187","188"]
        number = "0123456789"
        return random.choice(phone_head)+"".join(random.choice(number) for i in range(8))

    @staticmethod
    def random_answer():
        """随机问题答案"""
        answer_list = ["为人性僻耽佳句,语不惊人死不休.",
                       "白发三千丈,缘愁似个长.",
                       "座客三千人，于今知有谁.",
                       "出师未捷身先死，长使英雄泪满襟。",
                       "兰陵美酒郁金香，玉碗盛来琥珀光。",
                       "庄生晓梦迷蝴蝶，望帝春心托杜鹃。",
                       "靡不有初，鲜克有终。",
                       "一唱雄鸡天下白，万方乐奏有于阗",
                       "高山仰止，景行行止",
                       "一日不见，如三月兮",
                       "有匪君子，如切如磋，如琢如磨"
                       ]
        return random.choice(answer_list)

    @staticmethod
    def random_choice():
        """随机选择下拉框选项"""
        choice_list = ["请选择商品类型",
                       "书",
                       "音乐",
                       "电影",
                       "手机",
                       "笔记本电脑",
                       "数码相机",
                       "数码摄像机",
                       "化妆品",
                       "精品手机"
                       ]
        return random.choice(choice_list)



    def get_all_register_data(self):
        """获取全部注册数据"""
        data = {}
        data["username"] = Constructdata.random_username()
        data["email"] = Constructdata.random_email()
        data["password"] = Constructdata.random_password()
        data["mobile"] = Constructdata.random_mobile()
        data["answer"] = Constructdata.random_answer()
        new_data = {}
        for i in range(len(data)):
            new_data[list(data.keys())[i]] = self.is_exist(list(data.keys())[i], data[list(data.keys())[i]])
        return new_data

    def get_require_options_register_data(self):
        """获取必填项注册数据"""
        data = {}
        data["username"] = Constructdata.random_username()
        data["email"] = Constructdata.random_email()
        data["password"] = Constructdata.random_password()
        data["mobile"] = Constructdata.random_mobile()
        data["answer"] = ""
        new_data = {}
        for i in range(len(data)):
            new_data[list(data.keys())[i]] = self.is_exist(list(data.keys())[i], data[list(data.keys())[i]])
        return new_data

    @staticmethod
    def get_dict_value_to_list(data: dict):
        """
        将字典的值转化成列表
        :param data:
        :return:
        """
        values = []
        for key in data.keys():
            values.append(data[key])
        return values

    def run_main(self, inputname):
        if inputname == "username":
            retry_data = Constructdata.random_username()
        elif inputname == "email":
            retry_data = Constructdata.random_email()
        elif inputname == "mobile":
            retry_data = Constructdata.random_mobile()
        else:
            print("输入的类型不正确")
            retry_data = None
        return retry_data

    def is_exist(self, col_name, col_data):
        """判断新生成的数据是否存在于列表中"""
        col_name_data = self.oper_excel.get_col_data(col_name)
        if col_name in ["username", "email", "mobile"] and col_data in col_name_data:
            new_col_data = self.run_main(col_name)
        else:
            new_col_data = col_data

        return new_col_data



if __name__ == '__main__':
    # text = Constructdata.random_username()
    # text = Constructdata.random_email()
    # text = Constructdata.random_password()
    # text = Constructdata.random_mobile()
    text = Constructdata().is_exist('username',"诸葛亮_9")
    # text = Constructdata.random_answer()
    print(text)
