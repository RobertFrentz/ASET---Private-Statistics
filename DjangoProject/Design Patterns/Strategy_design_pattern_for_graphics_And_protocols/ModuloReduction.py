import random

from CriptosSistemPaillier import CriptosistPaillier


class ModuloReduction:
    paillier_encrypt = CriptosistPaillier()

    def __init__(self, n, g, random_seed, s, nr_serv, k, r, x, a):
        self.n = n
        self.g = g
        self.random_seed = random_seed
        self.s = s
        self.nr_serv = nr_serv
        self.k = k
        self.r = r
        self.x = x
        self.a = a

    def generate_l_s(self):
        while True:
            self.l_s = random.randint(1, 20)
            self.l_x = int.bit_length(self.x)
            if self.a * self.nr_serv * pow(2, self.l_x + self.l_s) < pow(self.n, self.s):
                # print("ceva")
                # print(self.a*self.nr_serv*pow(2,l_x+self.l_s))
                # print(pow(self.n,self.s))
                # print(l_x)
                # print(self.l_s)
                return self.l_s

    def generate_s_i(self,l_s, l_x):
        length = l_s + l_x
        s = ""
        for i in range(0, length):
            s += str(random.randint(0, 1))
        return int(s, 2)
