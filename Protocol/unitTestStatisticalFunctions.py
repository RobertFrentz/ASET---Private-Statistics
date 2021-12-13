import math
import unittest
from StatisticalFunctions import StatisticalFunctions
from CriptosSistemPaillier import CriptosistPaillier
from TCR import TCR


class UnitTestStatisticalFunctions(unittest.TestCase):

    obiect = CriptosistPaillier()
    s = 1
    param_list = obiect.setup(s)
    n = param_list[0]
    p = param_list[1]
    q = param_list[2]
    g = param_list[3]
    u = param_list[4]
    m = param_list[5]
    exp = [0, 1]
    m_list = [m, pow(n, s)]
    tcr = TCR()
    d = tcr.chinese_remainder(m_list, exp)
    k = 3
    shares = obiect.split_shares(4, n, d, m, k, s)
    random_seed = obiect.gen_random_seed(n, s)
    delta_patrat = pow(math.factorial(4), 2)
    lista = [1, 2, 3, 4]
    statisticalFunc_obj = StatisticalFunctions(lista, n, g, random_seed, s, shares,
                                                    obiect, delta_patrat)

    def test_mean(self):

       self.assertTrue(2.5 == round(self.statisticalFunc_obj.mean(),2))

    def test_variance(self):

        self.assertTrue( 1.67 == round(self.statisticalFunc_obj.variance(),2))

    def test_standard_deviation(self):

        self.assertTrue( 1.29 == round(self.statisticalFunc_obj.standard_deviation(),2))

    def test_standard_error(self):

         self.assertTrue(0.65 == round(self.statisticalFunc_obj.standard_error(),2))



if __name__ == '__main__':
    unittest.main()