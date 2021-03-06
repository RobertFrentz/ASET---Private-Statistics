import random
from CriptosSistemPaillier import CriptosistPaillier
class RandomBitwiseGeneration:

    paillier_encrypt = CriptosistPaillier()


    def __init__(self,n,g,random_seed,s,share,nr_serv,k):
        self.gen_bit = random.randint(0,1)
        self.n = n
        self.g = g
        self.random_seed = random_seed
        self.s = s
        self.share = share
        self.nr_serv = nr_serv
        self.k = k


    def encrypt_bit(self):

         self.encrypted_bit = self.paillier_encrypt.criptarePaillier(self.gen_bit,self.n,self.g,self.random_seed,self.s)

         return  self.encrypted_bit

    def gen_cryptotext_for_shared_decryption(self, crypto_bit):

        return self.paillier_encrypt.decriptarePaillier(self.share,crypto_bit,self.nr_serv,self.n,self.s)






