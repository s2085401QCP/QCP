import numpy as np 
import math 
from register.QuantumRegister import *

class Grovers:
    """
    Class which implements Grover's Algorithm 

    Attributes: 
        oracle: A function which flips a target state of a register, as a function that takes and returns the registers state vector
        list: A list to search 
        register: A quantum register with n_qubits >= log2(len(list))
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
        self.iterations = int((math.pi/4) * math.sqrt(self.n_states_))
         

    def applyOracle(self):
        self.register.state_ = self.oracle(self.register)
        

    def flipByMean(self):
        mu = (1/self.n_states_) * np.sum(self.register.state_)
        for i in range(self.register.n_states_):
            self.register.state_[i] = self.register.state_[i] - 2*mu

    def groversAlgorithm(self):
        self.register.setEqualSuperposition()
        for i in range(self.iterations):
            self.applyOracle()
            self.flipByMean()
        

    def findIndex(self):
        index = self.register.measureState()
        return index

    




