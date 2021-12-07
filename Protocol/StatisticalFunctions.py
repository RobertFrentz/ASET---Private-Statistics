import math

import test_main
from CriptosSistemPaillier import CriptosistPaillier


class StatisticalFunctions:
    paillier_encrypt = CriptosistPaillier()

    def __init__(self, values_list, n, g, random_seed, s, shares, obiect, delta_patrat):
        self.values_encrypted = []
        self.values_list = values_list
        self.n = n
        self.g = g
        self.random_seed = random_seed
        self.s = s
        self.shares = shares
        self.obiect = obiect
        self.delta_patrat = delta_patrat
        self.nr_serv=4
        self.k=3

    def encrypt_values(self):
        for value in self.values_list:
            encrypt = self.paillier_encrypt.criptarePaillier(value, self.n, self.g, self.random_seed, self.s)
            self.values_encrypted.append(encrypt)
        return self.values_encrypted

    def mean(self):
        # summ=sum(self.values_list)
        product = math.prod(self.values_encrypted) % pow(self.n,self.s+1)
        number_of_elements = len(self.values_list)
        return test_main.calculate_function(product, number_of_elements, self.n, self.g, self.random_seed, self.s, self.shares, self.obiect, self.delta_patrat,self.nr_serv,self.k)

    def variance(self):

        pass