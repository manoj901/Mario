from person import Person
from checkclss import *
from controllers import overlayMatrix
from brickcords import Rem
import sys

class Enemy(Person):

	def __init__(self,length,width,person_type,di=1):
		"""using the person parent class"""
		Person.__init__(self,length,width,person_type)
		self.matrix =  [['^', '^'], ['|', "|"]]
		self.dir = di
		self.liv = 1


	def moveLefti(self,board_object):
		"""make the person move left by changing cords"""

		if checkClash2(board_object,self,self.x,self.y-1) == 0:
			overlayMatrix(board_object,self,self.x,self.y-1)
			self.setPos(self.x,self.y - 1)
		else:
			return 1

	def moveRighti(self,board_object):
		"""make the person move left by changing cords"""
		if checkClash2(board_object,self,self.x,self.y+1) == 0:
			overlayMatrix(board_object,self,self.x,self.y+1)
			self.setPos(self.x,self.y+1)
		else:
			return 1

	def destroy(self,board_object):
		self.matrix =  [[' ', ' '], [' ', ' ' ]]
		overlayMatrix(board_object,self,self.x,self.y)
		overlayMatrix(board_object,Rem.mar[0],Rem.mar[0].x,Rem.mar[0].y)
		self.liv =0