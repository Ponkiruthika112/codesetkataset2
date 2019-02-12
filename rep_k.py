n,k=map(int,input().split())
a=list(map(int,input().split()))
l=list(set(a))
s=""
for i in range(0,len(l)):
    if a.count(l[i])==k:
        s=s+str(l[i])+" "
print(s.strip())
#repeat k times
