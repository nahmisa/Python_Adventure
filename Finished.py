from sys import exit
from Scene import *

class Finished(Scene):
	
	def enter(self):
		print "Congrats! You finished the game!!! :D"
		exit(1)