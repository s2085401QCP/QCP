import numpy as np 
import math 
import Operators as op
import QuantumRegister as qr

class Grovers:

    def __init__(self, oracle, list):
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

    def findIndex(self):
        index = self.register.measureState()
        return index

    




