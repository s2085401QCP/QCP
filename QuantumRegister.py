from Qubit import Qubit
import Operators as op
import numpy as np
import math

class QuantumRegister:
    def __init__(self, n_qubits):
        self.n_qubits_ = n_qubits
        self.n_states_ = 2**self.n_qubits_
        self.qubits_ = [Qubit(1, 0) for _ in range(self.n_qubits_)]
        self.state_ = np.zeros(self.n_qubits_, self.n_qubits_)
        self.state_[0][0] = 1 

    def setEqualSuperposition(self):
        self.state_ = np.ones((self.n_qubits_, self.n_qubits_)) / math.sqrt(self.n_qubits_)
    
    def measureState(self):
        prob = np.sum(np.abs(self.state_)**2, axis=0)
        index = np.random.choice(2**self.n_qubits_, p=prob)
        self.state = np.zeros((2**self.n_qubits_, 2**self.n_qubits_))
        self.state[index, index] = 1.0
        return index

    def applyHadamard(self, index):
        self.qubits_[index].hadamard() 

    def applyCNOT(self, control, target):
        pass

    

    # TODO: define gates which act on two or more qubits, also figure it out 


        
