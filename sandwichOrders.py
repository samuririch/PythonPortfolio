#Python Crash Course 7-8 & 7-9 Exercises

sandwich_orders = ['Reuben','BLT','Pastrami','Cuban','PB&J', 'Pastrami','Chicken Salad','Pastrami','Sasuage, Egg & Cheese']
finished_sandwiches = []

print("We are out of Pastrami!")

while 'Pastrami' in sandwich_orders:
	sandwich_orders.remove('Pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	
	print("The " + current_sandwich + " has been made.")
	finished_sandwiches.append(current_sandwich)
	
print("\nThe following sandwiches have been made")
for sandwich in finished_sandwiches:
	print(sandwich)
	
