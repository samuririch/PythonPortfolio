#Magicians and Great Magicians - PCC 8-9, 8-10, 8-11
#------------------------------------------------------------------
#Function show_magicians accepts a list parameter and prints each item in the list.

magicians = ['david blaine', 'harry houdini', 'david copperfield']

def show_magicians(list):
	for item in list:
		print(item.title())

#Function make_great modifies the list by popping each list item to add 'the Great' suffix,
#and is appended to a new 'great_magicians' list. 

def make_great(list):
	great_magicians = [ ]
	while magicians:
		current_magician = magicians.pop()
		great_magician = current_magician + ' the Great!'
		great_magicians.append(great_magician)
	
	for great_magician in great_magicians:
			magicians.append(great_magician)
	return magicians

#We call the show_magicians function to show the original list items

print("\nOriginal magicians:")
show_magicians(magicians)

#We call the make_great function to accept a copy of the magicians list, which adds 'the Great' suffix to each item.
#We call the show_magicians function again to display the modified magicians list.

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
		


