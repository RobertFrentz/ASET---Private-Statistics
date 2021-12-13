import random
from functools import reduce


class TCR:


    def chinese_remainder(self, m, a):
        sum = 0
        prod = reduce(lambda acc, b: acc * b, m)
        for n_i, a_i in zip(m, a):
            p = prod // n_i
            sum += a_i * self.mul_inv(p, n_i) * p
        return sum % prod

    def mul_inv(self, a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1