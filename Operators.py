import numpy as np
# this file contains some of the matrix operators we are not allowed to use from packages
# they have much room for improvement with numpy arrays

# change name and can be optimised by just unpacking the list 
def printMatrix(a):
	print(*a) 

# change name to something more clear 
def transposeMatrix(a):
	# change variable name 
	a_T = [[0]*len(a) for _ in range(len(a[0]))]
	for i in range(len(a)):
		for j in range(len(a[i])):
			a_T[j][i] = a[i][j]
	return a_T
	# matrix T


# change name on matrix 
def matrixMulti(a,b): 
	dimension = len(a)

	# use assert for error control 
	assert len(a[0]) == len(b), "Matrices of different dimensions cannot be multiplied"
	n = len(b)
	p = len(b[0])
	product = [[0]*p for _ in range(m)]
	for i in range(dimension):
		for j in range(p):
			c = 0
			for k in range(n):
				c += a[i][k]*b[k][j]
			# could change rounding magnitude to a class member, so precision can be changed simply 
			product[i][j] = round(c,6) ###### IMPORTANT ROUNDING WITHIN FUNCTION

	return product

def tensorProd(a, b):
	"""
	Compute the tensor product of two matrices 
	:param a: input matrix a
	:param b: input matrix b
	:return: tensor product of the two matrices
	"""
    
	assert type(a) is np.ndarray and type(b) is np.ndarray, "Input matrices were not numpy arrays" 

	a_dims = a.shape
	b_dims = b.shape

	# calculates the dimensions of final product by concantinating the tuples
	result_dims = a_dims + b_dims

	a_flat = a.flatten()
	b_flat = b.flatten()

	# adds a new dimension to af, then spans along the new axis multiplying by bf
	product = a_flat[:, np.newaxis] * b_flat 
	
	# returns the tensor product in the calculated shape 
	return product.reshape(result_dims)
