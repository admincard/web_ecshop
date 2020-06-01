'''

使用HTMLTestRunnerPlugins类生成测试报告

author:llj
'''
import unittest
import HTMLTestRunnerPlugins
import time

# 1 获取测试用例文件夹路径
case_dir = './scripts'
# 2 获取需要执行测试用例文件.py
test_dir = 'test_*.py'
# 3 建立测试报告存放路径
report_dir = './report'
# 4 将需要执行的测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(case_dir,test_dir)
# 5 使用HTMLTestRunnerPlugins 执行测试用例并生成测试报告
# 测试报告以获取的当前时间命名
now = time.strftime('%Y_%m_%d %H_%M')
#打开文件写入内容
with open(report_dir+'\\'+now+'report.html','wb') as file:
    #执行测试获取报告
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(
        stream=file, verbosity=2, title='自动化测试报告', description='报告详细描述', retry=0
    )
    # verbosity: 结果描述的详细程度 0, 1, 2 三个值
    runner.run(discover)