#4 assingment
squares = [value **2 for value in range (1, 11)]
print(squares)
print('\n')
squares = [value **2 for value in range (1, 20)]
print(squares)
#One milion
milion = []
for value in range (0, 1000001):
	milion.append(value)
print(min(milion))
print(max(milion))
print(sum(milion))

odd_numbers = []
for value in range (1, 20, 2):
	odd_numbers.append(value)
	print(value)

odd_numbers1 = []
for value1 in range (3, 33, 3):
	odd_numbers1.append(value1)
	print(value1)

qube_numbers = []
for value2 in range (1, 11):
	qube_numbers.append(value2 **3)
	print(qube_numbers)
#Comperhension
qube_numbers = [value3 **3 for value3 in range (1,11)]
print(qube_numbers)