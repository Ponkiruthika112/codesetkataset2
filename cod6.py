#this is my code for prime
n,k=map(int,input().split())
for i in range(n+1,k):
	for j in range(2,i):
		if i%j==0:
			break
	if j==i-1:
		s=s+str(i)+" "
	
print(s.strip())
	
