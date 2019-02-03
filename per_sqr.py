# your code goes here
def perfect(n):
	h=math.sqrt(n)
	if int(h)*int(h)==n:
		return 1
import math
h,k=map(int,input().split())
c=0
for i in range(h+1,k):
	f=perfect(i)
	if f==1:
		c=c+1
print(c)
#to find a perfect square
