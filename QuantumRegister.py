from Qubit import Qubit
import Operators as op
import numpy as np
import math

class QuantumRegister:
    def __init__(self, n_qubits):
        self.n_qubits_ = n_qubits
        self.n_states_ = 2**self.n_qubits_
        self.state_ = [Qubit(1, 0) for _ in range(n_qubits)]

    def superPosition(self):
        for i in self.state_:
            i.equalSuperposition()
    
    def measureState(self):
        for i in self.state_:
            i.measure()
        binary_string = ""
        for i in self.state_:
            binary_string += str(int(i[1]))
        return int(binary_string, 2)

    # TODO: define gates which act on two or more qubits, also figure it out 


        
