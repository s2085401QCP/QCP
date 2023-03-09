from Qubit import Qubit
from register.QuantumRegister import *
from register.Operators import *

import register.deutsch as deutsch
import register.deutschJozsa as deutschJozsa
import register.grovers as grovers

def objArgTest(Obj,inputs):

	inputType = "FAILED"
	try:
		test = Obj(*inputs)
		print("SUCCESSFUL INPUT",type(inputs))
		inputType = type(inputs)
			
			
	except:
		#print("FAILED INPUT",type(inputs))
		test = inputs

	return inputType

def objSelectTypeTest(Obj,inputs):
	types = [True,"string",1,2.0]
	for i in range(len(input)): 
		try:
			test = Obj(*inputs)
			print("SUCCESSFUL INPUT",type(inputs))
			
		except:
			pass



def registerTest():
	print("INIT REGISTER TEST")

	print("SHOULD FAIL - STRING")
	stringInp = objArgTest(QuantumRegister,["THIS WILL FAIL"])
	print(stringInp)
	print()

	print("SHOULD FAIL - FLOAT")
	floatInp = objArgTest(QuantumRegister,[2.0])
	print(stringInp)
	print()

	print("SHOULD PASS - INT")
	intInp = objArgTest(QuantumRegister,[8])
	print(stringInp)
	print()

def dJTest():
	print("INIT DJ TEST")
	def dJInput(oracle,n_qubits):
		try:
			test = deutschJozsa.DeutschJozsa(oracle,n_qubits)
			print("SUCCESSFUL INPUT",type(oracle),type(n_qubits))
		except:
			print("FAILED INPUT",type(oracle),type(n_qubits))
			test = oracle,n_qubits
		return test

	print("SHOULD FAIL - NOT FUNC")
	dJInput("NOT A FUNC",8)
	print()


def groversTest():
	print("INIT GROVER TEST")
	def groverInput(oracle,inputList):
		try:
			test = grovers.Grovers(oracle,inputList)
			print("SUCCESSFUL INPUT",type(oracle),type(inputList))
		except:
			print("FAILED INPUT",type(oracle),type(inputList))
			test = oracle,inputList
		return test
	inputList = [0]*100
	print("SHOULD FAIL - NOT FUNC")
	groverInput("NOT A FUNC",inputList)
	print()




registerTest()
#dJTest()
#groversTest()
