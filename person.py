"""Using this as the parent class for mario and enemies"""
from controllers import *

class Person(object):
	"""def for person"""

	def __init__(self,length,width,person_type):
		"""initialising person"""
		self.length = length
		self.width = width
		self.person_type = person_type
		self.matrix = []
		self.x = None
		self.y = None

	def setNewPosition(self,board_object,x,y):
		"""set the object for the first time"""
		if checkClash(board_object,self,x,y)==0:
			overlayMatrix(board_object,self,x,y)
			self.setPos(x,y)
			return 0
		else:
			return 1

	def setPos(self,x,y):
		"""set the pos"""
		self.x = x
		self.y = y

	def returnMatrix(self):
		"""return the matrix"""
		return self.matrix

	def moveLeft(self,board_object):
		"""make the person move left by changing cords"""

		if checkClash(board_object,self,self.x,self.y-1) == 0:
			if(self.y-1>board_object.start):
				overlayMatrix(board_object,self,self.x,self.y-1)
				self.setPos(self.x,self.y - 1)
		else:
			return 1

	def moveRight(self,board_object):
		"""make the person move left by changing cords"""
		if checkClash(board_object,self,self.x,self.y+1) == 0:
			overlayMatrix(board_object,self,self.x,self.y+1)
			self.setPos(self.x,self.y+1)
			if self.y > board_object.start + 25: 
				board_object.start += 1
		else:
			return 1


	def moveUp(self,board_object):
		"""make the person move left by changing cords"""
		for i in range(0,1):
			if checkClash(board_object,self,self.x-1,self.y) == 0:
				overlayMatrix(board_object,self,self.x-1,self.y)
				self.setPos(self.x-1,self.y)
			else:
				return 1


	def moveDown(self,board_object):
		"""make the person move left by changing cords"""
		if checkClash(board_object,self,self.x+1,self.y) == 0:
			overlayMatrix(board_object,self,self.x+1,self.y)
			self.setPos(self.x+1,self.y )
		else:
			return 1

	def moveRightJump(self,board_object):
		"""make the person move left by changing cords"""
		if checkClash(board_object,self,self.x-1,self.y+1) == 0:
			overlayMatrix(board_object,self,self.x-1,self.y+1)
			self.setPos(self.x-1,self.y+1 )
		else:
			return 1

	def die(self,brd):
		"""killing the person"""
		self.matrix = [[' ',' ',' ',' '],[' ',' ',' ',' ']]
		overlayMatrix(brd,self,self.x,self.y)