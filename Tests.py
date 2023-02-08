import numpy as np
from Register import Register
from Qubit import Qubit
import Operators as op
import Gates as G
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
	print(q1.coefs,q2.coefs,q3.coefs)
	
	op.printMat(register.stateS)
	print("DONE")
	print()

	q1.upd(0,1)
	
	register.updateS()
	print("START 111 dec 7")
	print(q1.coefs,q2.coefs,q3.coefs)
	op.printMat(register.stateS)
	print("DONE")
	print()


	print("SUPERPOS QUBIT1 2**-.5")
	q1.upd(2**-.5,2**-.5)
	print(q1.coefs,q2.coefs,q3.coefs)
	register.updateS()
	op.printMat(register.stateS)
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

	op.printMat(register.stateS)
	print()
	#print(register.qubits[0])
	

	return register

def normalizedTest(register):
	print("START normalizedTest")
	print(register.stateS)

	total = 0
	for i in range(len(register.stateS)):
		total += round(register.stateS[i][0]**2,6)
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
	op.printMat(prod2)
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
	op.printMat(register.stateE)
	


def CNOTtest():
	a = [[1,0]]
	b = [[1,0]]
	r = op.tensorProd(a,b)
	op.printMat(op.matrixMulti(r,G.C))

	a = [[1,0]]
	b = [[0,1]]
	r = op.tensorProd(a,b)
	op.printMat(op.matrixMulti(r,G.C))

	a = [[0,1]]
	b = [[1,0]]
	r = op.tensorProd(a,b)
	op.printMat(op.matrixMulti(r,G.C))

	a = [[0,1]]
	b = [[0,1]]
	r = op.tensorProd(a,b)
	op.printMat(op.matrixMulti(r,G.C))
	op.printMat(G.C)
	


