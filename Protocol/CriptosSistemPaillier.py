import math
import random

from Crypto.Util import number
import fractions

from CryptoAspects.paillier_aspect import paillier_aspect
from TCR import TCR


class CriptosistPaillier:

    def setup(self, s):

        # criptosistemul Paillier: generam parametrii pentru criptare/decriptare

        p_prim = number.getPrime(20)
        q_prim = number.getPrime(20)
        while not number.isPrime(2 * p_prim + 1):
            p_prim = number.getPrime(20)
        while not number.isPrime(q_prim * 2 + 1):
            q_prim = number.getPrime(20)
        p = 2 * p_prim + 1
        q = 2 * q_prim + 1
        n = p * q
        n_at_s = pow(n, s + 1)
        # m din document
        cmmmc_p_q = p_prim * q_prim

        # calculam g si miu
        este_zstar = False
        este_inversabil = False
        g = n + 1
        u = 0
        while not este_zstar:
            g = random.randint(2, n_at_s - 1)
            if math.gcd(g, n_at_s) == 1:
                este_zstar = True

        while not este_inversabil:

            u = pow(g, cmmmc_p_q, n_at_s)

            u = u - 1
            u = u // n

            if math.gcd(u, n) == 1:
                u = pow(u, -1, n)
                este_inversabil = True

        return [n, p, q, g, u, cmmmc_p_q]

    def gen_random_seed(self, n, s):
        r = 0
        este_zstar = False
        n_at_s = pow(n, s + 1)

        while not este_zstar:
            r = random.randint(2, n_at_s - 1)
            if math.gcd(r, n_at_s) == 1:
                este_zstar = True

        return r

    @paillier_aspect
    def criptarePaillier(self, plaintext, n, g, random_seed, s):

        n_at_s = pow(n, s)
        n_at_s_p1 = pow(n, s + 1)

        return (pow(g, plaintext, n_at_s_p1) * pow(random_seed, n_at_s, n_at_s_p1)) % n_at_s_p1

    @paillier_aspect
    def decriptarePaillier(self, share, criptotext, nr_serv, n, s):

        delta = math.factorial(nr_serv)

        exponent = delta * share * 2
        modulus = pow(n, s + 1)
        c_i = pow(criptotext, exponent, modulus)

        return c_i

    def lamda_calculation(self, nr_serv, indexes, index):
        delta = math.factorial(nr_serv)
        produs = delta
        fraction_result = fractions.Fraction(1, 1)
        fractionss = []
        for i in indexes:
            if i != index:
                fractionss.append(fractions.Fraction(-i, index - i))
        for item in fractionss:
            fraction_result *= item
        return fraction_result * produs

    def c_prim_calculation(self, nr_serv, indexes, cryptotexts, n, s):
        produs = 1
        modulus = pow(n, s + 1)
        for i in indexes:
            lamda_i = self.lamda_calculation(nr_serv, indexes, i)
            lamda_i *= 2
            produs *= pow(cryptotexts[i - 1], int(lamda_i), modulus)
        return produs % modulus

    def exponent_calculation(self, n, c_prim, s):
        i = 0
        for j in range(1, s + 1):
            modul = pow(n, j + 1)
            t_1 = ((c_prim % modul) - 1) // n
            t_2 = i
            for k in range(2, j + 1):
                modul = pow(n, j)
                i -= 1
                t_2 = (t_2 * i) % modul
                t_1 = t_1 - (t_2 * pow(n, k - 1)) * pow(math.factorial(k), -1, modul)
                t_1 %= modul
            i = t_1
        return i

    def gen_coeficienti(self, m, n, s, d, k):
        coeficienti = [d]
        for i in range(0, k - 1):
            coeficienti.append(random.randint(0, (m * (pow(n, s)) - 1)))

        return coeficienti

    def polynomyal_secret_sharing(self, coeficienti, k, n, s, m, x):
        polynom_result = 0
        modulus = m * pow(n, s)
        for i in range(0, k):
            polynom_result += coeficienti[i] * pow(x, i)
            polynom_result %= modulus

        return polynom_result

    def split_shares(self, serv_number, n, d, m, k, s):
        coeficienti = self.gen_coeficienti(m, n, s, d, k)
        shares = []
        for i in range(1, serv_number + 1):
            shares.append(self.polynomyal_secret_sharing(coeficienti, k, n, s, m, i))

        return shares

    def split_verif_values(self, u, nr_serv, shares, n, s):

        verif_values = []
        fact = math.factorial(nr_serv)

        for i in range(0, nr_serv):
            verif_values.append(pow(u, fact * shares[i], pow(n, s + 1)))

        return verif_values

    def decryption_sharing(self, ciphertext, n, s, shares, delta_patrat, nr_serv):
        c_1 = self.decriptarePaillier(shares[0], ciphertext, nr_serv, n, s)
        c_2 = self.decriptarePaillier(shares[1], ciphertext, nr_serv, n, s)
        c_3 = self.decriptarePaillier(shares[2], ciphertext, nr_serv, n, s)
        c_4 = self.decriptarePaillier(shares[3], ciphertext, nr_serv, n, s)
        c_prim = self.c_prim_calculation(nr_serv, [1, 2, 3, 4], [c_1, c_2, c_3, c_4], n, s)
        exponent = self.exponent_calculation(n, c_prim, s)
        return (exponent * pow(4 * delta_patrat, -1, pow(n, s))) % pow(n, s)


# obiect = CriptosistPaillier()
# tcr = TCR()
# parametrii = obiect.setup(1)
# n = parametrii[0]
# m = parametrii[5]
# u = parametrii[4]
# g = n + 1
# s = 1
# exp = [0, 1]
# m_list = [m, pow(n, s)]
# d = tcr.chinese_remainder(m_list, exp)
# k = 3
# shares = obiect.split_shares(4, n, d, m, k, s)
# random_seed = obiect.gen_random_seed(n, s)
# delta_patrat = pow(math.factorial(4), 2)
# ciphertext = obiect.criptarePaillier(10, n, g, random_seed, s)
# print(obiect.decryption_sharing(ciphertext, n, s, shares, delta_patrat, 4))
"""
for share in shares:
    print("Share: " + str(share))
M = 124121
cryptotext = obiect.criptarePaillier(M, n, g, obiect.gen_random_seed(n,s), s)
c_1 = obiect.decriptarePaillier(shares[0], cryptotext, 3, n, s)
c_2 = obiect.decriptarePaillier(shares[1], cryptotext, 3,  n, s)
c_3 = obiect.decriptarePaillier(shares[2], cryptotext, 3,  n, s)
c_4 = obiect.decriptarePaillier(shares[3], cryptotext, 3,  n, s)
delta_patrat = pow(math.factorial(3), 2)
print("Criptotext: " + str(cryptotext))

c_prim = obiect.c_prim_calculation(3, [1, 2, 3], [c_1, c_2, c_3], n, s)

print("C_prim: " + str(c_prim))
print("Verificare: " + str(pow(cryptotext, 4 * delta_patrat * d, pow(n, s + 1))))
print("Verificare 2: " + str(pow(n + 1, 4 * delta_patrat * M, pow(n, s + 1))))
exponent = obiect.exponent_calculation(n, c_prim, s)

print((exponent * pow(4 * delta_patrat, -1, pow(n, s))) % pow(n, s))
"""
