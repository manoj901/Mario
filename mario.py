"""defining mario"""

from person import Person
from controllers import overlayMatrix
import sys

class Mario(Person):
	"""initialising mario"""

	def __init__(self,length,width,person_type):
		"""using the person parent class"""
		Person.__init__(self,length,width,person_type)
		self.matrix =  [['[', '^', '^', ']'], ['.', ']', '[', '.']]
		self.lvl = 1

	def move(self,ch,board_object):
		"""Fucntion to move the Mario"""
		if ch == 'w':
			self.moveUp(board_object)
		elif ch == 'a':
			self.moveLeft(board_object)
		elif ch == 's':
			self.moveDown(board_object)
		elif ch == 'd':
			self.moveRight(board_object)
		elif ch=='e':
			self.moveRightJump(board_object)

	def change(self,sign):
		if sign == '+':
			if self.lvl == 1:
				self.matrix =  [['[', '@', '@', ']'], ['.', ']', '[', '.']]
				self.lvl=2

			elif self.lvl == 2:
				self.matrix = [['[', '~', '~', ']'], ['.', ']', '[', '.']]
				self.lvl = 3

		else:
			if self.lvl > 1:
				self.matrix = [['[', '^', '^', ']'], ['.', ']', '[', '.']]
				self.lvl = 1
				return 1
			return 0
