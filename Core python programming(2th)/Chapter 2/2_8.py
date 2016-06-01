aList = [1,2,3,4,5]
sum = 0
for i in aList:
	sum += i;
print("Sum of the list is %d" % sum)

i = 0
sum = 0
while i < len(aList):
	sum += aList[i]
	i += 1
print("Sum of the list is %d" % sum)

i = 0
sum = 0
while i < 5:
	i += 1
	numInput = input("input the %d num:" % i)
	sum += int(numInput)
print("Sum of input num is %d" % sum)

i = 0
sum = 0
for i in range(1,6):
	numInput = input("input the %d num:" % i)
	sum += int(numInput)
print("Sum of input num is %d" % sum)
	