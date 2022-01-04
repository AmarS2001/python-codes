lis= [0,0,1,1,0,1,1,1,0,1,1,1]
def func(lis):
	i=0
	j=0
	max_len=0
	count=0
	while( j < len(lis)):
		if count !=2:
			max_len=max(max_len,j-i+1)
			j=j+1
			if lis[j]==0:
				count=count+1
		else:
			while lis[i] :
				i=i+1
			i=i+1
			count = 1
	return max_len	

print(func(lis))
