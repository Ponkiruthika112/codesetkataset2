# your code goes here
s=input()
k=""
for i in s:
	if i.isupper():
		k=k+i.lower()
	else:
		k=k+i.upper()
print(k)
#for covert the letters
