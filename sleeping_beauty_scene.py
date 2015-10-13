from Scene import *
from Contains import *

class Sleeping_Beauty(Scene):
	
	def enter(self):
		print """
***Sleeping Beauty***

Needs... something to waker her up? make a prince to kiss her?
"""
		input = raw_input("> ")
		
		answer = Contains().in_array(input, ['string', 'integer']) # variables are keywords to return "correct" answer
		
		while answer == False: 
			print "How many hints would you like?"
			number_hints = raw_input("(1,2, or 3)> ")
			hints = ["Hint1", 
					 "Hint2", 
					 "Hint3"]
			
			for item in hints[:int(number_hints)]:
				print item
			print "Give a solution or ask for another hint."
			
			input = raw_input("> ")
		
		self.happy_ending()
			
		return 'Finished'

	def happy_ending(self):
		print """
Happy ending text
"""