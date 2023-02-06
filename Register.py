from Qubit import Qubit
import Operators as op
import numpy as np

class Register:	

	def __init__(self,qubits):
		self.qubits = qubits
		self.qs = len(qubits)
		self.n = 2**self.qs

		self.stateS = [[0] for _ in range(self.n)]
		self.stateE = [[0] for _ in range(self.n)]

		ident = [[1,0],[0,1]]
		self.reg = ident

		for i in range(1,self.qs):
			self.reg = op.tensorProd(self.reg,ident)
		

	def updateS(self):
		product = op.tensorProd(self.qubits[0].coefs,self.qubits[1].coefs)

		for i in range(2,self.qs):
			product = op.tensorProd(product,self.qubits[i].coefs)
		#rint(product)
		self.stateS = product

	def updateE(self):
		prod = op.matrixMulti(self.reg,self.stateS)
		self.stateE = prod



	
