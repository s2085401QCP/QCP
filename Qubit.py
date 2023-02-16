import numpy as np
import math
import Operators as op

class Qubit:
	def __init__(self,a,b):
			self.a_ = a
			self.b_ = b
			self.state_ = np.array([self.a_, self.b_])

	# simple class to create a qubit, may be useful in future
	def update(self,a,b):
		"""
		Function that updates the coefficients of the qubits
		:param a: Float input value
		:param b: Float input value
		"""
		self.state_[0] = a
		self.state_[1] = b
		
	def checknorm(self):
		return (self.a_**2 + self.b_**2 == 1)

	def normalize(self):
		
		self.state_ = self.state_  / np.linalg.norm(self.state_)

	def equalSuperposition(self):
		self.state_[0] = 1
		self.state_[1] = 1
		self.state_ = self.state_ / math.sqrt(2)
		
	def measure(self):
		prob = abs(self.state_)**2
		index = np.random.choice([0, 1], p = prob)
		if index == 0:
			self.state_[0] = 1
			self.state_[1] = 0
		elif index == 1:
			self.state_[0] = 0
			self.state_[1] = 1

	def hadamard(self):
		H = 1/math.sqrt(2) * np.array([1, 1], [1, -1])
		self.state_ = op.matrixMultiply(H, self.state_)








