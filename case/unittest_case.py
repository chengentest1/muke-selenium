import unittest
class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('这个是所有case的前置条件')
    @classmethod
    def tearDownClass(cls):
        print('这个是所有case的后置条件')
    def setUp(self):
        print('这个是case的前置条件')
    def tearDown(self):
        print('这个是case的后置条件')
    @unittest.skip('跳过')
    def testfirst01(self):
        print('这个第一个case')
    def testfirst02(self):
        print('这个第二个case')
    def testfirst03(self):
        print('这个第三个case')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst01'))
    suite.addTest(FirstCase01('testfirst03'))
    suite.addTest(FirstCase01('testfirst02'))
    unittest.TextTestRunner().run(suite)