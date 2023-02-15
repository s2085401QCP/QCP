import numpy as np 
import math 
import Operators as op
import Register as register 
from Qubit import Qubit

class Grovers:

    def __init__(self, wanted_state, register):
        self.qubits_ = register.qubits
        self.n_qubits_ = register.n_qubits_
        self.n_states_ = register.n_states_
        self.register = register 
        self.wanted_state = wanted_state

        self.iterations = (np.pi / 4) * math.sqrt((2**self.n_states_)/len(wanted_state))

        self.state = 1/(self.n_states_) * np.ones(self.n_states_)

        self.previous_state = self.state

        self.oracle = np.eye(self.n_qubits_)

    def oracle(self):
        for state in self.wanted_state: 
            self.oracle[state][state] = -1

    def oneStepGrover(self):
        op.matrixMultiply(self.oracle, self.state)
        mean_average = np.mean(self.state)
        self.previous_state = self.state
        self.state = 2*mean_average - self.state
        pass 

    def groversAlgorithm(self):
        for _ in range(self.iterations):
            self.oneStepGrover() 
        return self.state

    def getFinalState(self):
        probability = np.abs(self.state)**2
        measurement = np.random.choice(self.n_states_, p = probability)
        return measurement




