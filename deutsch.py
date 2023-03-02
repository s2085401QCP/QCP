import QuantumRegister
import numpy as np 
import math 

class Deutsch:

    def __init__(oracle):
        self.register = QuantumRegister(2)
        self.n_qubits_ = 2
        self.n_states_ = 2 ** self.n_qubits_
        self.oracle = oracle


    def deutschAlgorithm(self):
        for i in range(self.n_qubits_):
            self.register.applyGate(gate = self.register.hadamard, target = i)
        for i in range(self.n_qubits_):
            self.register.state_[i] *= (-1) ** self.oracle(i)
        for i in range(self.n_qubits_):
            self.register.applyGate(gate = self.register.hadamard, target = i)
        if abs(self.register.state[0]) == 1:
            print("Oracle is Constant")
        else:
            print("Oracle is Balanced")


