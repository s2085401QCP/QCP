class Qubit:
	def __init__(self,a,b):
			self.a = a
			self.b = b
			self.coefs = [[a],[b]] # could maybe use tuple

	# do not use alta or altb except in specific circumstances as does not account for negative state coefficients

	def upd(self,a,b):
		self.a = a
		self.b = b
		self.coefs = [[a],[b]]

	def alta(self,k):
		self.a = k
		self.b = (1-self.a**2)**.5
		self.coefs[0] = self.a
		self.coefs[1] = self.b

	def altb(self,k):
		self.b  = k
		self.a = (1-self.b**2)**.5
		self.coefs[0] = self.a
		self.coefs[1] = self.b
		

	def checknorm(self):

		return self.a**2 + self.b**2 == 1
		




