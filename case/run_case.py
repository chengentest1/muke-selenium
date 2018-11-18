import unittest
import os
# f=os.getcwd()
# print(os.getcwd())
# print(os.path.join(f,'case'))
class RunCase(unittest.TestCase):
    def test_case01(self):
        # case_path=os.path.join(os.getcwd(),'case')
        case_path=os.getcwd()
        suite=unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()