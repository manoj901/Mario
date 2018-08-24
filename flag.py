from person import Person
from controllers import overlayMatrix
import sys

class Flagpole(Person):
	"""initialising mario"""

	def __init__(self,length,width):
				
		self.matrix =  [['|'],['|'],['|'],['|'],['|'],['|'],['|'],['|'],['|'],['|'],['|'],['|']]
		self.length = length
		self.width = width
		self.x = None
		self.y = None

	def returnMatrix(self):
		"""return bricks"""
		return self.matrix

	def setPosition(self,x,y):
		"""setting the position of bricks"""
		self.x = x
		self.y = y

	def placebrick(self,brd):
		"""places brick on the board"""
		overlayMatrix(brd,self,self.x,self.y)
		