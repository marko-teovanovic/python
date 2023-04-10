message = input("Tell me something, and i will repeat it back to you:")
print(message)
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print(f"\nHello, {name}")
age = input("How old are you?")
age = int(age)
print(age)
print(age >= 18)
height = input("How tall are you?")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")