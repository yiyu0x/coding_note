# y <= 2k
k = int(input())
for y in range(1,2*k+1) :
	for x in range(y,99999) :
		if round(1/k,5) == round(1/x+1/y,5) :
			print('1/',k,' = ','1/',x,' + 1/',y,sep='')
			break