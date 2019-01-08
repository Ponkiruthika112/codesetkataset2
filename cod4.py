#this is my code
n,k=map(int,input().split())
s=" "
j=" "
for i in range(n+1,k):
	if i%2!=0:
		s=s+str(i)+j
print(s.strip())
