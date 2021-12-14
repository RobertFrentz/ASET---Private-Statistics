import math

from Protocol import test_main
from Protocol.CriptosSistemPaillier import CriptosistPaillier


class StatisticalFunctions:
    paillier_encrypt = CriptosistPaillier()

    def __init__(self, values_list, n, g, random_seed, s, shares, obiect, delta_patrat):
        self.values_encrypted = []
        self.values_list = values_list
        self.n = n
        self.g = g
        self.random_seed = random_seed
        self.s = s
        self.shares = shares
        self.obiect = obiect
        self.delta_patrat = delta_patrat
        self.nr_serv = 4
        self.k = 3
        self.encrypt_values()
        self.modulus = pow(self.n, self.s + 1)
        self.number_of_elements = len(self.values_list)

    def encrypt_values(self):
        for value in self.values_list:
            encrypt = self.paillier_encrypt.criptarePaillier(value, self.n, self.g, self.random_seed, self.s)
            self.values_encrypted.append(encrypt)
        return self.values_encrypted

    def mean(self):
        product = math.prod(self.values_encrypted) % self.modulus
        values_after_operations = test_main.calculate_function(product, self.number_of_elements, self.n, self.g,
                                                               self.random_seed, self.s,
                                                               self.shares,
                                                               self.obiect, self.delta_patrat, self.nr_serv, self.k)

        return (values_after_operations[0] * self.number_of_elements + values_after_operations[
            1]) / self.number_of_elements

    def variance(self):

        values_encrypted_squares = []
        for value in self.values_encrypted:
            values_encrypted_squares.append(
                test_main.calculate_a_multiply_b(value, value, self.n, self.g, self.random_seed, self.s, self.shares,
                                                 self.obiect, self.delta_patrat, self.nr_serv, self.k))
        sum_of_square_values_encrypted = math.prod(values_encrypted_squares) % self.modulus
        sum_of_square_values_encrypted = pow(sum_of_square_values_encrypted, len(values_encrypted_squares),
                                             self.modulus)
        product = math.prod(self.values_encrypted) % self.modulus
        product_square = test_main.calculate_a_multiply_b(product, product, self.n, self.g, self.random_seed, self.s,
                                                          self.shares,
                                                          self.obiect, self.delta_patrat, self.nr_serv, self.k)
        product_square = pow(product_square, -1, self.modulus)
        v_encrypted = sum_of_square_values_encrypted * product_square % self.modulus
        values_after_operations = test_main.calculate_function(v_encrypted,
                                                               self.number_of_elements * (self.number_of_elements - 1),
                                                               self.n,
                                                               self.g, self.random_seed, self.s, self.shares,
                                                               self.obiect, self.delta_patrat, self.nr_serv, self.k)
        return (values_after_operations[0] * (self.number_of_elements * (self.number_of_elements - 1)) +
                values_after_operations[
                    1]) / (self.number_of_elements * (self.number_of_elements - 1))

    def standard_deviation(self):
        return math.sqrt(self.variance())

    def standard_error(self):
        s=self.standard_deviation()
        square_n=math.sqrt(self.number_of_elements)
        return s / square_n
