from register.QuantumRegister import *
import numpy as np
import pytest 

def twoBitEntanglement():
    print("--------- TWO BIT ENTANGLEMENT ---------")
    # This entanglement is to ensure the premise of our register is sound
    # It is used to non trivially entangle a two bit system
    # Following literature, a system of hadamard on qubit 0 and cnot on qubit 1
    # should produce a system of equal probabilities on state 00 and 11
    register = QuantumRegister(2)
    register.applyGate(register.hadamard,0)
    register.applyGate(register.pauli_x,1,0)
    expected = np.array([2**-.5, 0, 0, 2**-.5])
    if np.allclose(register.state_, expected):
        print("SUCCESSFUL ENTANGLEMENT\n")
    else:
        raise Exception("FAILED ENTANGLEMENT\n")

def testHadamardApplications():
    print("--------- TEST HADAMARD APPLICATIONS ---------")

    arr = []
    for i in range(2):
        for j in range(4):
            register = QuantumRegister(2, state = j)
            register.applyGate(gate = register.hadamard, target = i)
            n_counts = 20
            counts = register.measureStateNTimes(n_counts)
            arr.append((counts[j] + counts[j ^ (1 << i)] == n_counts))

    if all(arr):
        print("SUCCESSFUL HADAMARD APPLICATIONS\n")
    else:
        raise Exception("FAILED HADAMARD APPLICATIONS\n")

def testPauliXApplication():
    print("--------- TEST Pauli X APPLICATIONS ---------")

    arr = []
    for i in range(2):
        for j in range(4):
            register = QuantumRegister(2, state = j)
            register.applyGate(gate = register.pauli_x, target = i)
            n_counts = 20
            counts = register.measureStateNTimes(n_counts)
            arr.append((counts[j ^ (1 << i)] == n_counts))

    if all(arr):
        print("SUCCESSFUL PAULI X APPLICATIONS\n")
    else:
        raise Exception("FAILED PAULI X APPLICATIONS\n")




    

if __name__ == "__main__":

    twoBitEntanglement()

    testHadamardApplications()

    testPauliXApplication()