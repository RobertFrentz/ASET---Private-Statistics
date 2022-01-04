from Protocol.CriptosSistemPaillier import CriptosistPaillier
from Protocol.StatisticalFunctions import StatisticalFunctions
from users.file_helper import read_paillier_setup
from users.statistic_strategy import StatisticStrategy


class MeanStrategy(StatisticStrategy):
    def compute_statistic(self, attribute_values):
        n, g, random_seed, s, shares, delta_patrat = read_paillier_setup()
        obiect = CriptosistPaillier()
        statistic = StatisticalFunctions(attribute_values, n, g, random_seed, s, shares, obiect, delta_patrat, 7)
        return statistic.mean()
