#Creating a list with 'append'
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#Inserting elements in list. [number] - determine where in list we want to add element
motorcycles.insert(0, 'ducati')
motorcycles.insert(2, 'harley davidson')
print(motorcycles)
#Removing elements from list. [number] - determines witch element we want to remove
del motorcycles[0]
print(motorcycles)
#Removing elements from list with pop() method.
motorcycles = ['honda', 'suzuki', 'harley davidson']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#Example of using a pop() method.
motorcycles = ['honda', 'suzuki', 'harley davidson', 'ducati']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was {last_owned.title()}.")
#Using pop() to remove an item from any position in a list. pop(number) - index of a item in list we want to remove.
first_owned = motorcycles.pop(1)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
#Removing items from a list by value.
motorcycles = ['honda', 'suzuki', 'harley davidson', 'ducati']
print(motorcycles)
motorcycles.remove('harley davidson')
print(motorcycles)
#Reusing item after using a remove() method.
motorcycles = ['honda', 'suzuki', 'harley davidson', 'ducati']
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
print('----------------------------------------------------------------------------')
#Avoiding index errors when working with lists
motorcycles = ['honda', 'suzuki', 'harley davidson', 'ducati']
#print(motorcycles[4]) - IndexError: list index out of range
print(motorcycles[-1]) #-1 always return last item in a list
