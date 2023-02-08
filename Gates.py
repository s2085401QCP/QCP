import Operators as op

I = [[1,0],[0,1]]
C = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]

H = [[2**-.5,2**-.5],[2**-.5,-2**-.5]]

def CNOT(register,a,b):
	qa = register.qubits[a]
	qb = register.qubits[b]
	#print(qa)
	stateS = op.tensorProd(qa.coefs,qb.coefs)
	#op.printMat(stateS)

	stateE = op.matrixMulti(C,stateS)
	register.stateE = stateE
	return register



def hadSparse(register,qbool):
	qs = register.qubits
	prouduct = I
	if qbool[0]:
		product = H

	for i in range(1,len(qbool)):
		if qbool[i]:
			product = op.tensorProd(product,H)
		else:
			product = op.tensorProd(product,I)
	register.reg = product
	return register

def hadamard(register,qbool):
	qs = register.qubits

	for i in range(len(qbool)):
		if qbool[i]:

			res1 = op.matrixMulti(H,qs[i].coefs)
			a = qs[i].a
			b = qs[i].b
			ha = round((a+b)/(2**.5),6)
			hb = round((a-b)/(2**.5),6)
			res2 = [[ha],[hb]]
			if res1 == res2:
				register.qubits[i].upd(ha,hb)
			else:
				print("ERROR IN COMPARISON: HADAMARD GATE FAIL ON QUBIT- ",i)
				print(res1,"COMPARED TO",res2)
	return register

