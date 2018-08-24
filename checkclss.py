from brickcords import Rem
import os,time
import sys
from controllers import overlayMatrix
def checkClash2(board_object,item_object,x,y):

	board_matrix = board_object.retBoard()
	prev_x = item_object.x
	prev_y = item_object.y
	brd = board_object
	l = brd.length

	#Erasing the object before checking
	if prev_x is not None:
		for i in range(prev_x,prev_x+item_object.length):
			for j in range(prev_y,prev_y+item_object.width):
				board_matrix[i][j] = ' '

	for hol in Rem.holes:
		if hol[1] < y < hol[1]+4:
			item_object.dir*=-1
			break

	for i in range(x,x+item_object.length):
		for j in range(y,y+item_object.width):
			if board_matrix[i][j] != ' ':
				if board_matrix[i][j] == '.' or board_matrix[i][j] == '[' or board_matrix[i][j] == ']':
					if Rem.mar[0].change('-')==0:
						board_object.lives-=1
						if board_object.lives != 0:
							os.system('pkill aplay')
							os.system('aplay death.wav&')
							xi = Rem.mar[0].y
							yi = Rem.mar[0].x
							if 0 < xi < 100:
								Rem.mar[0].y = 4
								Rem.mar[0].x = prev_x
								for i in range(yi,yi+Rem.mar[0].length):
									for j in range(xi,xi+Rem.mar[0].width):
										board_matrix[i][j] = ' '
								overlayMatrix(board_object,Rem.mar[0],board_object.length-4,4)
								board_object.start = 0
							elif 100 <= xi < 200:
								Rem.mar[0].y = 104
								Rem.mar[0].x = prev_x
								for i in range(yi,yi+Rem.mar[0].length):
									for j in range(xi,xi+Rem.mar[0].width):
										board_matrix[i][j] = ' '
								overlayMatrix(board_object,Rem.mar[0],board_object.length-4,104)
								board_object.start = 100
							elif 200 <= xi < 300:
								Rem.mar[0].y = 204
								Rem.mar[0].x = prev_x
								for i in range(yi,yi+Rem.mar[0].length):
									for j in range(xi,xi+Rem.mar[0].width):
										board_matrix[i][j] = ' '
								overlayMatrix(board_object,Rem.mar[0],board_object.length-4,204)
								board_object.start = 200
							elif 300 <= xi < 400:
								Rem.mar[0].y = 304
								board_object.start = 300
								for i in range(yi,yi+Rem.mar[0].length):
									for j in range(xi,xi+Rem.mar[0].width):
										board_matrix[i][j] = ' '
								overlayMatrix(board_object,Rem.mar[0],board_object.length-4,304)
								board_object.start = 300
							elif 400 <= xi < 500:
								Rem.mar[0].y = 404
								board_object.start = 400
								for i in range(yi,yi+Rem.mar[0].length):
									for j in range(xi,xi+Rem.mar[0].width):
										board_matrix[i][j] = ' '
								overlayMatrix(board_object,Rem.mar[0],board_object.length-4,404)
								board_object.start = 400
							time.sleep(3)
							os.system('aplay sound/main_theme.wav&')
						else:
							os.system('pkill aplay')
							os.system('aplay sound/evil_morty_theme.wav&')
							time.sleep(5)
							os.system('clear')
							print('GAME OVER')
							time.sleep(10)
							sys.exit()
					# time.sleep(0.3)
				if board_matrix[i][j] == '>':
					overlayMatrix(board_object,item_object,prev_x,prev_y)
					Rem.remar.append(item_object)
				overlayMatrix(board_object,item_object,prev_x,prev_y)
				item_object.dir*=-1
				return 1
	return 0

