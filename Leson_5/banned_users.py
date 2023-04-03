#Checking if value is not in a list
banned_users = ['marko', 'marija', 'predrag', 'jelena']
user = 'dragan'
if user not in banned_users:
	print(f"{user.title()}, you can post a response.")