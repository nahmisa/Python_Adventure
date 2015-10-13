from Fairy_Godmother_Scene import Fairy_Godmother
from Goldilocks_Scene import Goldilocks
from Snow_White_Scene import Snow_White
from Sleeping_Beauty_Scene import Sleeping_Beauty
from Finished import Finished

# The Engine references this map to find the scenes		
class Map(object):
		
	scenes = {'Fairy Godmother': Fairy_Godmother(),
			  'Goldilocks': Goldilocks(), 
			  'Snow White': Snow_White(),
			  'Sleeping Beauty': Sleeping_Beauty(),
			  'Finished': Finished()
			  }
	
	def __init__(self, start_scene): # we get the start scene from the functions at the end that run the game.  
									 # based on the string we put into a_map
		self.start_scene = start_scene
		
	def get_scene(self, scene_name): # since I removed the "opening_scene" function because I didn't like it, can I remove the self here?
									 # based on my current understanding, this does not need to be global
		val = Map.scenes.get(scene_name) # variable scene_name comes from unpacked Engine functions
		return val
	def opening_scene(self): # this is just for the first scene because of the parameters necessary to make get_scene
	# work for all other scenes.
		return self.get_scene(self.start_scene)
	
