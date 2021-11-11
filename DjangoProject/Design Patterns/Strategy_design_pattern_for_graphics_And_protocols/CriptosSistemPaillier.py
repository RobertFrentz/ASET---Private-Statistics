import math
import random
from Crypto.Util import number
from sympy.ntheory import discrete_log


class CriptosistPaillier:

    def setup(self, s):

        # criptosistemul Paillier: generam parametrii pentru criptare/decriptare

        p_prim = number.getPrime(50)
        q_prim = number.getPrime(50)
        while not number.isPrime(2 * p_prim + 1):
            p_prim = number.getPrime(50)
        while not number.isPrime(q_prim * 2 + 1):
            q_prim = number.getPrime(50)
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

    def criptarePaillier(self, plaintext, n, g, random_seed, s):

        n_at_s = pow(n, s)
        n_at_s_p1 = pow(n, s + 1)

        return (pow(g, plaintext, n_at_s_p1) * pow(random_seed, n_at_s, n_at_s_p1)) % (n_at_s_p1)

    def decriptarePaillier(self, share, criptotext, nr_serv, verif_key, u, n, s):

        # print("Decriptez...")

        delta = math.factorial(nr_serv)

        exponent = delta * share*2
        modulus = pow(n, s + 1)
        c_i = pow(criptotext, exponent, modulus)

        # print(c_i)

        return c_i

    def lamda_calculation(self, nr_serv, indexes, index):
        delta = math.factorial(nr_serv)
        produs = delta
        for i in indexes:
            if i != index:
                val = -index // (index - i)
                produs *= val
        return produs

    def c_prim_calculation(self, nr_serv, indexes, cryptotexts, n, s):
        produs = 1
        modulus = pow(n, s + 1)
        for i in indexes:
            lamda_i = self.lamda_calculation(nr_serv, indexes, i)
            produs *= pow(cryptotexts[i - 1], 2 * lamda_i, modulus)
            produs %= modulus
        return produs

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

        # print(d % pow(n, s) == 1)
        # print(d % m == 0)
        # print(d)
        # print(n)
        # print(m)

        return d

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


obiect = CriptosistPaillier()
parametrii = obiect.setup(1)
n = 77
m = 15
u = parametrii[4]
g = 78
s = 1
d = obiect.gen_d_value(m, n, s)
print("D: " + str(d))
shares = obiect.split_shares(4, n, d, m, 3, s)
verif_val = obiect.split_verif_values(u, 4, shares, n, s)

# obiect.decriptarePaillier(shares[0], 100, 4, verif_val[0], u, n, 2)
obiect.lamda_calculation(4, [1, 2, 3], 2)
cryptotext = obiect.criptarePaillier(10, n, g, 3, s)
c_1 = obiect.decriptarePaillier(shares[0], cryptotext, 4, verif_val[0], u, n, s)
c_2 = obiect.decriptarePaillier(shares[1], cryptotext, 4, verif_val[1], u, n, s)
c_3 = obiect.decriptarePaillier(shares[2], cryptotext, 4, verif_val[2], u, n, s)
delta_patrat = pow(math.factorial(4), 2)
print("Criptotext: " + str(cryptotext))

c_prim = obiect.c_prim_calculation(4, [1, 2, 3], [c_1, c_2, c_3], n, s)

print("C_prim: " + str(c_prim))
print("Verificare: " + str(pow(cryptotext, 4 * delta_patrat * d, pow(n, s + 1))))
exponent = obiect.exponent_calculation(77, c_prim, s)

print((exponent * pow(4 * delta_patrat, -1, pow(n, s))) % pow(n, s))
