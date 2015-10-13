
class Contains(object):
		
	def in_array(self, input, answers):
		
		for item in answers:
			if item.lower() in input.lower():
				 return True
				
		return False