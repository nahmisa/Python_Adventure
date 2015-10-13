from Scene import *
from Contains import *

class Snow_White(Scene):
	
	def enter(self):
		print """
***Snow White and the Seven Dwarves***

Snow White has an apple in one hand an a pear in the other.  Her stomach is growling loudly
and she is looking very perplexed.
'I could really use some help.  The dwarves wrote me a program so I wouldn't ingest any 
poisonous fruit... but I can't figure out how it works!  I think this program only tests
for apples, and it seems to me that apples can be both poisonous and not poisonous.  I'm
so confused - and very hungry!'
She shows you this code, asking, 'How can I find out if I can eat this pear, and is it a 
good idea to take a bite of this apple?'

	def poisoned(apple):

		if apple == 'apple':
			print "Don't eat it! It's poisoned!"
	
		else:
			print "Totally not poisoned! Enjoy that %s." %(apple)
	

What would you change about the dwarves' code - can you see how Snow could be confused?
"""
		input = raw_input("> ")
		
		answer = Contains().in_array(input, ['parameter', 'argument']) # variables are keywords to return "correct" answer
		
		while answer == False: 							
			print "How many hints would you like?"
			number_hints = raw_input("(1,2, or 3)> ")
			hints = ["Functions take both paramaters and arguments.", 
					 "The name of the variable we pass as an argument has nothing\n\tto do with the name of the parameter... but it sure can be confusing!", 
					 "Something that is both an apple and pear would be a better parameter\n\tname since Snow needs to test multiple things."]
			
			for item in hints[:int(number_hints)]:
				print item
			print "Give a solution or ask for another hint."
			
			input = raw_input("> ")
		
		self.happy_ending()
			
		return 'Sleeping Beauty'

	def happy_ending(self):
		print """
Snow White exclaims, 'Oh, now I get it!' and is able to use the function to test her pear 
and apple.  She quickly discards the apple and happily chomps into the pear.
Your fairy godmother is quite impressed. 
'Darling, that was so astute. Fruit is a much better parameter name.  This function is 
now easier to read and understand'
Here is the code after your suggestion:

	def poisoned(fruit):

		if fruit == 'apple':
			print "Don't eat it! It's poisoned!"
	
		else:
			print "Totally not poisoned! Enjoy that %s." %(fruit)
"""
