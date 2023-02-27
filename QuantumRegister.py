from Qubit import Qubit
import Operators as op
import numpy as np
import math

class QuantumRegister:
    def __init__(self, n_qubits):
        self.n_qubits_ = n_qubits
        self.n_states_ = 2**self.n_qubits_
        self.state_ = np.zeros(self.n_states_, dtype = complex)
        self.state_[0] = 1 
        self.hadamard = np.array(([1, 1], [1, -1])) / math.sqrt(2)
        self.NOT = np.array(([0, 1], [1, 0])) 
        self.T = np.array(([1, 0], [0, complex(np.cos(math.pi/4), np.sin(math.pi/4))]))
        self.T_dagger = np.array(([1, 0], [0, complex(np.cos(math.pi/4), -np.sin(math.pi/4))]))

    def setEqualSuperposition(self):
        self.state_ = np.ones(self.n_states_, dtype = complex) / math.sqrt(self.n_states_)
    
    def measureState(self):
        prob = np.abs((self.state_))**2
        index = np.random.choice(self.n_states_, p=prob)
        self.state_ = np.zeros(self.n_states_, dtype = complex)
        self.state_[index] = 1.0
        return index


    class QuantumRegister:
    def __init__(self, n_qubits, state = 0):
        self.n_qubits_ = n_qubits
        self.n_states_ = 2**self.n_qubits_
        self.state_ = np.zeros(self.n_states_, dtype = complex)
        self.state_[state] = 1 
        self.hadamard = np.array(([1, 1], [1, -1])) / math.sqrt(2)
        self.NOT = np.array(([0, 1], [1, 0])) 
        self.T = np.array(([1, 0], [0, complex(np.cos(math.pi/4), np.sin(math.pi/4))]))
        self.T_dagger = np.array(([1, 0], [0, complex(np.cos(-math.pi/4), np.sin(-math.pi/4))]))
        
    def setEqualSuperposition(self):
        self.state_ = np.ones(self.n_states_, dtype = complex) / math.sqrt(self.n_states_)
    
    def measureState(self):
        prob = np.abs((self.state_))**2
        index = np.random.choice(self.n_states_, p=prob)
        self.state_ = np.zeros(self.n_states_, dtype = complex)
        self.state_[index] = 1.0
        return index


    def applyGate(self, gate, target, control = None):
        assert gate.shape == (2, 2), f"Gate Matrix has wrong dimensions, please input a 2x2 array \n input array was of shape {gate.shape}"
        assert type(target) == int and target < self.n_qubits_, f"Target Qubit is outwith range of Qubits \nnumber of qubits was initialised as {self.n_qubits_}, however target qubit was {target}"
        if control != None:
            assert type(control) == int and control < self.n_qubits_, f"Control Qubit is out of range of Qubits \nnumber of qubits was initialised as {self.n_qubits_},  however control qubit was {control}"
            assert control != target, "Control qubit cannot equal target qubit"

        for i in range(self.n_states_):
            if (i >> target) & 1 == 0:
                if control != None:
                    if (i >> control) & 1 == 0:
                        continue
                a = i
                b = i ^ (1 << target)

                state_a = self.state_[a] 
                state_b = self.state_[b]  
                
                self.state_[a] = state_a * gate[0][0] + state_b * gate[0][1]
                self.state_[b] = state_a * gate[1][0] + state_b * gate[1][1]
                    







        




    #def applyHadamard(self, index):
    #    self.qubits_[index].hadamard() 

    # def applyCNOT(self, control, target):
    #     cnot = np.array([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0])
    #     state = np.array(self.qubits_[control], self.qubits_[target])
    #     state = op.matrixMultiply(cnot, state)
    #     self.qubits_[target].update(state[2][0], state[3][0]) 


    

    # TODO: define gates which act on two or more qubits, also figure it out 


        
