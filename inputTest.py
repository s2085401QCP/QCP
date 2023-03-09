from QuantumRegister import *
from source.Qubit import Qubit
from source.Operators import Operators as op

import deutsch
import deutschJozsa
import grovers

def registerTest():
	print("INIT REGISTER TEST")
	def registerInput(n_qubits):
		try:
			test = QuantumRegister(n_qubits)
			print("SUCCESSFUL INPUT",type(n_qubits))
		except:
			print("FAILED INPUT",type(n_qubits))
			test = n_qubits
		return test

	print("SHOULD FAIL - STRING")
	stringInp = registerInput("THIS WILL FAIL")
	print()
	print("SHOULD FAIL - FLOAT")
	floatInp = registerInput(2.0)
	print()
	print("SHOULD PASS - INT")
	intInp = registerInput(8)
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
dJTest()
groversTest()
