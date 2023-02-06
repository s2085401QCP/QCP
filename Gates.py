import Operators as op

def hadSparse(register,qbool):
	qs = register.qubits
	H = [[2**-.5,2**-.5],[2**-.5,-2**-.5]]
	I = [[1,0],[0,1]]

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
	
	H = [[2**-.5,2**-.5],[2**-.5,-2**-.5]]
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