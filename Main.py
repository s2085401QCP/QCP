from QuantumRegister import *
from qubit import Qubit
import operators as op

import deutsch
import deutschJozsa
import grovers



def deutschMain():
	# This function is used to run the deutsch algorithm, it uses examples for both balanced and constant functions
	# The deutsch algorithm is used to evaluate a black box algorithm using a basic quantum circuit, for all constant 
	# functions our implementation will produce a 0 and for all balanced, a 1

	def balanced(x):
		return x % 2
	def constant(x):
		return 0

	deutschBalanced = deutsch.Deutsch(balanced)
	deutschBalanced.deutschAlgorithm()

	deutschConstant = deutsch.Deutsch(constant)
	deutschConstant.deutschAlgorithm()

def dJMain():
	# This function is used to run the deutsch algorithm, it uses examples for both balanced and constant functions
	# The deutsch algorithm is used to evaluate a black box algorithm using a basic quantum circuit, for all constant 
	# functions our implementation will produce a 0 and for all balanced, a 1

	def balanced(x):
		return x % 2
	def constant(x):
		return 0

	nqubits = 8

	dJBalanced = deutschJozsa.DeutschJozsa(balanced,nqubits)
	dJBalanced.deutschJozsaAlgorithm()

	dJConstant = deutschJozsa.DeutschJozsa(balanced,nqubits)
	dJConstant.deutschJozsaAlgorithm()

def groverMain():

	# grovers algorithm is an algorithm to sort a list using an oracle
	# our implementation selects the appropriate qubit number number from the list size
	# It can operate efficiently in under two seconds up to 21 qubits in size

	groverList = [0]*100
	target = 40

	def groverOracle(x):
	
		bit = 0
		if x == target:
			bit = 1
		return bit

	groverExample = grovers.Grovers(groverOracle,groverList)
	groverExample.groversAlgorithm()

def main():
	deutschMain()
	dJMain()
	groverMain()



main()
