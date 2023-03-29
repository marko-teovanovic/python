sodas = ['Coca cola', 'pepsi', 'sprite', 'fanta']
for soda in sodas:
	print(f"{soda.title()} is a great refreshing drink.\n")
for soda1 in sodas:
	print(soda1.title())
print("I realy like soda's!")
print('\n') #Continuation of a 5th asingment
firend_sodas = sodas [:]
firend_sodas.append('dr. pepper')
print("My favourite soda's are:")
for my_soda in sodas:
	print(my_soda.title())
print("\nMy friend favourite soda's are:")
for firend_soda in firend_sodas:
	print(firend_soda.title())
