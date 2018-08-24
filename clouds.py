from controllers import *
import os


class Clouds():

	def __init__(self,length,width):
		"""initialising bricks"""
		self.length = length
		self.width = width
		self.matrix = [[' ','O','O','O','O',' '],['C','C','C','C','C','C'],['O','O','O','O','O','O'],[' ','O','O','O','O',' ']]
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
