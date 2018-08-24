""" making bricks """
from controllers import *
import os


class Bricks():

	def __init__(self,length,width,type):
		"""initialising bricks"""
		self.length = length
		self.width = width
		if type == 1:
			self.matrix = [ ['[','@','@',']'], ['[','@','@',']'] ]
		else:
			self.matrix = [ ['[','#','#',']'], ['[','#','#',']'] ]
		self.x = None
		self.y = None
		self.destroyed = False
		self.type = type


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

	def destroy(self,brd,mario):
		if self.type == 1 and self.destroyed == False:
			os.system('aplay sound/coin.wav&')
			self.matrix = [ ['[','&','&',']'], ['[','&','&',']'] ]
			self.destroyed = True
			if mario.lvl == 1:
				brd.score+=100
			elif mario.lvl == 2:
				brd.score+=150
			else:
				brd.score+=200
			self.placebrick(brd)

		elif self.type == 2 and self.destroyed == False:
			self.matrix = [ ['[','&','&',']'], ['[','&','&',']'] ]
			os.system('aplay sound/powerup.wav&')
			self.destroyed = True
			if mario.lvl == 1:
				brd.score+=200
			elif mario.lvl == 2:
				brd.score+=300
			elif mario.lvl == 3:
				brd.score+=400
			mario.change('+')
			self.placebrick(brd)

		elif self.destroyed == True:
			os.system('aplay sound/brick_smash.wav&')

		

#04043468888