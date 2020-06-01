import pandas


class HandleExcel:

    def __init__(self,file_path, filename = 0):
        """
        converters={"列名":数据类型}可以指定读出的数据格式类型
        :param file_path:excel文件的路径
        :param filename:可传索引,也可传表名
        """
        self._sheet = pandas.read_excel(file_path,filename)

    def get_data_for_dict(self):
        """
        用pandas对excel里的数据进行获取
        :return: 返回值格式为列表里包含字典[{},{},{}.....]
        """
        try:
            _data = []
            for i in self._sheet.index.values:
                # 用表格里每行遍历出来的值用字典的方式保存在row_data中
                _row_data = self._sheet.loc[i].to_dict()
                _data.append(_row_data)
            return _data

        except FileNotFoundError:
            print('读取数据的文件不存在,请检查文件路径！')
            return False

        except Exception as e:
            print(f'读取数据失败 -> 错误原因 : {e}')
            return False

    def write_reg_excel(self, list_data: dict, to_path):
        """

        :param list_data: 传入字典格式的数据
        :param to_path: 要写入的表格路径
        :return:
        """
        try:
            _username = []
            _email = []
            _password = []
            _mobile = []
            _answer = []

            for i in self._sheet.index.values:
                # 根据i值循环读取表格数据
                row_data = self._sheet.loc[i].to_dict()

                # 把老表格读取出来的值循环添加到对应的列表里
                _username.append(row_data['username'])
                _password.append(row_data['password'])
                _email.append(row_data['email'])
                _mobile.append(row_data['mobile'])
                _answer.append(row_data['answer'])

            # 在对应列表里的最前添加数据,使其写入的时候永远在第一行
            # 测试数据
            _username.insert(0, list_data['username'])
            _password.insert(0, list_data['password'])
            _email.insert(0, list_data['email'])
            _mobile.insert(0, list_data['mobile'])
            _answer.insert(0, list_data['answer'])

            # 建立ExcelWriter实例化对象,传入需要写入的excel表的路径
            writer = pandas.ExcelWriter(to_path)

            # 将数据用pandas里的DataFrame的方法处理并且用变量df1保存
            df1 = pandas.DataFrame({
                'username': _username,
                'password': _password,
                'email': _email,
                'mobile': _mobile,
                'answer': _answer})

            # 将数据写入excel表格
            # na_rep参数是当为写入某列数据时用None代替 index参数是为是否显示pandas自带索引
            df1.to_excel(writer, index=False)

            # 保存表格
            writer.save()

        except Exception as e:
            print(f'写入数据失败 -> 错误原因 : {e}')