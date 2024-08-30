rows = int(input("Enter number of rows : "))
print("* " * rows)
for i in range(0, rows - 2):
	for j in range(0, rows):
		if j == 0 or j == rows - 1:
			print("*", end=" ")
		else:
			print(" ", end=" ")
	print()
print("* " * rows)