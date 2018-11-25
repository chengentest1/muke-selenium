import os
import HTMLTestRunner
import ddt
import time
from selenium import webdriver
import unittest

from business.register_business import RegisterBusiness
from util.excel_util import ExcelUtil

ex=ExcelUtil()
data=ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login=RegisterBusiness(self.driver)
    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.path.dirname(os.getcwd())+'/report/'+case_name+'.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
        '''
    @ddt.data(
        ['12','yewr3','123456','code','user_email_error','请输入有效的电子邮件地址'],
        ['@qq.com', 'yewr3', '123456', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
        ['12yu@qq.com', 'yewr3', '123456', 'code', 'user_email_error', '请输入有效的电子邮件地址']
    )
    @ddt.unpack
        '''
    @ddt.data(*data)
    def test_login_email_error(self,data):
        email, username, password, code, assertCode, assertText=data
        email_error=self.login.register_function(email,username,password,code,assertCode,assertText)
        self.assertFalse(email_error,'此条case执行失败')

if __name__ == '__main__':
    file_path=os.path.join(os.path.dirname(os.getcwd())+"/report/"+"first_case1.html")
    f=open(file_path,'wb')
    suite=unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='this is first report1',description='这是第一个报告1')
    runner.run(suite)