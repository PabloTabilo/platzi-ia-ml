import unittest

def suma(num1, num2):
    return num1+num2

class BlackBox(unittest.TestCase):
    def test_sum(self):
        num1, num2 = 10, 5
        res = suma(num1, num2)
        self.assertEqual(res, 15)

    def test_sum_neg(self):
        num1, num2 = -10, -7
        res=suma(num1, num2)
        self.assertEqual(res, -17)

if __name__=="__main__":
    unittest.main()