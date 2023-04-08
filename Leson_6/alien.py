#Simple dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#Accessing values in a dictionary
new_points = alien_0['points'] #<= pulls value associated with the key 'points'
print(f"You just earned {new_points} points!")
print('\n')
#Adding new key-value pairs in a dictionary
alien_1 = {'color': 'green', 'points': 5}
print(alien_1)
alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_1)
print('\n')
#Empty dictionary
alien_2 = {}
alien_2['color'] = 'green'
alien_2['points'] = '5'
print(alien_2)
#Modifying values 
alien_3 = {'color': 'green'}
print(f"The alien is {alien_3['color']}.")
alien_3['color'] = 'yellow' #<=== associate different color to alien
print(f"The alien is now {alien_3['color']}.")
#Moving alien
alien_moving = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_moving['x_position']}")
#Move the alien to the righ.
#Determine how far to move the alien based on its curren speed.
if  alien_moving['speed'] == 'slow':
	x_increment = 1
elif alien_moving['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_moving['x_position'] = alien_moving['x_position'] + x_increment
print(f"New position: {alien_moving['x_position']}.")
