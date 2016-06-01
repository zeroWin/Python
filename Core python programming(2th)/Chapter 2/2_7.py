str = input("input str:")
print("use while output")
i = 0
while i < len(str):
	print(str[i],end = " ")
	i += 1
print("")
print("use for output")
for s in str:
	print(s,end = " ")