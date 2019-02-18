n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(0,len(l)):
    s.append(0^l[i])
print(max(s))
#max_xor
