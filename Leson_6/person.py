#10th asingment - person
person = {'first_name': 'marija', 
	'last_name': 'acimovic', 
	'age': 22, 
	'city': 'krupanj'
	}
print(person)
print('\n')
#Favorite numbers
person1 = {'predrag': 5,
	'marija': 19,
	'jelena': 25,
	'marko': 29
	}
for names in person1:
	#print(names.title())
	person1.keys()
	favorite_number = person1['predrag']
	print(f"{names.title()} favorite number is {favorite_number}.")
#Simplified way
for key, value in person1.items():
	print(key.title() + " favorite number is " + str(value))
print('\n')
#Glossary
words = {'string': 'A series of characters.',
	'comment': 'A note in program that Python interpreter ignores.',
	'loop': 'Work through a collection of items, one at a time.',
	'list': 'A collection of items in a particular order.',
	'dictionary': 'A collection of key-value pairs.',
	}
for key, value in words.items():
	print(key.title() + ':' + '\n' + value)
