""" making bricks """
from controllers import *

class Holes():

	def __init__(self,length,width):
		"""initialising bricks"""
		self.length = length
		self.width = width
		self.matrix = [ [' ',' ',' ',' '], [' ',' ',' ',' '] ]
		self.x = None
		self.y = None
		self.destroyed = False


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