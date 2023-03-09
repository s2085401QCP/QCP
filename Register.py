from Qubit import Qubit
import register.Operators as op
import numpy as np
import math

class Register:	

	def __init__(self,qubits):
		# the register holds the qubit classes as an array
		# it stores the start and end states as tensor products
		# it also has a working matrix register which is where we can load gates into if needed
		self.qubits_ = qubits 
		self.n_qubits_ = len(qubits)
		self.n_states_ = 2**self.n_qubits_

		self.state_s_ = [[0] for _ in range(self.n_states_)]
		self.state_e_ = [[0] for _ in range(self.n_states_)]

		self.I = np.eye(2)
		self.C = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]


		# TODO: check value
		ident = np.eye(self.n_states_)
		self.reg_ = ident
		for i in range(1,self.n_qubits_):
			self.reg_ = op.tensorProd(self.reg_,ident)
		

	def updateS(self):
		"""
		Function which updates the state_s_ vector
		"""
		product = op.tensorProd(self.qubits_[0].coefs_,self.qubits_[1].coefs_)

		for i in range(2,self.n_qubits_):
			product = op.tensorProd(product,self.qubits_[i].coefs_)
		self.state_s_ = product

	def updateE(self):
		"""
		Function which updates the state_e_ vector 
		"""
		prod = op.matrixMulti(self.reg_,self.state_s_)
		self.state_e_= prod

	def CNOT(self, a, b):
		# this initialises the start state as the tensor product of the two qubit coeficients
		stateS = op.tensorProd(self.qubits_[a].coefs_, self.qubits_[b].coefs_)
	
		# creates the end state as the multiplication of the CNOT matrix and the start state
		# may need updated
		stateE = op.matrixMulti(C, stateS)
		self.state_e_ = stateE

	def hadamard(self, qbool):
		qs = self.qubits_

		for i in range(len(qbool)):
			if qbool[i]:

				res1 = op.matrixMulti(self.H, self.qubits_[i].coefs_)
				a = self.qubits_[i].a_
				b = self.qubits_[i].b_
				ha = round((a+b)/(math.sqrt(2)),6)
				hb = round((a-b)/(math.sqrt(2)),6)
				res2 = [[ha],[hb]]
				if res1 == res2:
					self.qubits_[i].update(ha, hb)
				else:
					raise Exception(f"ERROR IN COMPARISON: HADAMARD GATE FAIL ON QUBIT-{i} \n {res1} COMPARED TO {res2}")

	def hadSparse(self, qbool):

		# This does similar as above but with hadamard gates and identity matrices, 
		# both are needed as the tensor product doesnt always reduce to square ( in cases where the matrices arent square)
		# so we use the identity matrix to ensure all matrices are square
		product = self.I
		if qbool[0]:
			product = self.H

		for i in range(1,len(qbool)):
			if qbool[i]:
				product = op.tensorProd(product, self.H)
			else:
				product = op.tensorProd(product, self.I)
		self.reg_ = product

	
