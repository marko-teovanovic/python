#If - elif - else:
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cost is $40.")
print('\n')
#Simplification of code
age = 13
if age < 3:
	price = 0
elif age < 18:
	price = 25
else:
	price = 45
print(f"Your admission cost is ${price}.")