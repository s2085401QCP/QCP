import numpy as np 
import math 
from QuantumRegister import *

class Grovers:
    """
    Class which implements Grover's Algorithm 

    Attributes: 
        oracle: A function which flips a target state of a register, as a function that takes and returns the register
        list: A list to search 
    """

    def __init__(self, oracle, list, register):
        """
        Initialises Grovers class with: 
            n_qubits_ = log2(len(list))
            register = QuantumRegister(n_qubits)
            n_states_ = 2 ** n_qubits
        """
        assert register.n_states_ >= len(list)
        self.oracle = oracle
        self.register = register
        self.n_qubits_ = self.register.n_qubits_
        self.n_states_ = self.register.n_states_
        self.iterations = int((math.pi/4) * math.sqrt(self.n_states_) - 0.5)
         

    def applyOracle(self):
        self.register = self.oracle(self.register)
        

    def flipByMean(self):
        mu = (1/self.n_states_) * np.sum(self.register.state_)
        for i in range(self.register.n_states_):
            self.register.state_[i] = self.register.state_[i] - 2*mu

    def groversAlgorithm(self):
        self.register.setEqualSuperposition()
        for i in range(self.iterations):
            self.applyOracle()
            self.register.flipByMean()
        

    def findIndex(self):
        index = self.register.measureState()
        return index

    



