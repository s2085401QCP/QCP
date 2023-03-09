from QuantumRegister import *
from source.Qubit import Qubit
from source.Operators import *

from deutsch import *
from deutschJozsa import *
from grovers import *

def balanced(register):
	def oracle(a):
		return a % 2
	for i in range(register.n_states_):
		register.state_[i] *= (-1) ** oracle(i)
	return register.state_

def constant(register):
	def oracle(a):
		return 0
	for i in range(register.n_states_):
		register.state_[i] *= (-1) ** oracle(i)
	return register.state_


def deutschMain():
	# This function is used to run the deutsch algorithm, it uses examples for both balanced and constant functions
	# The deutsch algorithm is used to evaluate a black box algorithm using a basic quantum circuit, for all constant 
	# functions our implementation will produce a 0 and for all balanced, a 1

	register = QuantumRegister(2)

	deutschBalanced = Deutsch(balanced,register)
	deutschBalanced.deutschAlgorithm()

	deutschConstant = Deutsch(constant,register)
	deutschConstant.deutschAlgorithm()
	print("DONE DEUTSCH")

def dJMain(n_qubits):
	# This function is used to run the deutsch algorithm, it uses examples for both balanced and constant functions
	# The deutsch algorithm is used to evaluate a black box algorithm using a basic quantum circuit, for all constant 
	# functions our implementation will produce a 0 and for all balanced, a 1

	register = QuantumRegister(n_qubits)

	dJBalanced = DeutschJozsa(balanced,register)
	dJBalanced.deutschJozsaAlgorithm()

	dJConstant = DeutschJozsa(constant,register)
	dJConstant.deutschJozsaAlgorithm()
	print("DONE DJ")

def groverMain(n_qubits,list_Len):

	register = QuantumRegister(n_qubits)

	# grovers algorithm is an algorithm to sort a list using an oracle
	# our implementation selects the appropriate qubit number number from the list size
	# It can operate efficiently in under two seconds up to 21 qubits in size

	groverList = [0]*list_Len
	target = 40

	def groverOracle(register):

		def oracle(a):
			
			bit = 0
			if a == target:
				bit = 1
			return bit
		
		for i in range(register.n_states_):
			register.state_[i] *= (-1) ** oracle(i)
		return register.state_

		n_qubits = x.n_qubits_
		oracleRegister = QuantumRegister(n_qubits)
		oracleState =  np.array([0]*len(x.state_))
		oracleState[target] = 1
		assert len(oracleState) == len(oracleRegister.state_)
		oracleRegister.state_ = oracleState
		return oracleState

	groverExample = Grovers(groverOracle,groverList,register)
	groverExample.groversAlgorithm()
	print("DONE GROVERS")

def main():
	deutschMain()
	dJMain(8)
	groverMain(12,100)



main()
