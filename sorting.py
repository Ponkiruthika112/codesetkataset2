# your code goes here
n=int(input())
l=list(map(str,input().split()))
l.sort(key=lambda item: (len(item), item))
s=""
for i in range(0,len(l)):
	s=s+l[i]+" "
print(s.strip())
#sort the list
