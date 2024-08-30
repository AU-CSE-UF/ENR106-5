no_of_elements = 0
start_element = 1
rows = int(input("Enter number of rows : "))
for i in range(0, rows):
	no_of_elements +=1
	for j in range(start_element, start_element + no_of_elements):
		print(j, end=' ')
	print()
	start_element += no_of_elements