from Qubit import Qubit
import Operators as op
import numpy as np
import math

class QuantumRegister:
    def __init__(self, n_qubits):
        self.n_qubits_ = n_qubits
        self.n_states_ = 2**self.n_qubits_
        self.state_ = np.zeros(self.n_states_)
        self.state_[0] = 1 
        self.hadamard = np.eye(2)
        self.CNOT = np.eye(2) 

    def setEqualSuperposition(self):
        self.state_ = np.ones(self.n_states_) / math.sqrt(self.n_states_)
    
    def measureState(self):
        prob = np.abs((self.state_))**2
        index = np.random.choice(self.n_states_, p=prob)
        self.state_ = np.zeros(self.n_states_)
        self.state_[index] = 1.0
        return index


    def applyGate(self, gate, target, control = None):
        assert gate.shape == (2, 2), "Gate Matrix has wrong dimensions"
        assert type(target) == int and target < self.n_qubits_, "Target Qubit is outwith range of Qubits"
        if control is not None:
            assert type(control) == int and control < self.n_qubits_, "Control Qubit is out of range of Qubits"

        for i in range(self.n_states_/2):
            if (i >> target) & 1 == 0:
                a = i
                b = i ^ (1 << target)

                state_a = self.state_[a] 
                state_b = self.state_[b] 

                if control is not None:
                    if (i >> control) & 1 == 0:
                        continue
                else: 
                    self.state_[a] = self.state_[a] * gate[0][0] + self.state_[b] * gate[0][1]
                    self.state_[b] = self.state_[a] * gate[1][0] + self.state_[b] * gate[1][1]








        




    #def applyHadamard(self, index):
    #    self.qubits_[index].hadamard() 

    # def applyCNOT(self, control, target):
    #     cnot = np.array([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0])
    #     state = np.array(self.qubits_[control], self.qubits_[target])
    #     state = op.matrixMultiply(cnot, state)
    #     self.qubits_[target].update(state[2][0], state[3][0]) 


    

    # TODO: define gates which act on two or more qubits, also figure it out 


        
