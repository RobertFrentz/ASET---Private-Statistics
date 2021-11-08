import math
import random
from Crypto.Util import number
from sympy.ntheory import discrete_log


class CriptosistPaillier:

    def setup(self):

        # criptosistemul Paillier: generam parametrii pentru criptare/decriptare

        p = number.getPrime(50)
        q = number.getPrime(50)
        n = p * q
        n_patrat = n * n
        # m din document
        cmmmc_p_q = math.lcm(p - 1, q - 1)

        # calculam g si miu
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

    def gen_random_seed(self, n, s):
        r = 0
        este_zstar = False
        n_at_s = pow(n, s + 1)

        while este_zstar == False:
            r = random.randint(2, n_at_s - 1)
            if (math.gcd(r, n_at_s) == 1):
                este_zstar = True

        return r

    def criptarePaillier(self, plaintext, n, g, random_seed, s):

        n_at_s = pow(n, s)
        n_at_s_p1 = pow(n, s + 1)

        return pow(g, plaintext, n_at_s_p1) * pow(random_seed, n_at_s, n_at_s_p1) % (n_at_s_p1)

    def decriptarePaillier(self, share, criptotext, nr_serv, verif_key, u, n, s):

        print("Decriptez...")

        delta = math.factorial(nr_serv)

        exponent = delta * share
        modulus = pow(n, s + 1)
        c_i = pow(criptotext, exponent, modulus)

        print(c_i)

        return c_i

    def lamda_calculation(self, nr_serv, indexes, index, n, s):
        delta = math.factorial(nr_serv)
        produs = delta
        modul = pow(n, s + 1)
        for i in indexes:
            if i != index:
                produs *= -index * pow(index - i, -1, modul)
                produs %= modul
        return produs

    def c_prim_calculation(self, nr_serv, indexes, cryptotexts, n, s):
        produs = 1
        modulus = pow(n, s + 1)
        for i in indexes:
            lamda_i = self.lamda_calculation(nr_serv, indexes, i, n, s)
            produs *= pow(cryptotexts[i - 1], 2 * lamda_i, modulus)
            produs %= modulus
        return produs

    def exponent_calculation(self, n, c_prim, s):
        i = 0
        for j in range(1, s + 1):
            modul = pow(n, j)
            t_1 = ((c_prim - 1) // modul) % modul
            t_2 = i
            for k in range(2, j + 1):
                i -= 1
                t_2 = t_2 * i % modul
                t_1 = t_1 - (t_2 * pow(n, k - 1, modul)) * pow(math.factorial(k), -1, modul)
                t_1 %= modul
            i = t_1
        return i

    def generareSirDeBiti(self, lungime):

        sir = ""

        for i in range(0, lungime):
            sir += str(random.randint(0, 1))

        return sir

    def gen_d_value(self, m, n, s):

        x = (pow(n, s) + 1) * pow(m, -1, pow(n, s))
        d = x * m

        print(d % pow(n, s) == 1)
        print(d % m == 0)
        print(d)
        print(n)
        print(m)

        return d

    def polynomyal_secret_sharing(self, d, k, n, s, m, x):

        coeficienti = []
        coeficienti.append(d)
        polynom_result = 0
        modulus = m * pow(n, s)

        for i in range(0, k - 1):
            coeficienti.append(random.randint(0, (m * (pow(n, s)) - 1)))

        for i in range(0, k):
            polynom_result += coeficienti[i] * pow(x, i)
            polynom_result %= modulus

        print(coeficienti)

        return polynom_result

    def split_shares(self, serv_number, n, d, m, k, s):

        shares = []
        for i in range(1, serv_number + 1):
            shares.append(self.polynomyal_secret_sharing(d, k, n, s, m, i))

        return shares

    def split_verif_values(self, u, nr_serv, shares, n, s):

        verif_values = []
        fact = math.factorial(nr_serv)

        for i in range(0, nr_serv):
            verif_values.append(pow(u, fact * shares[i], pow(n, s + 1)))

        return verif_values


obiect = CriptosistPaillier()
parametrii = obiect.setup()
n = parametrii[0]
m = parametrii[5]
u = parametrii[4]
g = parametrii[3]
s = 2
d = obiect.gen_d_value(m, n, s)
print(obiect.polynomyal_secret_sharing(d, 3, n, 2, m, 100))
shares = obiect.split_shares(4, n, d, m, 3, 2)
verif_val = obiect.split_verif_values(u, 4, shares, n, 2)

# obiect.decriptarePaillier(shares[0], 100, 4, verif_val[0], u, n, 2)
obiect.lamda_calculation(4, [1, 2, 3], 2, n, 2)
cryptotext = obiect.criptarePaillier(10, n, g, obiect.gen_random_seed(n, s), s)
c_1 = obiect.decriptarePaillier(shares[0], cryptotext, 4, verif_val[0], u, n, s)
c_2 = obiect.decriptarePaillier(shares[1], cryptotext, 4, verif_val[1], u, n, s)
c_3 = obiect.decriptarePaillier(shares[2], cryptotext, 4, verif_val[2], u, n, s)

print("Criptotext: " + str(cryptotext))
c_prim = obiect.c_prim_calculation(4, [1, 2, 3], [c_1, c_2, c_3], n, s)
exponent = obiect.exponent_calculation(n, c_prim, s)
delta_patrat=pow(math.factorial(4), 2)
print((exponent * pow(4 * delta_patrat, -1, pow(n, s))) % pow(n, s))
