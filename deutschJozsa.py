import QuantumRegister

class DeutschJozsa:

    """
    Class which implements the Deutsch-Jozsa Algorithm

    Attributes: 
        oracle : Function which returns 0 or 1 for any output, either balanced or constant 
        n_qubits: number of qubits in the register, max value for the oracle must be between 0 and 2 ** n_qubits - 1

    """

    def __init__(oracle, n_qubits):
        self.oracle = oracle
        self.n_qubits_ = n_qubits
        self.n_states_ = 2 ** n_qubits
        self.register = QuantumRegister(self.n_qubits_)

    def applyOracle(self):
        """
        Function which applies the oracle onto the state vector
        """
        for i in range(self.n_states_):
            self.register.state_[i] *= (-1) ** self.oracle(i)


    def deutschJozsaAlgorithm(self, return_isBalanced = False):
        """
        Function which implements the Deutsch-Jozsa Algorithm
        :type return_isBalanced: Bool
        :param return_isBalanced: True if wanting function to return a boolean value
        :return: if return_isBalanced is True, returns True if oracle is balanced
        """
        for i in range(self.n_qubits_):
            self.register.applyGate(gate = self.register.hadamard, target = i)
        self.applyOracle()
        for i in range(self.n_qubits_ - 1):
            self.register.applyGate(gate = self.hadamard, target = i)
        state = self.register.measureState()
        if state & 1 == 1:
            print("Oracle is Balanced")
            if return_isBalanced:
                return True
        else:
            print("Oracle is Constant")
            if return_isBalanced:
                return False