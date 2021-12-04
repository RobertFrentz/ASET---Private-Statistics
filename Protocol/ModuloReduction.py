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
        self.encrypted_r = self.paillier_encrypt.criptarePaillier(r, n, g, random_seed, s)

    def generate_l_s(self):
        while True:
            self.l_s = 10
            # self.l_x = int.bit_length(self.x)
            # if self.a * self.nr_serv * pow(2, self.l_x + self.l_s) < pow(self.n, self.s):
            #     # print("ceva")
            #     # print(self.a*self.nr_serv*pow(2,l_x+self.l_s))
            #     # print(pow(self.n,self.s))
            #     # print(l_x)
            #     # print(self.l_s)
            return self.l_s


    def generate_s_i(self, l_s, l_x):
        length = l_s + l_x
        s = ""
        for i in range(0, length):
            s += str(random.randint(0, 1))
        return self.paillier_encrypt.criptarePaillier(int(s, 2), self.n, self.g, self.random_seed, self.s)

    def compute_x_at_step_2(self, S_i):

        produs = 1
        modulus = pow(self.n, self.s+1)

        for i in range(0, len(S_i)):
            produs *= S_i[i] % modulus

        produs = pow(produs, self.a, modulus)

        return self.x * pow(self.encrypted_r, -1, modulus) * produs % modulus

    def compute_mod_x_A(self, c_encrypted, x_second_encrypted):

        return x_second_encrypted * self.encrypted_r * pow(c_encrypted, -self.a, pow(self.n, self.s + 1)) % pow(self.n,
                                                                                                                self.s + 1)
