from QuantumRegister import *

class Deutsch:
    """
    Class which implements Deutsch's Algorithm

    Attributes: 
        oracle: A function which is either balanced or constant, which returns 1 or 0
    """

    def __init__(self, oracle, register):
        assert register.n_qubits_ == 2
        self.register = register
        self.n_qubits_ = 2
        self.n_states_ = 2 ** self.n_qubits_
        self.oracle = oracle


    def deutschAlgorithm(self):
        """
        Function which implements Deutsch's Algorithm, optional return of boolean
        :return: True if oracle is balanced, or False if constant
        """
        for i in range(self.n_qubits_):
            self.register.applyGate(gate = self.register.hadamard, target = i)
        for i in range(self.n_states_):
            self.register.state_[i] *= (-1) ** self.oracle(i)
        self.register.applyGate(gate = self.register.hadamard, target = 0)
        state = self.register.measureState()
        if state & 1 == 1:
            return True
        else:
            return False


