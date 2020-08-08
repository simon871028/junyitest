import unittest
from Q1 import reverseString

class TestQ1(unittest.TestCase):
    #測試單字
    def testVocab(self):
        data = "Python"
        result = reverseString(data)
        self.assertEqual(result,"nohtyP")
    #測試句子
    def testStr(self):
        data = ["I am from Taiwan"," I am  from    Taiwan","hello world"]
        ans =  ["I ma morf nawiaT"," I ma  morf    nawiaT","olleh dlrow"]
        for i in range(0,2):
            result = reverseString(data[i])
            self.assertEqual(result,ans[i])
    # test numbers
    def testNum(self): 
        data = "12345678889"
        result = reverseString(data)
        self.assertEqual(result,"98887654321")

if __name__ == '__main__':
    unittest.main()