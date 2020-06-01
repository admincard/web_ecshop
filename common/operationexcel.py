'''
1.读取excel表格
2.读取出来的数据格式[{},{}]
3.处理单元格中的数据格式
    在excel中各种数据类型都有对应编号 ctype
    ctype      数据类型
    2           int
    3           date
    4           Boolean
'''
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime
from xlutils.copy import copy


class OperationExcel:
    def __init__(self,filename,index=0):
        '''
        打开表格并按照索引获取sheet.索引由0开始
        :param filename:  table 路径
        :param index: sheet的索引值
        '''
        # 打开excel文件
        self.filename = filename
        self.table = xlrd.open_workbook(filename=filename)
        # 通过索引读取具体表格
        self.sheet = self.table.sheet_by_index(index)

    def read_excel_date(self):
        '''
        读取表格中的数据,并对特殊数据进行处理
        通过按照读取单元格的数据,对单元格的数据进行数据类型转换
        :return:
        '''
        rows = self.sheet.nrows #获取总行数
        locs = self.sheet.ncols #获取总列数
        # 遍历行和列得到单元格的数据(先遍历行,再遍历列)
        all_data = []
        for row in range(1,rows):   #首行为标题栏
            cell_data= [] # 转换后的单元格数据
            for col in range(locs):
                cell = self.sheet.cell_value(row,col) #获取单元格数据
                ctype= self.sheet.cell(row,col).ctype #获取单元格数据类型
                #单元格数据类型为:int
                if ctype==2 and cell %1 ==0:
                    cell = int(cell)
                #单元格数据类型为 日期
                elif ctype==3:
                    date = datetime(*xldate_as_tuple(cell,0))
                    '''
                    xldate_as_tuple(xldate, datemode)
                    将Excel数字（假定代表日期、日期时间或时间）转换为适用于向datetime或mx.datetime构造函数提供数据的元组。
                    datemode: 0: 1900-based, 1: 1904-based.
                    '''
                    cell =date.strftime('"%Y_%m_%d %H:%M:%S"')
                #单元格数据类型为bool 值
                elif ctype==4:
                    cell = True if cell==1 else False   #三目运算符
                cell_data.append(cell)
            all_data.append(cell_data)
        return all_data

    def get_data_for_dict(self):
        """
        将表格中的数据按照[{},{}]格式输出
        :return:
        """
        key = self.sheet.row_values(0)  #第一行作为键
        values= self.read_excel_date()   #其余行作为值
        data_list = []
        for value in values:
            #zip函数组合 keys,value
            tmp = zip(key,value)
            #将组合后的数据转化为字典加入列表
            data_list.append(dict(tmp))
        return data_list

    def wirte_excel(self, new_data: list):
        """
        1.复制老表格的数据
        2.重新打开复制的表格,写入数据
        :return:
        """
        # 1.复制老表格文件
        new_table = copy(self.table)
        # 2.打开新表格
        new_sheet = new_table.get_sheet(0)
        # 3.插入新数据--插入一行数据
        insert_row_no = 1  # 将数据从第2行插入
        # 获取插入数据的个数
        num = len(new_data)
        for i in range(num):
            new_sheet.write(insert_row_no,i,new_data[i]) # 将新数据写入表格中
        # 4.复写老数据
        # 获取老数据的行数
        rows = self.sheet.nrows
        # 获取老数据的列数
        cols = self.sheet.ncols
        for row in range(1,rows):
            for col in range(cols):
                new_sheet.write(row+1,col,self.sheet.cell_value(row,col))
        # 5.保存
        new_table.save(self.filename)

    def get_col_data(self,col_name):
        """
        根据列名获取列数据
        :param col_name: 获取的列名
        :return:
        """
        cols = self.sheet.ncols  #获取所有的列数
        for i in range(cols):  #遍历出列号
            title = self.sheet.cell_value(0, i)  #获取首行 表头每个单元格 文本信息
            if title==col_name:   # 第一行 第i+1列 单元格值与 列表名相同
                #获取--目标列数据
                col_values = self.sheet.col_values(i,1)
                return col_values

if __name__ == '__main__':
   data = OperationExcel('../../textdata.xlsx')
   print(data.read_excel_date())
   print(data.get_data_for_dict())
