
import math

import test_main
from StatisticalFunctions import StatisticalFunctions
from TCR import TCR
from CriptosSistemPaillier import CriptosistPaillier

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
shares = obiect.split_shares(4, n, d, m, 3, s)
random_seed = obiect.gen_random_seed(n, s)
delta_patrat = pow(math.factorial(4), 2)

statistic = StatisticalFunctions([1, 2, 3, 4, 5], n, g, random_seed, s)
encrypted_values = statistic.encrypt_values()
print(statistic.mean())
print(test_main.calculate_function(15,5))
