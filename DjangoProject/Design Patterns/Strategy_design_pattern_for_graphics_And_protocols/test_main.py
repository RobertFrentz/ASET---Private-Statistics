import math

from TCR import TCR
from CriptosSistemPaillier import CriptosistPaillier
from RandomBitwiseGen import RandomBitwiseGeneration
from ModuloReduction import ModuloReduction
#param genn

obiect = CriptosistPaillier()
tcr = TCR()
parametrii = obiect.setup(1)
n = parametrii[0]
m = parametrii[5]
u = parametrii[4]
g = n+1
s = 1
exp = [0, 1]
m_list = [m, pow(n, s)]
d = tcr.chinese_remainder(m_list, exp)
shares = obiect.split_shares(4, n, d, m, 3, s)
random_seed = obiect.gen_random_seed(n,s)
delta_patrat = pow(math.factorial(4),2)
a=12

while True:
    Serv_1 = RandomBitwiseGeneration(n,g,random_seed,s,shares[0],4,3)
    Serv_2 = RandomBitwiseGeneration(n,g,random_seed,s,shares[1],4,3)
    Serv_3 = RandomBitwiseGeneration(n,g,random_seed,s,shares[2],4,3)
    Serv_4 = RandomBitwiseGeneration(n,g,random_seed,s,shares[3],4,3)

    servers = [Serv_1,Serv_2,Serv_3,Serv_4]
    #share decryption
    bit_plain_list = [Serv_1.gen_bit,Serv_2.gen_bit,Serv_3.gen_bit,Serv_4.gen_bit]
    bitlist = [Serv_1.encrypt_bit(),Serv_2.encrypt_bit(),Serv_3.encrypt_bit(),Serv_4.encrypt_bit()]
    decrypted_bit_list = []

    indexes = [1,2,3,4]
    for bit in bitlist:
        decrypted_bits = []
        for serv in servers:

            decrypted_bits.append(serv.gen_cryptotext_for_shared_decryption(bit))

        bit_prime = obiect.c_prim_calculation(4,indexes,decrypted_bits,n,s)
        exponent = obiect.exponent_calculation(n,bit_prime,s)

        decrypted_bit_list.append((exponent * pow(4 * delta_patrat, -1, pow(n, s))) % pow(n, s))


    bit_String = "".join([str(i) for i in decrypted_bit_list])

    print(bit_plain_list)
    print(decrypted_bit_list)
    print(int(bit_String,2))

    r = int(bit_String,2)
    if (r < a): break

x=5
modulRed= ModuloReduction(n,g,random_seed,s,4,3,r,x,a)
l_s=modulRed.generate_l_s()
l_x=int.bit_length(x)
print(modulRed.generate_s_i(l_s,l_x))
print("R final: " + str(r))













