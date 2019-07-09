import unittest
def div(a,b):
    return a/b

class Myfirstunittest(unittest.TestCase):
    def setUp(self):
        print('star')

    def tearDown(self):
        print('end')

    def test_testcase(self):
        self.assertEquals(div(1,1),1/1)

    def test_testcase2(self):
        self.assertEquals(div(3,4),3/4)

    def test_testcase3(self):
        print('3/0')
        self.assertRaises(ZeroDivisionError,div,3,0) #执行代码运行到div这个方法时，如果a参数是3，b参数是0时，就是抛出异常
        # self.assertRaises("", div, 3, 0)  # 执行代码运行到div这个方法时，如果a参数是3，b参数是0时，就是抛出异常

if __name__ == '__main__':
    unittest.main()