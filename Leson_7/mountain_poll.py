responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    #Store the response in dictionary
    responses[name] = response
    repeat = input("Would you like to let another person to repond? (yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll results ---")
for name, response in responses.items():
    print(f"{name} would you like to climp {response}.")