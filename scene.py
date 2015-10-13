# Organized scenes by parent class scene

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		# having text instead of pass helps us for testing and to see errors, but there will be no real scenes in
		# this object/class
		exit(1)