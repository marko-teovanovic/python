#9th asingment
#usernames = ['marija', 'predrag', 'jelena', 'admin', 'marko']
#9th asingment - empty list
usernames = []
for user in usernames:
	if user == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print(f"Hello {user.title()}, thank you for logging again.")
if usernames:
		for usernames in usernames:
			print("We need to find some users!")
else:
		print("We need to find some users!")

