#Similar objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
print('\n')
#Looping through key-value in a dictionary
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")
print('\n')
#Looping through keys in a dictionary
friends = ['phil', 'sarah']
for name in favorite_languages.keys(): #favorite_languages.keys() is same as favorite_languages
	#print(name.title())
	print(f"Hi {name.title()}")
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys():
	print("\nErin, pleas take our poll!")
print('\n')
#Looping through key is particular order
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for takin the poll.")
print('\n')
#Looping through all values in a dictionary
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
print("The following languages have been mentoined:")
#for language in favorite_languages.values():
#Using set, set is a collection in wich each element must be unique
for language in set(favorite_languages.values()):`
	pass
	print(language.title())

