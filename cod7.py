n=int(input())
i=0
arm=0
while n>0:
  r=n%10
  n=n//10
  arm=arm+(r*r*r)
if arm==n:
  print("yes")
else:
  print("no")
  
