num1 = input("input the first num:")
num2 = input("input the second num:")
num3 = input("input the third num:")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if(num1 < num2 < num3):
	print("From small to big is:%d,%d,%d" % (num1,num2,num3))
elif(num1 < num3 < num2):
	print("From small to big is:%d,%d,%d" % (num1,num3,num2))
elif(num2 < num1 < num3):
	print("From small to big is:%d,%d,%d" % (num2,num1,num3))
elif(num2 < num3 < num1):
	print("From small to big is:%d,%d,%d" % (num2,num3,num1))
elif(num3 < num1 < num2):
	print("From small to big is:%d,%d,%d" % (num3,num1,num2))
elif(num3 < num2 < num1):
	print("From small to big is:%d,%d,%d" % (num3,num2,num1))

