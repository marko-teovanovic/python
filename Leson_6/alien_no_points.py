#Using get() to access values
alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])
point_value = alien_0.get('points', 'No point value assinged.')
print(point_value)