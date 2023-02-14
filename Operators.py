# this file contains some of the matrix operators we are not allowed to use from packages
# they have much room for improvement with numpy arrays

# change name 
def printMat(a):
	for i in range(len(a)):
		print(a[i])
	print()


def TransMatrix(a):
	Ta = [[0]*len(a) for _ in range(len(a[0]))]
	for i in range(len(a)):
		for j in range(len(a[i])):
			Ta[j][i] = a[i][j]
	return Ta
	# matrix T



def matrixMulti(a,b):
	m = len(a)

	if (len(a[0]) == len(b)):
		n = len(b)
		p = len(b[0])
		product = [[0]*p for _ in range(m)]
		for i in range(m):
			for j in range(p):
				c = 0
				for k in range(n):
					c += a[i][k]*b[k][j]
				product[i][j] = round(c,6) ###### IMPORTANT ROUNDING WITHIN FUNCTION
	else:
		print("ERROR: Matrix sizes not aligned,  cannot multiply")
		return []

	return product

def tensorProd(a,b):
	
	rwid =len(a[0])*len(b[0])
	rheight = len(a)*len(b)

	tensa = [[0]*rwid for _ in range(rheight)]
	tensb = [[0]*rwid for _ in range(rheight)]

	product = [[0]*rwid for _ in range(rheight)]


	#converts a to the scale of the tensor
	for i in range(len(a)):
		for j in range(len(a[0])):
			fack = i * len(b)
			facl = j * len(b[0])
			for k in range(len(b)):
				for l in range(len(b[0])):
				
					tensa[k+fack][l+facl] = a[i][j]


	#converts b to the scale of the tensor
	#print(len(b[0]),len(a[0]))
	for k in range(len(b)):
		for l in range(len(b[0])):
			for i in range(len(a)):
				for j in range(len(a[0])):
					fack = i * len(b)
					facl = j * len(b[0])
			
					tensb[k+fack][l+facl] = b[k][l]

	#multiplies the scaled arrays to find the tensor product
	for i in range(len(product)):
		for j in range(len(product[i])):
			product[i][j] = round(tensa[i][j]*tensb[i][j],6)

	return product
