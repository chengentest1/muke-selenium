from business.register_business import RegisterBusiness
import HTMLTestRunner
from selenium import webdriver
import unittest,os,time
class FirstCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login=RegisterBusiness(self.driver)
    def tearDown(self):
        time.sleep(3)
        self.driver.close()
    def test_login_email_error(self):
        email_error=self.login.login_email_error('34', 'user111','111111','test1')
        self.assertFalse(email_error,'此条case执行失败')
        # if email_error==True:
        #     print('注册成功了，此条case执行失败')
    @unittest.skip('跳过')
    def test_login_username_error(self):
        username_error = self.login.login_name_error('111@qq.com','ss','111111','test2')
        if username_error ==True:

            print('此条case执行失败')

    @unittest.skip('跳过')
    def test_login_code_error(self):
        password_error = self.login.login_code_error('34@qq.com', 'user111','111111','test1')
        if password_error == True:
            print('此条case执行失败')

    @unittest.skip('跳过')
    def test_login_success(self):
        succes =self.login.user_base('34@qq.com', 'user111','111111','test1')
        if self.login.register_succes()==True:
            print('注册成功')



if __name__ == '__main__':
    # path=os.path.join(os.path.dirname(os.getcwd())+'/report/'+'first_case.html')
    # f=open(path,'wb')
    # suite=unittest.TestSuite()
    # suite.addTest(FirstCase('test_login_email_error'))
    # runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='this is first report',description='这是第一个报告')
    # runner.run(suite)
    # unittest.TextTestRunner().run(suite)
    unittest.main()


