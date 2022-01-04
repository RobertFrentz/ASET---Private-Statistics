import math

from Protocol import test_main
from Protocol.CriptosSistemPaillier import CriptosistPaillier


class StatisticalFunctions:
    paillier_encrypt = CriptosistPaillier()

    def __init__(self, values_encrypted, n, g, random_seed, s, shares, obiect, delta_patrat, l_x):
        self.values_encrypted = values_encrypted
        self.n = n
        self.g = g
        self.random_seed = random_seed
        self.s = s
        self.shares = shares
        self.obiect = obiect
        self.delta_patrat = delta_patrat
        self.nr_serv = 4
        self.k = 3
        self.modulus = pow(self.n, self.s + 1)
        self.number_of_elements = len(self.values_encrypted)
        self.l_x = l_x

    def mean(self):
        product = math.prod(self.values_encrypted) % self.modulus
        values_after_operations = test_main.calculate_function(product, self.number_of_elements, self.n, self.g,
                                                               self.random_seed, self.s,
                                                               self.shares,
                                                               self.obiect, self.delta_patrat, self.nr_serv, self.k, self.l_x)

        return round((values_after_operations[0] * self.number_of_elements + values_after_operations[
            1]) / self.number_of_elements,4)

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
                                                               self.obiect, self.delta_patrat, self.nr_serv, self.k, self.l_x)
        return round((values_after_operations[0] * (self.number_of_elements * (self.number_of_elements - 1)) +
                values_after_operations[
                    1]) / (self.number_of_elements * (self.number_of_elements - 1)),4)

    def standard_deviation(self):
        return round(math.sqrt(self.variance()),4)

    def standard_error(self):
        s=self.standard_deviation()
        square_n=math.sqrt(self.number_of_elements)
        return round(s / square_n,4)
