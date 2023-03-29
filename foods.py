my_foods = ['pizza', 'burger', 'chicken nuggets']
friend_foods = my_foods[:]

print("My favourite foods are:")
print(my_foods)
print("\nMy friend favourite foods are:")
print(friend_foods)

my_foods.append('gyros')
friend_foods.append('salad')
print('\n')
#We prove that we actualy have 2 different lists
print(my_foods) 
print(friend_foods)