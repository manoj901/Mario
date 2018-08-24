"""walls"""

class Walls():

	def placeWalls(board_object):
		""" Placing the floor basically """
		game_board = board_object.retBoard()
		length =  board_object.length
		width = board_object.width

		for x in range(length-2,length):
			for y in range(0,width):
				game_board[x][y]='X'