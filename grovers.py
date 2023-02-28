import numpy as np 
import math 
import Operators as op
import QuantumRegister as qr

class Grovers:
    """
    Class which implements Grover's Algorithm 

    Attributes: 
        oracle: A function which returns 1 for a chosen item, or 0 otherwise
        list: A list to search 
    """

    def __init__(self, oracle, list):
        """
        Initialises Grovers class with: 
            n_qubits_ = log2(len(list))
            register = QuantumRegister(n_qubits)
            n_states_ = 2 ** n_qubits
        """
        self.oracle = oracle
        self.n_qubits_ = math.ceil(math.log2(len(list))) 
        self.register = QuantumRegister(self.n_qubits_)
        self.n_states_ = self.register.n_states_
         

    def applyOracle(self):
        for i in range(self.n_states_):
            self.register.state_[i] *= ((-1) ** self.oracle(i))
        

    def groversOneIteration(self):
        self.applyOracle()
        mu = (1/self.n_states_) * np.sum(self.register.state_)
        for i in range(register.n_states_):
            self.register.state_[i] = self.register.state_[i] - 2*mu

    def groversAlgorithm(self):
        self.register.setEqualSuperposition()
        for i in range(int((math.pi/4) * math.sqrt(self.n_states_) - 0.5)):
            self.register.groversOneIteration()
        

    def findIndex(self):
        index = self.register.measureState()
        return index

    




