import math
from Protocol import StatisticalFunctions
from Protocol.StatisticalFunctions import StatisticalFunctions
from Protocol.TCR import TCR
from Protocol.CriptosSistemPaillier import CriptosistPaillier


def generate_setup():
    obiect = CriptosistPaillier()
    tcr = TCR()
    parametrii = obiect.setup(1)
    n = parametrii[0]
    m = parametrii[5]
    u = parametrii[4]
    g = n + 1
    s = 1
    exp = [0, 1]
    m_list = [m, pow(n, s)]
    d = tcr.chinese_remainder(m_list, exp)
    nr_serv = 4
    k = 3
    shares = obiect.split_shares(nr_serv, n, d, m, k, s)
    random_seed = obiect.gen_random_seed(n, s)
    delta_patrat = pow(math.factorial(4), 2)
    return n, g, random_seed, s, shares, obiect, delta_patrat


# values = [1, 2, 3, 4]
# statistic = StatisticalFunctions(values, n, g, random_seed, s, shares, obiect, delta_patrat)
# a = 30
# b = 30
# a_encrypted = obiect.criptarePaillier(a, n, g, random_seed, s)
# b_encrypted = obiect.criptarePaillier(b, n, g, random_seed, s)
# a_multyply_b_encrypted = obiect.criptarePaillier(a * b, n, g, random_seed, s)
# print(a_multyply_b_encrypted)
# print(obiect.decryption_sharing(a_multyply_b_encrypted, n, s, shares, delta_patrat, nr_serv))
# print(test_main.calculate_a_multiply_b(a_encrypted, b_encrypted, n, g, random_seed, s, shares, obiect, delta_patrat,
#                                        nr_serv, k))