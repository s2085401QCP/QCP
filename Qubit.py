class Qubit:
	def __init__(self,a,b):
			self.a_ = a
			self.b_ = b
			self.coefs_ = [[a],[b]] # could maybe use tuple

	# simple class to create a qubit, may be useful in future
	def update(self,a,b):
		"""
		Function that updates the coefficients of the qubits
		:param a: Float input value, a < 1
		:param b: Float input value, b < 1
		"""

		assert a < 1 and b < 1, f"a and/or b not normalised properly \n a = {a}, b = {b}"

		self.a_ = a
		self.b_ = b
		self.coefs_ = [[a],[b]]
		
	def checknorm(self):
		return self.a_**2 + self.b_**2 == 1
		




