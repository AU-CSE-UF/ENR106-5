sum = 0
num = 0
while 1:
	num = int(input("Enter a number : "))
	if num < 0:
		break
	else:
		sum += num

print("sum =",sum)