import math

from TCR import TCR
from CriptosSistemPaillier import CriptosistPaillier
from RandomBitwiseGen import RandomBitwiseGeneration
from ModuloReduction import ModuloReduction

# param genn

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


# plaintext = 10
# cryptotext = obiect.criptarePaillier(plaintext, n, g, obiect.gen_random_seed(n, s), s)
# print(obiect.decryption_sharing(10, n, s, shares, delta_patrat))
# a = 12


def calculate_function(x, a):
    while True:
        Serv_1 = RandomBitwiseGeneration(n, g, random_seed, s, shares[0], 4, 3)
        Serv_2 = RandomBitwiseGeneration(n, g, random_seed, s, shares[1], 4, 3)
        Serv_3 = RandomBitwiseGeneration(n, g, random_seed, s, shares[2], 4, 3)
        Serv_4 = RandomBitwiseGeneration(n, g, random_seed, s, shares[3], 4, 3)

        servers = [Serv_1, Serv_2, Serv_3, Serv_4]
        # share decryption
        bit_plain_list = [Serv_1.gen_bit, Serv_2.gen_bit, Serv_3.gen_bit, Serv_4.gen_bit]
        bitlist = [Serv_1.encrypt_bit(), Serv_2.encrypt_bit(), Serv_3.encrypt_bit(), Serv_4.encrypt_bit()]
        decrypted_bit_list = []

        indexes = [1, 2, 3, 4]
        for bit in bitlist:
            decrypted_bits = []
            for serv in servers:
                decrypted_bits.append(serv.gen_cryptotext_for_shared_decryption(bit))

            bit_prime = obiect.c_prim_calculation(4, indexes, decrypted_bits, n, s)
            exponent = obiect.exponent_calculation(n, bit_prime, s)

            decrypted_bit_list.append((exponent * pow(4 * delta_patrat, -1, pow(n, s))) % pow(n, s))

        bit_String = "".join([str(i) for i in decrypted_bit_list])

        # print(bit_plain_list)
        # print(decrypted_bit_list)
        # print(int(bit_String, 2))

        r = int(bit_String, 2)
        if r < a: break

    modulRed = ModuloReduction(n, g, random_seed, s, 4, 3, r, x, a)
    l_s = modulRed.generate_l_s()
    l_x = int.bit_length(x)

    S_i_list = []
    for i in range(0, 4):
        S_i_list.append(modulRed.generate_s_i(l_s, l_x))

    x_prime = modulRed.compute_x_at_step_2(S_i_list)

    cryptotexts_list = [obiect.decriptarePaillier(shares[0], x_prime, 4, n, s),
                        obiect.decriptarePaillier(shares[1], x_prime, 4, n, s),
                        obiect.decriptarePaillier(shares[2], x_prime, 4, n, s),
                        obiect.decriptarePaillier(shares[3], x_prime, 4, n, s),
                        ]

    c_prime_for_x_prime = obiect.c_prim_calculation(4, [1, 2, 3, 4], cryptotexts_list, n, s)
    exponent_for_x_prime = obiect.exponent_calculation(n, c_prime_for_x_prime, s)
    x_prime_decrypted = (exponent_for_x_prime * pow(4 * delta_patrat, -1, pow(n, s))) % pow(n, s)
    x_second = x_prime_decrypted % a
    x_second_encrypted = obiect.criptarePaillier(x_second, n, g, random_seed, s)

    if a - 1 - x_second < r:
        c = 1
    else:
        c = 0
    # c = 1 if (a - 1 - x_second) < r == True else 0
    c_encrypted = obiect.criptarePaillier(c, n, g, random_seed, s)

    result_encrypted = modulRed.compute_mod_x_A(c_encrypted, x_second_encrypted)

    cryptotexts_list_second = [obiect.decriptarePaillier(shares[0], result_encrypted, 4, n, s),
                               obiect.decriptarePaillier(shares[1], result_encrypted, 4, n, s),
                               obiect.decriptarePaillier(shares[2], result_encrypted, 4, n, s),
                               obiect.decriptarePaillier(shares[3], result_encrypted, 4, n, s),
                               ]

    c_prime_for_final_result = obiect.c_prim_calculation(4, [1, 2, 3, 4], cryptotexts_list_second, n, s)
    exponent_for_final_result = obiect.exponent_calculation(n, c_prime_for_final_result, s)
    final_result_decrypted = (exponent_for_final_result * pow(4 * delta_patrat, -1, pow(n, s))) % pow(n, s)

    # print("c value: " + str(c) + " final: " + str(final_result_decrypted))
    return final_result_decrypted


