""" making a board """
import time,os,sys
from brickcords import Rem

class Board():

	def __init__(self,length,width):
		"""creating an empty board"""

		self.length = length
		self.width = width
		self.matrix = []
		self.score = 0
		self.start = 0
		self.lives = 3

		for x in range(0,length):
			self.matrix.append([])
			for y in range(0,width):
				self.matrix[x].append(' ')


	def retBoard(self):
		"""returns the matrix of the board"""
		return self.matrix


	def retBoardStr(self):
		"""return the board as a sring"""

		t = time.time()
		remain = 150 - (t-Rem.tim[0])
		rem = int(remain//1)

		if remain <= 0:
			os.system('pkill aplay')
			os.system('aplay sound/evil_morty_theme.wav&')
			time.sleep(0.01)
			os.system('clear')
			print('TIMED OUT')
			time.sleep(5)
			os.system('clear')
			print('GAME OVER' + '\n')
			print('SCORE: ' + str(self.score) + '\n')
			time.sleep(10)
			sys.exit()

		boardstr = ""
		for x in range(0,self.length):
			if self.start + 59 > self.width:
				lim = self.width
				st = self.width - 59
			else:
				lim = self.start + 59
				st = self.start

			for y in range(st,lim):
				boardstr += self.matrix[x][y]
			boardstr += '\n'
		boardstr += "SCORE: " + str(self.score) + "\n"
		boardstr += "LIVES: " + str(self.lives) + "\n"
		boardstr += "TIME: " + str(rem) + "\n"
		boardstr += "Press 'l' to exit\n"
		return boardstr

	def editBoard(self,newMatrix):
		"""changes the board to the edited one"""
		self.matrix = newMatrix