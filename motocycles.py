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