from strategy_protocols import Strategy
from CriptosSistemPaillier import CriptosistPaillier

class PaillierBasedStrategy(Strategy):


    instanta_paillier = CriptosistPaillier()

    def protocol_algorithm(self):
        #to be continued
        self.instanta_paillier.setup()

        pass

    def print_protocol_message(self):

        print("Using a Paillier criptosystem based protocol!")






