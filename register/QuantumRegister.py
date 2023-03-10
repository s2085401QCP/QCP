from register.Operators import *
import numpy as np
import math

class QuantumRegister:
    """
    Class which simulates a Quantum Register

    Class Attributes: 
        n_qubits = number of qubits to initialise class with;
        state = which state the class is initialised into, as an integer, set to 0;

    Stored Gates are: 
        hadamard;
        pauli_x;
        pauli_y;
        pauli_z;
        phase;
        T;
        T_dagger;
    """
    def __init__(self, n_qubits, state = 0):

        assert isinstance(n_qubits,int)
        assert isinstance(state,int)
        """
        Initialises the QuantumRegister class with: 
            n_states = 2 ** n_qubits
            state = np.zeros(n_states, dtype = complex)
        """
        self.n_qubits_ = n_qubits
        self.n_states_ = 2**self.n_qubits_
        # stores the state as a list of probabilities, where the index of the list is the integer representation of the binary string 
        # representing the vector
        self.state_ = np.zeros(self.n_states_, dtype = complex)
        self.state_[state] = 1 
        # 2x2 matrix which applies a hadamard gate
        self.hadamard = np.array(([1, 1], [1, -1])) / math.sqrt(2)
        # 2x2 matrix which applies a pauli X (NOT) gate
        self.pauli_x = np.array(([0, 1], [1, 0])) 
        # 2x2 matrix which applies a pauli Y gate
        self.pauli_y = np.array(([0, complex(0, -1)], [complex(0, 1), 0]))
        # 2x2 matrix which applies a pauli Z gate
        self.pauli_z = np.array(([1, 0], [0, -1]))
        # 2x2 matrix which applies a phase gate
        self.phase = np.array(([1, 0], [0, complex(0, 1)]))
        # 2x2 matrix which applies a T gate
        self.T = np.array(([1, 0], [0, complex(np.cos(math.pi/4), np.sin(math.pi/4))]))
        # 2x2 matrix which applies a T dagger gate
        self.T_dagger = np.array(([1, 0], [0, complex(np.cos(-math.pi/4), np.sin(-math.pi/4))]))
        
    def setEqualSuperposition(self):
        """
        Function which makes the register equally likely to be found in any state
        """
        self.state_ = np.zeros(self.n_states_)
        self.state_[0] = 1
        for i in range(self.n_qubits_):
            self.applyGate(gate = self.hadamard, target = i) 
    
    def measureState(self, return_uncollapsed_state = False):
        """
        Function which collapses the wavefunction, and so the register goes into a singular state
        :type return_uncollapsed_state: Bool
        :param return_uncollapsed_state: If true, function returns the uncollapsed state
        :return: index or (index, state) where index is the integer value of the state, and state is the uncollapsed state vector
        """
        prob = np.abs((self.state_))**2
        index = np.random.choice(self.n_states_, p=prob)
        if  not (return_uncollapsed_state):
            self.state_ = np.zeros(self.n_states_, dtype = complex)
            self.state_[index] = 1.0
            return index
        else:
            state = self.state_
            self.state_ = np.zeros(self.n_states_, dtype = complex)
            self.state_[index] = 1.0
            return index, state

    def getStateProbability(self, state):
        """
        Function which gets the probability that the register is in a specified state
        :type state: int or bitstring
        :param state: wanted state of the register
        :return: Probability that the register is in the specified state
        """
        assert isinstance(state, int) or isinstance(state, str), "state must be an integer or a bitstring"
        if isinstance(state, str):
            assert state.count("0") + state.count("1") == len(state), "input state must be a bitstring"
            assert int(state, 2) >= self.n_qubits_, "Bitstring input is greater than the number of states of the register"
            state = int(state, 2)
        prob = abs(self.state_[state])**2
        return prob 

    def measureStateNTimes(self, n):
        """
        Function that measures the register n times, and counts how many times each state is collapsed to
        :type n: int
        :param n: number of times to measure the registers state
        :return: a list of length n_states_, with each value showing how many times the register collapsed into that state
        """
        assert isinstance(n, int), "n must be an integer"
        
        counts = np.zeros(self.n_states_)
        for _ in range(n):
            index, state = self.measureState(return_uncollapsed_state = True)
            counts[index] += 1
            self.state_ = state
        return counts



    def applyGate(self, gate, target, control = None):
        """
        Function that applies an arbitrary gate to a specified qubit, with an optional control qubit
        :type gate: np.ndarray
        :param gate: A 2x2 matrix which operates on a qubit
        :type target: int
        :param target: index of the target qubit
        :type control: tuple, int or None
        :param control: index of the control qubit(s), if not None
        """
        assert gate.shape == (2, 2), f"Gate Matrix has wrong dimensions, please input a 2x2 array \n input array was of shape {gate.shape}"
        assert np.allclose(np.eye(len(gate)), gate.dot(gate.T.conj())), "Gate matrix must be Unitary"
        assert type(target) == int and target < self.n_qubits_, f"Target Qubit is outwith range of Qubits \nnumber of qubits was initialised as {self.n_qubits_}, however target qubit was {target}"
        if control != None:
            if isinstance(control, int):
                assert control < self.n_qubits_, f"Control Qubit is out of range of Qubits \nnumber of qubits was initialised as {self.n_qubits_},  however control qubit was {control}"
                assert control != target, "Control qubit cannot equal target qubit"
            elif isinstance(control, tuple):
                assert isinstance(control, tuple), "Control qubit must be an integer or a tuple"
                assert all([type(i) == int for i in control]), "Control qubits must be integers"
                assert target not in control, "Target qubit cannot be in the control qubit tuple"
            else:
                raise TypeError("Control qubit must be an integer or a tuple")
        for i in range(self.n_states_):

            # checks if the target qubit is 0
            if (i >> target) & 1 == 0:
                flag = False
                # checks if the control qubit is 0, and if so skips this iteration
                if control is not None:
                    if isinstance(control, tuple):
                        if not all([(i >> j) & 1 == 1 for j in control]):
                            #flag = True
                            continue
                    elif isinstance(control, int):
                        if (i >> control) & 1 == 0:
                            #flag = True
                            continue
                # if flag:
                #     continue
                # a is the integer representation of the state where the target qubit is 0
                a = i

                # b is the integer representation of a where the target qubit has been flipped
                b = i ^ (1 << target)

                # the probability of finding the register in either of these states
                state_a = self.state_[a] 
                state_b = self.state_[b] 

                # updates the probabilities of each state according to the 2x2 input matrix
                self.state_[a] = state_a * gate[0][0] + state_b * gate[0][1]
                self.state_[b] = state_a * gate[1][0] + state_b * gate[1][1]


    def toffoli(self, target, control):
        """
        Function to apply the toffoli (controlled-controlled Not Gate) to a target qubit
        :type target: int
        :param target: index of the target qubit
        :type conrol: tuple
        :param control: tuple of the index's of the two control qubits
        """
        assert type(control) == tuple and len(control) == 2, "Number of Control qubits needs to be a tuple of length 2"
        assert type(target) == int and type(control[0]) == int and type(control[1]) == int, "qubits need to be given as integers"
        c0 = control[0]
        c1 = control[1]
        self.applyGate(gate = self.hadamard, target = target)
        self.applyGate(gate = self.pauli_x, target = target, control = c0)
        self.applyGate(gate = self.T_dagger, target = target)
        self.applyGate(gate = self.pauli_x, target = target, control = c1)
        self.applyGate(gate = self.T, target = target)
        self.applyGate(gate = self.pauli_x, target = target, control = c0)
        self.applyGate(gate = self.T_dagger, target = target)
        self.applyGate(gate = self.pauli_x, target = target, control = c1)
        self.applyGate(gate = self.T, target = target)
        self.applyGate(gate = self.T, target = c0)
        self.applyGate(gate = self.hadamard, target = target)
        self.applyGate(gate = self.pauli_x, target = c0, control = c1)
        self.applyGate(gate = self.T_dagger, target = c0)
        self.applyGate(gate = self.T, target = c1)
        self.applyGate(gate = self.pauli_x, target = c0, control = c1)

    def contrZ(self, target, control):
        """
        Function which applies the controlled Z gate onto a target qubit, using a control qubit
        :type target: int
        :param target: Index of the target qubit
        :type control: int
        :param control: Index of the control qubit
        """
        assert type(target) == int and type(control) == int, "Target or control is not of type int"
        assert target < self.n_qubits_, f"Target Qubit is outwith range of Qubits \nnumber of qubits was initialised as {self.n_qubits_}, however target qubit was {target}"
        assert control < self.n_qubits_, f"Control Qubit is outwith range of Qubits \nnumber of qubits was initialised as {self.n_qubits_}, however control qubit was {control}"
        self.applyGate(gate = self.hadamard, target = target)
        self.applyGate(gate = self.pauli_x, target = 0, control = control)
        self.applyGate(gate = self.hadamard, target = target)
                    


        
