import numpy as np
import math
from source.Operators import *

class Qubit:
	def __init__(self,a,b):
			self.state_ = np.array([a, b])

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
		return (self.state_[0]**2 + self.state_[1]**2 == 1)

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

	# TODO: define more gates which only affect one qubit, check if anything else is required???








