class Qubit:
	def __init__(self,a,b):
			self.a = a
			self.b = b
			self.coefs = [[a],[b]] # could maybe use tuple

	# simple class to create a qubit, may be useful in future
	def upd(self,a,b):
		self.a = a
		self.b = b
		self.coefs = [[a],[b]]
		
	def checknorm(self):

		return self.a**2 + self.b**2 == 1
		




