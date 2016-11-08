# This is a game built to complete the task in Chapter 45 of 
# "Learn Python the Hard Way". It is not perfect by any stretch.
# The first area for improvement is somehow getting the direction
# choice turned into a method so there is not as much repeated text.

from game_scenes import *

# Main engine that runs the game by continually looping with new scene names
class Engine(object):

	# Engine will be instantiated with scene_choice = SceneNames()
	def __init__(self, scene_choice):
		self.scene_choice = scene_choice
	
	# Starts play and keeps looping through
	def play(self):
		# Get opening_scene function in SceneNames() e.g. Shire()
		current_scene = self.scene_choice.opening_scene()
		
		while True:
			print "\n================"
			# Run the enter function in current_scene set 
			# via scene_choice above. e.g Shire.enter to start. This is
			# the line that generates the scene text and asks user for input.
			next_scene = current_scene.enter()
			# eg 'mordor' = RUN current_scene.enter, pass return value left

			# Run SceneNames.scene_change with return value of current scene
			current_scene = self.scene_choice.scene_change(next_scene)
			# eg Mordor() = ^SceneNames.scene_change with next_scene name/KEY		

# This is where scenes are defined and the current_scene is changed based
# on the return value of the scene that just ran.	
class SceneNames(object):
	
	scenes = {
		'shire': Shire(),
		'crossroad': Crossroad(),
		'elf_village': ElfVillage(),
		'dwarf_village': DwarfVillage(),
		'gnome_forest': GnomeForest(),
		'troll_forest': TrollForest(),
		'mountain': MountainPass(),
		'orc_pass': OrcPass(),
		'mordor': Mordor(),
		'death': Death()
	}
	
	# Instantiate the class with the first scene KEY to be run
	def __init__(self, first_scene):
		self.first_scene = first_scene
		#                   ^ 'shire' when instantiated
	
	# Function designed to pass new scene VALUES from the scenes dict above
	# to an instance of Engine.play()
	def scene_change(self, scene_name):
		# The scene_name KEY comes from the return value at the end of 
		# the current_scene running in the loop within Engine.play()
		return self.scenes.get(scene_name)
		#      ^ From SceneNames call scenes dict with KEY ('shire' at first) 
		# then GET the VALUE (Shire() at first) and returns to Engine.play()
	
	# Func to pass the first_scene dict KEY obtained on instantiation to the 
	# scene_change func above which will pass the VALUE to Engine.play()
	def opening_scene(self):
		return self.scene_change(self.first_scene)
		#      ^ From SceneNames call scene_change with first_scene ('shire')
		
scene1 = SceneNames('shire')
start1 = Engine(scene1)
start1.play()
