import math
import unittest
from primePy import primes
from TCR import TCR

from CriptosSistemPaillier import CriptosistPaillier as CP
class UnitTestPaillier(unittest.TestCase):

    obj = CP()
    s = 1
    param_list = obj.setup(s)

    n = param_list[0]
    p = param_list[1]
    q = param_list[2]
    g = param_list[3]
    u = param_list[4]
    m = param_list[5]

    def test_setup(self):

        ##tc1
        self.assertTrue(self.n == self.p * self.q)

        ##tc2

        self.assertTrue(primes.check(self.p) == True and primes.check(self.q) == True )

        ##tc3

        self.assertTrue(self.g == self.n + 1 )


    def test_encryption_decryption_process(self):
        exp = [0, 1]
        m_list = [self.m, pow(self.n, self.s)]
        tcr = TCR()
        d = tcr.chinese_remainder(m_list, exp)
        self.k = 3
        shares = self.obj.split_shares(4, self.n, d, self.m, self.k, self.s)
        random_seed = self.obj.gen_random_seed(self.n, self.s)
        delta_patrat = pow(math.factorial(4), 2)
        ciphertext = self.obj.criptarePaillier(10, self.n, self.g, random_seed, self.s)

        for share in shares:
            print("Share: " + str(share))
        M = 124121
        cryptotext = self.obj.criptarePaillier(M, self.n, self.g, self.obj.gen_random_seed(self.n,self.s), self.s)
        c_1 = self.obj.decriptarePaillier(shares[0], cryptotext, 3, self.n, self.s)
        c_2 = self.obj.decriptarePaillier(shares[1], cryptotext, 3,  self.n, self.s)
        c_3 = self.obj.decriptarePaillier(shares[2], cryptotext, 3,  self.n, self.s)
        c_4 = self.obj.decriptarePaillier(shares[3], cryptotext, 3,  self.n, self.s)
        delta_patrat = pow(math.factorial(3), 2)

        c_prim = self.obj.c_prim_calculation(3, [1, 2, 3], [c_1, c_2, c_3], self.n, self.s)

        self.assertTrue(c_prim == pow(cryptotext, 4 * delta_patrat * d, pow(self.n, self.s + 1)))



        exponent = self.obj.exponent_calculation(self.n, c_prim, self.s)

        self.assertTrue ((exponent * pow(4 * delta_patrat, -1, pow(self.n, self.s))) % pow(self.n, self.s) == M)





if __name__ == '__main__':
    unittest.main()