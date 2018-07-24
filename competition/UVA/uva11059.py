while True:
	arr = list(map(int,input().split()))
	result_max = 0
	for i in range(len(arr)):
		tmp = 1
		for j in range(i,len(arr)):
			tmp = tmp * arr[j]
			if tmp>result_max :
				result_max = tmp
	print(result_max)