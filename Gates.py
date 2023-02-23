import Operators as op
import math

# identity matrix, hadamard gate and cnot gate

I = [[1,0],[0,1]]
C = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]

H = [[2**-.5,2**-.5],[2**-.5,-2**-.5]]

def CNOT(register,a,b):
	qa = register.qubits_[a]
	qb = register.qubits_[b]

	# this initialises the start state as the tensor product of the two qubit coeficients
	stateS = op.tensorProd(qa.coefs_,qb.coefs_)
	
	# creates the end state as the multiplication of the CNOT matrix and the start state
	# may need updated
	stateE = op.matrixMulti(C,stateS)
	register.state_e_ = stateE

	# returns the register with its updated states
	return register



def hadSparse(register,qbool):

	# This does similar as above but with hadamard gates and identity matrices, 
	# both are needed as the tensor product doesnt always reduce to square ( in cases where the matrices arent square)
	# so we use the identity matrix to ensure all matrices are square
	qs = register.qubits_
	product = I
	if qbool[0]:
		product = H

	for i in range(1,len(qbool)):
		if qbool[i]:
			product = op.tensorProd(product,H)
		else:
			product = op.tensorProd(product,I)
	register.reg_ = product
	return register

def hadamard(register,qbool):
	qs = register.qubits_

	for i in range(len(qbool)):
		if qbool[i]:

			res1 = op.matrixMulti(H,qs[i].coefs_)
			a = qs[i].a_
			b = qs[i].b_
			ha = round((a+b)/(math.sqrt(2)),6)
			hb = round((a-b)/(math.sqrt(2)),6)
			res2 = [[ha],[hb]]
			if res1 == res2:
				register.qubits_[i].update(ha,hb)
			else:
				raise Exception(f"ERROR IN COMPARISON: HADAMARD GATE FAIL ON QUBIT- {i} \n {res1} COMPARED TO {res2}")
	return register

