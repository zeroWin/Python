aTuple = (1,2,3,4,5)
print("(1)Sum of five num input: 1")
print("(2)Average of five num input: 2")
print("(X)Exit input: X")
choose = input("Please input:")
while choose != 'X':
	if choose == '1':
		sum = 0
		for i in aTuple:
			sum += i
		print("Sum of five num is %d" % sum)
	elif choose == '2':
		sum = 0
		for i in aTuple:
			sum += i
		print("Average of five num is %f" % (sum/5))		
	else:
		print("Input error")
		
	print("(1)Sum of five num input: 1")
	print("(2)Average of five num input: 2")
	print("(X)Exit input: X")
	choose = input("Please input:")
	
print("Program exit")
