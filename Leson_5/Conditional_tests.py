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
#Numerical comparison
age = 17
if age >= 18:
	print("\nYou can drive a car!")
else:
	print("\nYou are not old enough!")
football_players = ['Ronaldinho', 'Kaka', 'Vidic', 'Rooney']
player = 'Van Persie' #If you change value to some from a list you will get a else print.
if player not in football_players:
	print(f"\n{player.title()} in not in a list.")
else:
	print("Player is already in a list!")


