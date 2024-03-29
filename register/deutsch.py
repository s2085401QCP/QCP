from register.QuantumRegister import *

class Deutsch:
    """
    Class which implements Deutsch's Algorithm

    Attributes: 
        oracle: A function which is either balanced or constant, which takes a register object, and returns a state vector
        register: A 2 qubit quantum register
    """

    def __init__(self, oracle, register):
        assert register.n_qubits_ == 2
        self.register = register
        self.n_qubits_ = 2
        self.n_states_ = 2 ** self.n_qubits_
        self.oracle = oracle
    
    def applyOracle(self):
        """
        Function which applies the oracle onto the state vector
        """
        self.register.state_ = self.oracle(self.register)

    def deutschAlgorithm(self):
        """
        Function which implements Deutsch's Algorithm, optional return of boolean
        :return: True if oracle is balanced, or False if constant
        """
        self.register.setEqualSuperposition()
        self.applyOracle()
        self.register.applyGate(gate = self.register.hadamard, target = 0)
        state = self.register.measureState()
        if state & 1 == 1:
            return True
        else:
            return False


