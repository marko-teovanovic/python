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
print('\n')
#9th asingment - checking 
current_users = ['milos', 'dejan', 'djordje', 'stefan', 'aleksandar']
new_users = ['ivan', 'uros', 'djordje', 'stefan', 'nenad']

current_users_lower = {new_user.lower() for new_user in current_users}
for new_user in new_users:
	if new_user in current_users:
		print(f"Username {new_user.title()} is already taken, please enter new username.")
	else:
		print(f"Username {new_user.title()} is available")

