from Q2 import totalNumberLeft
import unittest
import random
class TestQ2(unittest.TestCase):
    # 3倍數、5倍數、15倍數、不相干
    def test(self):
        data = [9,20,30,31]
        ans = [5,12,18,19]
        for i in range(0,4):
            result =totalNumberLeft(data[i]) 
            self.assertEqual(result, ans[i])
    #測資輸入1-10000，用不同的算法（扣掉3、5的倍數數目，加回2次交集：15的倍數數目）驗算一次。
    def testAutoCal(self): 
        for data in range(1,10000): 
            result = totalNumberLeft(data)
            result2 = data - int(data/3)- int(data/5)+ 2*int(data/15)
            self.assertEqual(result,result2)
    #輸入若為浮點數則return False
    def testFloat(self):
        data = 5.5
        result = totalNumberLeft(data)
        self.assertFalse(result)
    #若輸入為負數則return False
    def testNegative(self):
        data = -20
        result = totalNumberLeft(data)
        self.assertFalse(result)
        
if __name__ == '__main__':
    unittest.main()