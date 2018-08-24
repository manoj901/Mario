from person import Person
from controllers import *

class Bullets(Person):

	def __init__(self,length,width,person_type):
		"""using the person parent class"""
		Person.__init__(self,length,width,person_type)
		self.matrix =  [['>']]
		self.liv = 1

	def destroy(self,board_object):
		self.matrix =  [[' ']]
		for i in range(self.x,self.x+1):
			for j in range(self.y,self.y+1):
				board_matrix[i][j] = ' '
		overlayMatrix(board_object,self,self.x,self.y)
		self.liv =0

	def moveRight(self,board_object):
		"""make the person move left by changing cords"""
		if checkClash(board_object,self,self.x,self.y+1) == 0:
			overlayMatrix(board_object,self,self.x,self.y+1)
			self.setPos(self.x,self.y+1)
			
		else:
			self.matrix =  [[' ']]
			overlayMatrix(board_object,self,self.x,self.y)
			self.liv =0
			return 1