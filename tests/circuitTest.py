from register.QuantumRegister import QuantumRegister
import numpy as np

def checkExpected(state,expected):
    match = np.allclose(state,expected)
    return match

def probabilityCheck():
    register = QuantumRegister(4)

def checkGateApplication(qubits,gate):
    for q in range(qubits):
        for i in range(qubits**2):
            register = QuantumRegister(qubits,state = i)
            register.applyGate(gate,q)
            print(register.state_)
    print()
    




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
    print("Expected state")
    print(expected)
    print()

    print("Found state")
    print(register.state_)
    print()

    print("Check if equal")
    print(checkExpected(register.state_,expected))
    print()

    print("Check Normalised")
    print(register.checkNormalised())
    print()

def testGateApplications():
    print("--------- TEST GATE APPLICATIONS ---------")

    initRegister = QuantumRegister(2)
    checkGateApplication(2,initRegister.hadamard)
    print("As we cannot reverse tensor product, we cannot qubit coefficients independantly")
    print("For correct application, the state coefficients should match a binary pattern")
    print("Two qubits should produce a pattern of the style")
    print("1100, 0011 for qubit 0 --- 1010, 0101 for qubit 1")


probabilityCheck()

twoBitEntanglement()

testGateApplications()