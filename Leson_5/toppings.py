#If statements with lists, checking for special item in a list
requested_topping = ['mushrooms', 'extra cheese', 'green peppers']
for requested_topping in requested_topping:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")
