
# we will need an engine to power the game through the scenes
class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene() # we need to use a function different 
													   # from get_scene because get_scene needs parameters
													   # so there is a special opening_scene that is run once!
		last_scene = self.scene_map.get_scene('Finished')
		
		while current_scene != last_scene:
			next_scene_string = current_scene.enter()
			current_scene = self.scene_map.get_scene(next_scene_string)
			
		current_scene.enter()