magicians = ['david', 'alice', 'carolina']
for magician in magicians:
	print(magician)
	print(f"{magician.title()}, that was a great trick.")
	print(f"I can't wait to see your next trick, {magician.title()}!\n")
	print("Thank you, everyone. That was a great magic show!")

#What happens if you forget to indent the line afte for statment
#magicians = ['david', 'carolina', 'alice']
#for magician in magicians:
#print(magician) ---> #IndentationError: expected an indented block after 'for' statement on line 10
