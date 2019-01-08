#this is for prime no
n=int(input())
for i in range(2,n):
	if n%i==0:
		print("no")
		break
if i==n-1:
	print("yes")
	
