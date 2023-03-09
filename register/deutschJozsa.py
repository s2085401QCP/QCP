from register.QuantumRegister import *

class DeutschJozsa:

    """
    Class which implements the Deutsch-Jozsa Algorithm

    Attributes: 
        oracle : Function which applies to a quantum register and returns the register in a new state 
        n_qubits: number of qubits in the register, max value for the oracle must be 2 ** n_qubits - 1

    """

    def __init__(self, oracle, register):
        self.oracle = oracle
        self.n_qubits_ = register.n_qubits_
        self.n_states_ = register.n_states_
        self.register = register

    def applyOracle(self):
        """
        Function which applies the oracle onto the state vector
        """
        self.register.state_ = self.oracle(self.register)


    def deutschJozsaAlgorithm(self):
        """
        Function which implements the Deutsch-Jozsa Algorithm
        :return: True if oracle is balanced, or False if constant
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