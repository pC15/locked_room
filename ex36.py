# Game variables:
#	key

key = False

# Game functions:
#	start_game, do_nothing, did_not_comprehend
#	ceiling_door, floor_door, key_status
#	search_room

def start_game():
	print "You are in a room without windows."
	print "There is a door on the ceiling and a door on the floor."
	print "What do you do? \n"
	print "1. Try to open the floor door."
	print "2. Try to open the ceiling door."
	print "3. Do nothing. \n"
	
	choice = raw_input("> ")
	
	if choice == "1":
		floor_door()
	elif choice == "2":
		ceiling_door()
	elif choice == "3":
		do_nothing()
	else:
		did_not_comprehend()
		
# Bad Ending.
def do_nothing():
	print "\nYou spend the rest of your days wishing you tried"
	print "to do something, but were too scared to try anything. \n"
	print "You perished, insane and alone. \n"
	print "Such a waste of potential. \n"
	print "Hooray. \n"
	print "Bad Ending. \n"

# This function is to make sure the game doesn't break
# from a unknown command.
def did_not_comprehend():
	print "\nYou instantly died form doing something incomprehensible. \n"
	print "No one missed your presence or even remembered who you were. \n"
	print "Hooray. \n"
	
# Good Ending.
def ceiling_door():
	print "\nYou are just tall enough to reach the ceiling door."
	print "You grasp the doorknob and turn with ease."
	print "\n... ... ... ... ...\n"
	print "The door opens and a blizzard of confetti assaults your senses."
	print "You pull yourself out the room to freedom. \n"
	print "You escaped."
	print "Hooray. \n"
	print "Good Ending. \n"
	
def floor_door():
	print "\nYou try the floor door, but it does not budge."
	print "There is a keyhole in the doorknob."
	print "What do you do? \n"
	print "1. Search the room for a key."
	print "2. Try to open the door."
	print "3. Do nothing. \n"
	
	choice = raw_input("> ")
	
	if choice == "1":
		search_room()
	elif choice == "2":
		if key == True:
			print "\nYou escaped."
			print "Hooray. \n"
		else:
			floor_door()
	elif choice == "3":
		do_nothing()
	else:
		did_not_comprehend()

def key_status():
	global key
	if key == True:
		print "\nYou have the key."
	else:
		print "\nYou do not have the key."

def search_room():
	print "\nThere are many objects in the room."
	print "Which do you take? \n"
	print "1. Screwdriver."
	print "2. Bobby pin."
	print "3. Ladder."
	print "4. Mysteriously large box."
	print "5. Do nothing."
	
	choice = raw_input("> ")
	
	if (choice == "1" or choice == "2" or choice == "3"):
		key_status()
		floor_door()
	elif choice == "4":
		global key
		key = True
		key_status()
		floor_door()
	elif choice == "5":
		do_nothing()
	else:
		did_not_comprehend()


# Here's where the actual game starts.
start_game()