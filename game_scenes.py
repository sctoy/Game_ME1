from sys import exit
from random import randint

# Initial config of the various parties. Elves and Dwarves are broken up in
# order to allow for proper listing of options in the Elf and Dwarf Villages
main_party = ['Frodo', 'Sam'] 
dwarves = ['Gimli', 'Borin']
elves = ['Legolas', 'Amras']

# Establishes an umbrella class to hold all of the scenes
class Scene(object):

	def enter(self):
		print "Umbrella Scene class. It shouldn't be called directly."
		print "If you see this text something is awry."
		exit(1) 


# Shire scene which runs from start to decision on which direction to go	
class Shire(Scene):

	def enter(self):
		print "Welcome to the Shire. Here our humble Hobbits, Frodo and Sam,"
		print "prepare to take the One Ring to Mordor to destroy it."
		print "The way will be treacherous and they will need some help"
		print "to succeed. There are several ways to get to Mordor."
		print "The choices in front of our Hobbits are to go N, NW or NE."
		
		direction = raw_input("Which way? Enter: N, NW or NE? ")
		direction = direction.upper()
		
		while direction != "NW" or direction != "NE":
			if direction == "NW":
				print "You went NW to the Dwarf Village"
				return 'dwarf_village'
			
			elif direction == "NE":
				print "You went NE to the Elf Village"
				return 'elf_village'

			elif direction == "N":
				print "You went N to the Crossroad"
				return 'crossroad'

			else:
				print "That's not an option. Try again."
				direction = raw_input("Which way? Enter: N, NW or NE? ")
				direction = direction.upper()


# Defining Crossroad scene which merely has a choice of direction for the user
class Crossroad(Scene):

	def enter(self):
		print "You have reached the famous Crossroad at the center of"
		print "Middle Earth. Here you can go N, S, E or W."
		
		direction = raw_input("Which way? Enter: N, S, E or W? ")
		direction = direction.upper()
		
		while (direction != "N" or direction != "S" or
        		direction != "E" or direction != "W"):
			if direction == "N":
				print "You went N to the Mountain Pass"
				return 'mountain'
			
			elif direction == "S":
				print "You went S to the Shire"
				return 'shire'

			elif direction == "E":
				print "You went E to the Elf Village"
				return 'elf_village'
		
			elif direction == "W":
				print "You went W to the Dwarf Village"
				return 'dwarf_village'
				
			else:
				print "That's not an option. Try again."
				direction = raw_input("Which way? N, S, E or W? ")
				direction = direction.upper()


# Define Elf scene where the user must decide whether they want to add
# any elves to the main_party and then choose which direction to go next.	
class ElfVillage(Scene):

	def enter(self):
		print "Welcome to the Elf Village. You are welcomed by"
		print "Legolas and Amras. They are willing to join your party"
		print "and help with the mission." 
		print "You can add them by typing 'add'. Enter 'pass' to keep going."

		add_pass = raw_input()
		add_pass = add_pass.lower()
		
		if add_pass == 'add':
			print "Great. Who would you like to add? "
			for d in elves:
				print d
		
			mbr = raw_input('-> ')
			mbr = mbr.capitalize()
		
			if mbr in elves:
				print "Adding %s to Main Party and del from Elves " % mbr
				main_party.append(mbr)
				elves.remove(mbr)

				print "Now the Main Party count is %d and contains." % len(main_party)
				for mp in main_party:
					print mp
			
			else:
				print "That's not an option. Moving on."
		
		else:
			print "Ok, no changes to the party."
			
		print "Would you like to head West or East?"

		direction = raw_input("W or E? ")
		direction = direction.upper()
		
		while direction != "W" or direction != "E":
			if direction == "W":
				print "You went W to the Crossroad"
				return 'crossroad'
			
			elif direction == "E":
				print "You went E to the Forest of Wood Gnomes"
				return 'gnome_forest'
		
			else:
				print "That's not an option. Try again."
				# Is there a better way to keep trying for good input?
				direction = raw_input("W or E? ")
				direction = direction.upper()


# Define Dwarf scene where the user must decide whether they want to add
# any dwarves to the main_party and then choose which direction to go next.	

class DwarfVillage(Scene):

	def enter(self):
		print "Welcome to the Dwarf Village. You are welcomed by"
		print "Gimli and Borin. They are willing to join your party."
		print "You can add them by typing 'add'. Enter 'pass' to keep going."
		
		add_pass = raw_input()
		add_pass = add_pass.lower()
		
		if add_pass == 'add':
			print "Great. Who would you like to add? "
			for d in dwarves:
				print d
		
			mbr = raw_input('-> ')
			mbr = mbr.capitalize()
		
			if mbr in dwarves:
				print "Adding %s to Main Party and del from Dwarves " % mbr
				main_party.append(mbr)
				dwarves.remove(mbr)

				print "Now the Main Party count is %d and contains." % len(main_party)
				for mp in main_party:
					print mp

				print "Dwarves count is %d and includes: " % len(dwarves)
				for c in dwarves:
					print c
			
			else:
				print "That's not an option. Moving on."
		
		else:
			print "Ok, no changes to the party."
			
		print "Would you like to head West or East?"

		direction = raw_input("W or E? ")
		direction = direction.upper()
		
		while direction != "W" or direction != "E":
			if direction == "W":
				print "You went W to the Troll Forest"
				return 'troll_forest'
			
			elif direction == "E":
				print "You went E to the Crossroad"
				return 'crossroad'
		
			else:
				print "That's not an option. Try again."
				# Is there a better way to keep trying for good input?
				direction = raw_input("W or E? ")
				direction = direction.upper()


# Sets up Gnome Forest which decides whether the party lives or dies based
# on whether there is a dwarf in the party. If 'yes' choose next direction.
class GnomeForest(Scene):

	def enter(self):
		print "You have entered the Evil Gnome Forest."
		print "The only way to survive these evil creatures is to have the"
		print "sense of the trees and powers of a dwarf axe in your party." 
		
		if 'Gimli' in main_party or 'Borin' in main_party:
			print "Fortunately you have a dwarf"
			print "who helps you defeat the evil gnomes."
			
		else:
			print "Since you have no dwarf to combat the evil gnomes"
			print "Your entire party is killed."
			return 'death'
			 
		direction = raw_input("NW or W? ")
		direction = direction.upper()
		
		while direction != "NW" or direction != "W":
			if direction == "NW":
				print "You went NW to the Orc Pass"
				return 'orc_pass'
			
			elif direction == "W":
				print "You went W to the Elf Village"
				return 'elf_village'
		
			else:
				print "That's not an option. Try again."
				direction = raw_input("NW or W? ")
				direction = direction.upper()


# Sets up Troll Forest which decides whether the party lives or dies based
# on whether there is an elf in the party. If 'yes' choose next direction.
class TrollForest(Scene):

	def enter(self):
		print "You have entered the Evil Troll Forest."
		print "The only way to survive these evil creatures is to have the"
		print "sense and stealth of an elf in your party." 
		
		if 'Legolas' in main_party or 'Amras' in main_party:
			print "Fortunately you have an elf"
			print "who helps you defeat the evil trolls."
			
		else:
			print "Since you have no elf to combat the evil trolls"
			print "Your entire party is killed."
			return 'death'

		direction = raw_input("NE or E? ")
		direction = direction.upper()
		
		while direction != "NE" or direction != "E":
			if direction == "NE":
				print "You went NE to the Orc Pass"
				return 'orc_pass'
			
			elif direction == "E":
				print "You went E to the Dwarf Village"
				return 'dwarf_village'
		
			else:
				print "That's not an option. Try again."
				direction = raw_input("NE or E? ")
				direction = direction.upper()


# Sets up Mountain Pass scene which allows party to pass if there is a 
# Dwarf in the party. If party tries to pass without a Dwarf they die.
class MountainPass(Scene):

	def enter(self):
		print "You have reached the Mountain Pass. It is an scary looking." 
		
		if 'Gimli' in main_party or 'Borin' in main_party:
			print "Fortunately you have a dwarf who knows a secret passage"
			print "to the North. Do you want to go North or turn back South?"
			direction = raw_input("N or S? ")
			direction = direction.upper()
			
			while direction != 'N' or direction != 'S':
				if direction == 'N':
					print "You went North through the secret pass."
					return 'orc_pass'
			
				elif direction == 'S':
					print "You went S to the Crossroad"
					return 'crossroad'					
				
				else:
					print "That's not an option. Try again."
					# Makes another attempt for additional input. Seems inefficient.
					direction = raw_input("N or S? ")
					direction = direction.upper()				
			
		else:
			print "Do you want to go N and climb the pass or turn back S?"
			direction = raw_input("N or S? ")
			direction = direction.upper()
			
			while direction != "N" or direction != "S":
				if direction == 'N':
					print "You decided to climb. It is unpassable without"
					print "a dwarf's knowledge of the secret pass."
					print "Your entire party slips off the Mountain and dies."
					return 'death'
				
				elif direction == 'S':
					print "You went S to the Crossroad"
					return 'crossroad'
					
				else:
					print "That's not an option. Try again."
					direction = raw_input("N or S? ")
					direction = direction.upper()				
			 
# Sets up Orc scene where the party can survive is they have both an elf and
# a dwarf in the party. If 'yes' get next direction.		 
class OrcPass(Scene):

	def enter(self):
		print "You have come to a pass filled with Orcs."
		if (
			('Gimli' in main_party or 'Borin' in main_party)
			and ('Legolas' in main_party or 'Amras' in main_party)
		):
			print "The only way to survive the Orcs is to have the skills"
			print "of both an elf and a dwarf."
			print "Fortunately you do so the adventure continues."

		else: 
			print "The only way to survive the Orcs is to have the skills"
			print "of both an elf and a dwarf."
			print "Unfortunately you don't so your party is slaughtered"
			return 'death'		

		direction = raw_input("N, SE or SW? ")
		direction = direction.upper()
		
		while direction != "N" or direction != "SE" or direction != "SW":
			if direction == "N":
				print "You went North to Mordor"
				return 'mordor'
			
			elif direction == "SE":
				print "You went SE to the Gnome Forest"
				return 'gnome_forest'

			elif direction == "SW":
				print "You went SW to the Troll Forest"
				return 'troll_forest'
				
			else:
				print "That's not an option. Try again."
				direction = raw_input("W or E? ")
				direction = direction.upper()


# Sets up Mordor where the game succeeds and exits if Frodo is in the party.
# Presently there is no way to dump Frodo so this will always win.
class Mordor(Scene):
	
	def enter(self):
		print "Welcome to Mordor!"
		
		if 'Frodo' in main_party:
			print "Since your brave Hobbit Frodo is in your Party with the"
			print "One Ring he tosses it into the fires and destroys it."
			print "Your mission is a success. Congratulations!!!"
			exit(0)
			
		else:
			print "Since you dumped Frodo along the way you don't have a ring"
			print "to throw into the fires. The power of the ring let's the"
			print "evil forces gather and, well...you are killed."
			return 'death'


# Just a random message on exit to practice coding and nothing else
class Death(Scene):
	
	death_msg = [
		'Bummer Dude!',
		'Try again!',
		'J.R.R Tolkien is not impressed!',
		'Ouch!'
	]
	
	def enter(self):
		print self.death_msg[randint(0, 3)]
		exit(1)
		
