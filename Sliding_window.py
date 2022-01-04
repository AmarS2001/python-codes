def func(lis):
	i=0
	max_len=0
	count=0
	for j in range(0,len(lis)):
		if lis[j]==0:
			count=count+1
		if count==2:
			while lis[i]:
				i=i+1
			i=i+1
			count=1
			
		max_len=max(max_len, j-i+1)
	return max_len	
print(func(lis))

## returns maximum length of the sequence of ones.
