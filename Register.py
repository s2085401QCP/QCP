from Qubit import Qubit
import Operators as op
import numpy as np

class Register:	

	def __init__(self,qubits):
		self.qubits = qubits
		self.qs = len(qubits)
		self.n = 2**self.qs

		# creates qs dimensional matrix - binary states
		self.stateb = 0
		for i in range(self.qs):
			self.stateb = [self.stateb]*2
		#self.stateb = [np.asarray(self.stateb)] # converts to numpy array

		# creates n length array - decimal states
		self.stated = [0] * self.n

		self.coefs = []
		for i in self.qubits:
			self.coefs.append(i.coefs)
		#self. coefs = op.TransMatrix(self.coefs)
		self.statet = [[0]*self.n for _ in range(self.n)]
		
		
	def updateTensor(self):

		#print(self.coefs)
		product = op.tensorProd(self.coefs[0],self.coefs[1])
		#op.printMat(product)


		for i in range(2,len(self.coefs)):
			product = op.tensorProd(product,self.coefs[i])

		self.statet = product


	def new_hadamard(self,qbool):

		#print(qubit)
		#	Hadamard matrix
		H = [[2**-.5,2**-.5],[2**-.5,-2**-.5]]
		qs = self.qubits
		for i in range(len(qbool)):
			if qbool[i]:
				res1 = op.matrixMulti(H,qs[i].coefs)
				a = qs[i].a
				b = qs[i].b
				ha = round((a+b)/(2**.5),6)
				hb = round((a-b)/(2**.5),6)
				res2 = [[ha],[hb]]
				if res1 == res2:
					self.qubits[i].upd(ha,hb)
				else:
					print("ERROR IN COMPARISON: HADAMARD GATE FAIL ON QUBIT- ",i)
					print(res1,"COMPARED TO",res2)


	def hadamard(self,qbool): ## takes in an array of length qubits in boolean form eg [true,true,false] for hadamar qubit 1 and 2
	# only works for 1,0 inputs
		H = 2**-.5
		#had = [[H,H],[H,-H]]
		for i in range(len(qbool)):
			if qbool[i]:
				if self.qubits[i].a == 0:
					self.qubits[i].upd(H,H)

				else:
					self.qubits[i].upd(H,-H)





	def update_basis(self):
		# the state is a 3d matrix (binary shows coordinates) decomposed into linear array (decimal)
		# a product state is any state with a close to 1 value in any of the matrix positions
		
		# can probably do some fancy non hard code here

		for i in range(2):
			a = self.qubits[0].coefs[i][0]
			#print(a)

			for j in range(2):
				b = self.qubits[1].coefs[j][0]

				for k in range(2):
					c = self.qubits[2].coefs[k][0]

					val = a * b * c
					self.stateb[i][j][k] = val
					self.stated[i*4+j*2+k] = val


		#print(self.stateb)
		#print("in",self.stated)

				


		
