from Scene import * 
from Contains import *
		
class Fairy_Godmother(Scene):

	def enter(self):
		print """
A woman with wings stands before you.
'Welcome, welcome to Once Upon a Program... 
the game where the answers are made up and the syntax matters! 
I am your fairy godmother, darling, here to guide you on your quest.  

Your fairy godmother looks sad. She explains:
'Darling, all the fairy tale folk have been trapped inside this computer
by an evil spell.  Try as I might, I cannot break this spell to free us.
Honestly, we are all quite confused.  This typing and detail - ugh. 
Not to mention these disgusting... bugs, are they called? 
We've begun to lose hope.  There are no dragons or trolls to slay, 
instead, we are trapped by riddles none of us can solve! 
You're our only hope.'

Would you like to hear the rules?
			"""
		input = raw_input("(Y/N)> ")
	
		if input == "N":
			print "Bibbidi-Bobbidi-Boo!  Good luck to youuuuuuu!"
			return 'Goldilocks'
			
		else:
			self.print_rules()
			input = raw_input("> ")
			
			answer = Contains().in_array(input, ["i've got it"]) # variables are keywords to return "correct" answer	
			
			while answer == False:
				self.print_rules()
				answer = raw_input("> ")
					
			print "Bibbidi-Bobbidi-Boo!  Good luck to youuuuuuu!"
			return 'Goldilocks'
	
	def print_rules(self):
		print """
 Fairy Godmother kindly explains:
 'Each fairy tale character is trapped by a different riddle. You will need to solve
 the riddle so they can escape back to their proper fairy tale.  We have found these 
 riddles to be quite challenging, but don't dispair! I will be with you to help and guide 
 you.  If you get stuck, simply ask for a 'Hint'.  I have three hints per riddle to
 aid you in your quest. If you try to solve a riddle and don't get the correct answer right away,
 never fear! I will aid you with the hints unprompted.'
			  """
		print "If you're with me so far, enter 'I've got it'. Otherwise, I can go over the rules again." 					
					