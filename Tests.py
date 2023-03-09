import numpy as np
from Register import Register
from Qubit import Qubit
import register.Operators as op
import Gates as G

# tests to ensure program is working as intended
# check against notes to confirm proper operation
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
	register.updateS()
	print("START 011 dec 3")
	print(q1.coefs_,q2.coefs_,q3.coefs_)
	
	print(*register.state_s_)
	print("DONE")
	print()

	q1.update(0,1)
	
	register.updateS()
	print("START 111 dec 7")
	print(q1.coefs_,q2.coefs_,q3.coefs_)
	print(register.state_s_)
	print("DONE")
	print()


	print("SUPERPOS QUBIT1 2**-.5")
	q1.upd(2**-.5,2**-.5)
	print(q1.coefs_,q2.coefs_,q3.coefs_)
	register.updateS()
	print(register.state_s_)
	print()
	return register

def hadamardTest():
	q1 = Qubit(1,0)
	q2 = Qubit(0,1)
	q3 = Qubit(0,1)
	qubs = [q1,q2,q3]
	register = Register(qubs)
	register.updateS()
	register = G.hadamard(register,[1,1,1])
	register.updateS()

	print("START Hadamard Test ALL QUBITS")

	print(register.state_s_)
	print()
	#print(register.qubits[0])
	

	return register

def normalizedTest(register):
	print("START normalizedTest")
	print(register.state_s_)

	total = 0
	for i in range(len(register.state_s_)):
		total += round(register.state_s_[i][0]**2,6)
	print("REGISTER IS NORMALIZED:",total == 1)
	print()


def hadAdvanced():
	q1 = Qubit(0,1)
	q2 = Qubit(0,1)
	q3 = Qubit(0,1)
	qubs = [q1,q2,q3]
	register = Register(qubs)
	register.updateS()
	register = G.hadamard(register,[1,0,1])
	register.updateS()

	prod = op.tensorProd([[2**-.5,2**-.5],[2**-.5,-2**-.5]],[[1,0],[0,1]])
	prod2 = op.tensorProd(prod,[[2**-.5,2**-.5],[2**-.5,-2**-.5]])
		#op.printMat(prod)
	print("HADAMARD TEST H * I * H: FROM EXAMPLE")
	print(*prod2)
	print("MATCHING")

def stateTest():
	q1 = Qubit(0,1)
	q2 = Qubit(0,1)
	q3 = Qubit(0,1)
	qubs = [q1,q2,q3]
	register = Register(qubs)
	register.updateS()
	register = G.hadSparse(register,[1,1,1])
	register.updateE()
	print("STATE TEST - USES REGISTER AND NON EXPLICIT MATRIX")
	op.printMat(register.state_e_)
	


def CNOTtest():
	a = [[1,0]]
	b = [[1,0]]
	r = op.tensorProd(a,b)
	print(*op.matrixMulti(r,G.C))

	a = [[1,0]]
	b = [[0,1]]
	r = op.tensorProd(a,b)
	print(*op.matrixMulti(r,G.C))

	a = [[0,1]]
	b = [[1,0]]
	r = op.tensorProd(a,b)
	print(*op.matrixMulti(r,G.C))

	a = [[0,1]]
	b = [[0,1]]
	r = op.tensorProd(a,b)
	print(*op.matrixMulti(r,G.C))
	print(*G.C)
	


