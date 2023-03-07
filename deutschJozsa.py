from QuantumRegister import *

class DeutschJozsa:

    """
    Class which implements the Deutsch-Jozsa Algorithm

    Attributes: 
        oracle : Function which returns 0 or 1 for any output, either balanced or constant 
        n_qubits: number of qubits in the register, max value for the oracle must be 2 ** n_qubits - 1

    """

    def __init__(self, oracle, n_qubits):
        assert hasattr(oracle, '__call__')
        assert isinstance(n_qubits,int)
        
        self.oracle = oracle
        self.n_qubits_ = n_qubits
        self.n_states_ = 2 ** n_qubits
        self.register = QuantumRegister(n_qubits)

    def applyOracle(self):
        """
        Function which applies the oracle onto the state vector
        """
        for i in range(self.n_states_):
            self.register.state_[i] *= (-1) ** self.oracle(i)


    def deutschJozsaAlgorithm(self):
        """
        Function which implements the Deutsch-Jozsa Algorithm
        :return: returns True if oracle is balanced, or False if constant
        """
        for i in range(self.n_qubits_):
            self.register.applyGate(gate = self.register.hadamard, target = i)
        self.applyOracle()
        for i in range(self.n_qubits_ - 1):
            self.register.applyGate(gate = self.register.hadamard, target = i)
        state = self.register.measureState()
        if state & 1 == 1:
            return True
        else:
            return False