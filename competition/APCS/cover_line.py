import itertools
times = int(input())
space = [0 for n in range(0,1000)]
for _ in range(times):
	start,end = map(int,input().split())
	for index in range(start,end):
		space[index] = 1

table = []
for k,v in itertools.groupby(space):
	# append every element(key) and len of same element in the list
	table.append([k,len(list(v))])

max_len = 0
for index in table:
	if index[0] == 1:
		# sum of every len , when key == 1
		max_len += index[1]

print(max_len)
