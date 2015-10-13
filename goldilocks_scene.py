from Scene import *
from Contains import *

class Goldilocks(Scene):
	
	def enter(self):
		print """
***Goldilocks and the Three Bears***

Goldilocks sits on the floor of a house, furnished with three of everything.
She cries in frustration. 
'This won't work! How am I supposed to know how many live here when this program 
won't work?'
The program Goldilocks is working on looks like this:
	
	stolen_property = chairs
	owners = bears
	number_property = 'three'
	number_owners = '3.0'
	
	chair_per_bear = number_property/number_owners

	print "Goldilocks tried each of the %s that belonged to the %d %s." % (stolen_property, number_owners, owners)
	print "That's %d chair per bear." % (chair_per_bear)

'It doesn't print anything,' she continues to cry.

How would you fix Goldilocks' code? What has she confused?
"""
		input = raw_input("> ")
		
		answer = Contains().in_array(input, ['string', 'integer']) # variables are keywords to return "correct" answer
		
		while answer == False: 									                       		
			print "How many hints would you like?"
			number_hints = raw_input("(1,2, or 3)> ")
			hints = ["Think about what the type (string, integer or float) should be for each value", 
					 "Strings have letters and we surround them in ' '", 
					 "Integers and floats do not get surrounded and have numbers, or numbers and decimals"]
			
			for item in hints[:int(number_hints)]:
				print item
			print "Give a solution or ask for another hint."
			
			input = raw_input("> ")
		
		self.happy_ending()
				
		return 'Snow White'
	

	def happy_ending(self):
		print """
'Hooray!' Fairy Godmother cries. 'You are the hero we've been hoping for!  Look how
happy Goldilocks is to realize there are only three bears!'  
Here is the code after your suggestions:
	
	stolen_property = 'chairs'
	owners = 'bears'
	number_property = 3
	number_owners = 3

	chair_per_bear = number_property/number_owners

	print "Goldilocks tried each of the %s that belonged to the %d %s." % (stolen_property, number_owners, owners)
	print "That's %d chair per bear." % (chair_per_bear)
	
Output:	
	Goldilocks tried each of the chairs that belonged to the 3 bears.
	That's 1 chair per bear.
"""					
