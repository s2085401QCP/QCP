import numpy as np

def transposeMatrix(a):
	"""
	Function to take the transpose of a matrix 
	:param a: input matrix a, of size (m, n)
	:return: Transpose of matrix a, of size (n, m)
	"""
	assert type(a) is np.ndarray, "Input matrix is not a numpy array"
	a_T = np.zeros((a.shape[1], a.shape[0]))
	for i in range(a.shape[0]):
		for j in range(a.shape[1]):
			a_T[j][i] = a[i][j]
	return a_T

def matrixMultiply(a, b): 
	"""
	Function to multiply two matrices together 
	:param a: input matrix a of size (m, n)
	:param b: input matrix b of size (p, q)
	:return: product of the two matrices, of size (m, q) 
	"""
	assert a.shape[1] == b.shape[0], "Matrices are of incompatible dimensions for multiplication"

	result = np.zeros((a.shape[0], b.shape[1])) 

	for i in range(a.shape[0]):
		for j in range(b.shape[1]):
			for k in range(a.shape[1]):
				result[i][j] += a[i][k] * b[k][j]

	return result

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
