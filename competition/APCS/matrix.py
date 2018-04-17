'''
106/4/17
1050305APCSImplementation.pdf
question 2
author: yiyu0x
'''
R,C,M = map(int,(input().split()))

matrix = []
for i in range(R):
	matrix.append(list(map(int,(input().split()))))

mod = list(map(int,(input().split())))

for i in mod:
	# 0 is rotate
	if i == 0:
		matrix[:] = map(list,zip(*matrix[::-1]))
	elif i == 1:
	# 1 is flip
		matrix[:] = matrix[::-1]

print(len(matrix),len(matrix[0]))
for row in matrix:
	for column in row:
		print(column,end=" ")
	print()