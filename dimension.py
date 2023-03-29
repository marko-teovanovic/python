dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 If we try to change value of item in tuple
#TypeError: 'tuple' object does not support item assignment (we recieve this message)
print('\n')
for dimension in dimensions:
	print(dimension)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)