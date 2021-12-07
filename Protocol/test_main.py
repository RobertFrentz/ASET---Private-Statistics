import math

from TCR import TCR
from CriptosSistemPaillier import CriptosistPaillier
from RandomBitwiseGen import RandomBitwiseGeneration
from ModuloReduction import ModuloReduction


def calculate_function(x, a, n, g, random_seed, s, shares, obiect, delta_patrat, nr_serv, k):
    while True:
        Serv_1 = RandomBitwiseGeneration(n, g, random_seed, s, shares[0], nr_serv, k)
        Serv_2 = RandomBitwiseGeneration(n, g, random_seed, s, shares[1], nr_serv, k)
        Serv_3 = RandomBitwiseGeneration(n, g, random_seed, s, shares[2], nr_serv, k)
        Serv_4 = RandomBitwiseGeneration(n, g, random_seed, s, shares[3], nr_serv, k)

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

    modulRed = ModuloReduction(n, g, random_seed, s, nr_serv, k, r, x, a)
    l_s = modulRed.generate_l_s()

    # aici e bugul dragilor, aparent noi folosim l_x ca lungimea criptarii, si nu a lui x :(
    l_x = int.bit_length(1 + 2 + 5 + 4 + 6)

    S_i_list = []
    for i in range(0, 4):
        S_i_list.append(modulRed.generate_s_i(l_s, l_x))

    x_prime = modulRed.compute_x_at_step_2(S_i_list)
    x_prime_decrypted = obiect.decryption_sharing(x_prime, n, s, shares, delta_patrat, nr_serv)
    x_second = x_prime_decrypted % a
    x_second_encrypted = obiect.criptarePaillier(x_second, n, g, random_seed, s)

    c = 1 if a - 1 - x_second < r else 0
    c_encrypted = obiect.criptarePaillier(c, n, g, random_seed, s)

    result_encrypted = modulRed.compute_mod_x_A(c_encrypted, x_second_encrypted)

    final_result_decrypted = obiect.decryption_sharing(result_encrypted, n, s, shares, delta_patrat, nr_serv)
    # print("c value: " + str(c) + " final: " + str(final_result_decrypted))


    div = x * pow(result_encrypted,-1,pow(n,s+1))
    div = pow(div, pow(a,-1,pow(n,s+1) ),pow(n,s+1))

    print(obiect.decryption_sharing(div,n,s,shares,delta_patrat,nr_serv))


    return final_result_decrypted
