import unittest
class FirstCase02(unittest.TestCase):
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
    def testfirst001(self):
        print('这个第0一个case')
    def testfirst002(self):
        print('这个第0二个case')
    def testfirst003(self):
        print('这个第0三个case')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('testfirst001'))
    suite.addTest(FirstCase02('testfirst003'))
    suite.addTest(FirstCase02('testfirst002'))
    unittest.TextTestRunner().run(suite)