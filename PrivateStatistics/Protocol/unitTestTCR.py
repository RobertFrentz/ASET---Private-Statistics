import unittest
from TCR import TCR
class UnitTestTCR(unittest.TestCase):

    tcr_obj = TCR()

    def test_inv_multiplicative(self):

        self.assertTrue(self.tcr_obj.mul_inv(5,11) * 5 % 11  == 1)

    def test_chinese_remainder(self):

        x_list = [3,5,7]
        modulo_list = [11,13,17]

        result = self.tcr_obj.chinese_remainder(modulo_list,x_list)

        self.assertTrue(result % 11 == 3)
        self.assertTrue(result % 13 == 5)
        self.assertTrue(result % 17 == 7)



if __name__ == '__main__':
    unittest.main()






