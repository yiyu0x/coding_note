n = int(input())
for i in range(1000,99999):
	if i*n > 98765:
		break
	f = str(i).zfill(5)
	old_len = len(list(str(i*n) + f))
	new_len = len(list(set(str(i*n) + f)))
	if old_len==new_len:
		print(str(i*n),'/',f,'= ',n)
