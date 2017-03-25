from copy import deepcopy

def rotate_with_extra_memory(matrix):
	newmatrix=deepcopy(matrix)
	n=len(matrix)
	for i in range(n):
		for j in range(n):
			newmatrix[j][n-1-i]=matrix[i][j]
	return newmatrix 

def rotate_inplace(matrix):
	layers = len(matrix)//2
	length = len(matrix)-1
	for layer in range(layers): #for each layer
		for i in range(layer, length - layer): # loop through the elements we need to change at each layer
			temp = matrix[layer][i] #save the top element,
			#Left -> Top
			matrix[layer][i] = matrix[length - i][layer]
			#Bottom -> left
			matrix[length - i][layer] = matrix[length - layer][length - i]
			#Right -> bottom
			matrix[length - layer][length - i] = matrix[i][length - layer]
			#Top -> Right
			matrix[i][length - layer] = temp

def printmat(matrix):
	for row in matrix:
		print(row)

matrix=[['1','2','3','4','5'],['6','7','8','9','10'],['11','12','13','14','15']]
print("original")
printmat(matrix)
print ('rotation')
newmat=rotate_with_extra_memory(matrix)
printmat(newmat)

print ("In Place rotation")
rotate_inplace(matrix)
printmat(matrix)