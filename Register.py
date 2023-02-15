from Qubit import Qubit
import Operators as op
import numpy as np

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



	
