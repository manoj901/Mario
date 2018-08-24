from person import Person
from controllers import overlayMatrix
import sys

class Flagy(Person):
	"""initialising mario"""

	def __init__(self,length,width,person_type):
		"""using the person parent class"""
		Person.__init__(self,length,width,person_type)
		self.matrix =  [['#','#','#'],['#','#','#'],['#','#','#']]


