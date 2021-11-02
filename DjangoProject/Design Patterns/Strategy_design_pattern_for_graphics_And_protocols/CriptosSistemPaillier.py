import math
import random
from Cryptodome.Util import number


class CriptosistPaillier:


    def setup(self):

        # criptosistemul Paillier: generam parametrii pentru criptare/decriptare

        p = number.getPrime(800)
        q = number.getPrime(800)
        n = p * q
        n_patrat = n * n
        cmmmc_p_q = math.lcm(p - 1, q - 1)

        #calculam g si miu
        este_zstar = False
        este_inversabil = False
        g = 0
        u = 0
        while este_zstar == False:
            g = random.randint(2, n_patrat - 1)
            if (math.gcd(g, n_patrat) == 1):
                este_zstar = True

        while este_inversabil == False:

            u = pow(g, cmmmc_p_q, n_patrat)

            u = u - 1
            u = u // n

            if (math.gcd(u, n) == 1):
                u = pow(u, -1, n)
                este_inversabil = True

        return [n, p, q, g, u, cmmmc_p_q]

    def criptarePaillier(self, plaintext, n, g, random_seed):
        return pow(g, plaintext, n * n) * pow(random_seed, n, n * n) % (n * n)

    def decriptarePaillier(self, ciphertext, cmmmc, n, u):
        return ((((pow(ciphertext, cmmmc, n * n)) - 1) // n) * u) % n

    def generareSirDeBiti(self,lungime):

        sir = ""

        for i in range(0, lungime):
            sir += str(random.randint(0, 1))

        return sir