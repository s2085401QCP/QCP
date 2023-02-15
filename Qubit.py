class Qubit:
	def __init__(self,a,b):
			self.a_ = a
			self.b_ = b
			self.coefs_ = [[a],[b]] # could maybe use tuple

	# simple class to create a qubit, may be useful in future
	def upd(self,a,b):
		self.a_ = a
		self.b_ = b
		self.coefs_ = [[a],[b]]
		
	def checknorm(self):

		return self.a_**2 + self.b_**2 == 1
		




