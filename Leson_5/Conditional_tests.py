#Equality
car = 'bmw'
print("Is car == 'bmw'? I predict TRUE.")
print(car == 'bmw')
print("\nIs car == 'audi'? I predict FALSE.")
print(car == 'audi')
#Case sensitive
car = 'Ford'
print("\nIs car == 'ford'? I predict FALSE.")
print(car == 'ford')
#If case doesn't matter, you can convert var to lowercase and then check:
car = 'Subaru'
print("\nIs car == 'subaru'? I predict FALSE.")
print(car == 'subaru')
print("\nIs car == 'subaru'? I predict TRUE.")
print(car.lower() == 'subaru') #.lower() converst var to lowercase
#Checking fo Inequality
requested_song = 'bohemian rhapsody'
if requested_song != 'highway to hell':
	print("\nPlay highway to hell!")
