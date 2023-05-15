from sketchpy import library

list_character = ["Robert Downey Jr", "Gojo", "Tom Holland", "Flag", "APJ", "BTS", "Ironman ASCII", "Vijay"]
list_character.sort()

print("Choose a character from the list:")
for character in list_character:
	print(character)

character = input()

while character not in list_character:
	print("This character is not on the list")
	character = input()

if character == "Robert Downey Jr":
	library.rdj().draw()
	exit()
elif character == "Gojo":
	library.gojo().draw()
	exit()
elif character == "Tom Holland":
	library.tom_holland().draw()
	exit()
elif character == "Flag":
	library.flag().draw()
	exit()
elif character == "APJ":
	library.apj().draw()
	exit()
elif character == "BTS":
	library.bts().draw()
	exit()
elif character == "Ironman ASCII":
	library.ironman_ascii().draw()
	exit()
elif character == "Vijay":
	library.vijay().draw()
	exit()
