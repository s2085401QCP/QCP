import numpy as np
from Register import Register
from Qubit import Qubit
import Operators as op
def kronTest():
	g = np.array([[0],[1]])
	h = np.array([[1/np.sqrt(2)],[1j/np.sqrt(2)]])

	print(np.kron(g,h))
	print()
	print(np.kron(h,g))
	print()
	print(np.kron(g,np.kron(h,g)))

def threeSevenTest():

	q1 = Qubit(1,0)
	q2 = Qubit(0,1)
	q3 = Qubit(0,1)
	qubs = [q1,q2,q3]
	register = Register(qubs)
	register.update_basis()

	print("START 011 dec 3")
	print(q1.coefs,q2.coefs,q3.coefs)
	
	print(register.stated)
	print("DONE")
	print()

	q1.upd(0,1)
	
	register.update_basis()
	print("START 111 dec 7")
	print(q1.coefs,q2.coefs,q3.coefs)
	print(register.stated)
	print("DONE")
	print()


	print("SUPERPOS QUBIT1 2**-.5")
	q1.upd(2**-.5,2**-.5)
	print(q1.coefs,q2.coefs,q3.coefs)
	register.update_basis()
	print(register.stated)
	print()
	return register

def hadamardTest():
	q1 = Qubit(1,0)
	q2 = Qubit(0,1)
	q3 = Qubit(0,1)
	qubs = [q1,q2,q3]
	register = Register(qubs)
	register.update_basis()
	register.new_hadamard([1,1,1])
	register.update_basis()

	print("START Hadamard Test ALL QUBITS")

	print(register.stated)
	print()
	#print(register.qubits[0])
	

	return register

def normalizedTest(register):
	print("START normalizedTest")
	print(register.stated)
	total = 0
	for i in range(len(register.stated)):
		total += round(register.stated[i]**2,6)
	print("REGISTER IS NORMALIZED:",total == 1)
	print()


def hadAdvanced():
	q1 = Qubit(0,1)
	q2 = Qubit(0,1)
	q3 = Qubit(0,1)
	qubs = [q1,q2,q3]
	register = Register(qubs)
	register.update_basis()
	register.new_hadamard([1,0,1])
	register.update_basis()

	prod = op.tensorProd([[2**-.5,2**-.5],[2**-.5,-2**-.5]],[[1,0],[0,1]])
	prod2 = op.tensorProd(prod,[[2**-.5,2**-.5],[2**-.5,-2**-.5]])
	
	#op.printMat(prod)
	print("HADAMARD TEST H * I * H: FROM EXAMPLE")
	op.printMat(prod2)
	print("MATCHING")
