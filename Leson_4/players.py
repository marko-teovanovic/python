players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4]) #Slice starts wtih item on index 1
print(players[2:]) #Slice from index 2 to end of a list
print(players[-3:]) #Print out last 3 items in a list
print('\n')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
