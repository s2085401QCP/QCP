from register.QuantumRegister import *
from register.Operators import *

import register.deutsch as deutsch
import register.deutschJozsa as deutschJozsa
import register.grovers as grovers


def exampleOracle(register):

	def oracle(a):
		return 0
	
	for i in range(register.n_states_):
		register.state_[i] *= (-1) ** oracle(i)

	return register.state_


def objArgTest(Obj,inputs):

	inputType = "FAILED"
	try:
		test = Obj(*inputs)
		#print("SUCCESSFUL INPUT")
		inputType = "PASSED"
			
			
	except:
		#	print("FAILED INPUT",type(inputs))
		test = inputs
	for i in inputs:
		print(type(i), end="   ")	
	print()

	#print(inputType)
	return inputType

def objSelectTypeTest(Obj,inputs):
	types = [True,"string",1,2.0]
	for i in range(len(input)): 
		try:
			test = Obj(*inputs)
			print("SUCCESSFUL INPUT")
			
			
		except:
			print("FAILED INPUT")
	print(inputs)
	



def registerTest():
	print("--------- INIT REGISTER TEST ---------")

	print("SHOULD FAIL - STRING")
	stringInp = objArgTest(QuantumRegister,["THIS WILL FAIL"])
	print(stringInp)
	print()

	print("SHOULD FAIL - FLOAT")
	floatInp = objArgTest(QuantumRegister,[2.0])
	print(floatInp)
	print()

	print("SHOULD PASS - INT")
	intInp = objArgTest(QuantumRegister,[8])
	print(intInp)
	print()

def dJTest():
	dJRegister = QuantumRegister(8)
	print("--------- INIT DJ TEST ---------")

	print("SHOULD FAIL - NOT FUNC")
	intInp = objArgTest(deutschJozsa.DeutschJozsa,[1,1])
	print(intInp)
	print()

	print("SHOULD PASS - FUNC AND REGISTER")
	funcInp = objArgTest(deutschJozsa.DeutschJozsa,[exampleOracle,dJRegister])
	print(funcInp)
	print()


def groversTest():
	
	qubits = 16
	n_states = int((qubits/2)**2)
	groverRegister = QuantumRegister(qubits)
	inputList = np.zeros(n_states)

	print("--------- INIT GROVER TEST ---------")

	print("SHOULD FAIL - NOT FUNC")
	stringInp = objArgTest(grovers.Grovers,["NOT A FUNC",1,1])
	print(stringInp)
	print()

	print("SHOULD PASS - FUNC LIST REGISTeR")
	soundInp = objArgTest(grovers.Grovers,[exampleOracle,inputList,groverRegister])
	print(soundInp)
	print()


if __name__ == "__main__":
	
	registerTest()
	
	dJTest()
	
	groversTest()
