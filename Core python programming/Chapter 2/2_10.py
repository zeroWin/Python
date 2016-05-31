# judge the num of user input if range is 1 to 100
num = input("input a num range 1 to 100:")
num = int(num)
while num <= 1 or num >= 100:
	print("error,num range must 1 to 100")
	num = input("input:")
	num = int(num)
print("Succeed")