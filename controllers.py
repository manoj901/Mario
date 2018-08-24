
from brickcords import Rem
import os,time,sys
def overlayMatrix(board_object,item_object,x,y):
	"""placing items on the board likes bricks and stuff"""
	board_matrix = board_object.retBoard()
	item_matrix = item_object.returnMatrix()
	k =0 
	l = 0
	for i in range(x,x+item_object.length):
		for j in range(y,y+item_object.width):
			board_matrix[i][j] =item_matrix[k][l]
			l+=1
		k+=1
		l=0
	board_object.editBoard(board_matrix)

def checkClash(board_object,item_object,x,y):
	"""Check if the item is clashing with a wall/brick"""
	board_matrix = board_object.retBoard()
	prev_x = item_object.x
	prev_y = item_object.y

	

	#Erasing the object before checking
	if prev_x is not None:
		for i in range(prev_x,prev_x+item_object.length):
			for j in range(prev_y,prev_y+item_object.width):
				board_matrix[i][j] = ' '

	if x + item_object.length >= board_object.length:

	#start
		board_object.lives-=1
		if board_object.lives != 0:
			os.system('pkill aplay')
			os.system('clear')
			print(board_object.retBoardStr())
			os.system('aplay death.wav&')
			xi = Rem.mar[0].y
			yi = Rem.mar[0].x
			if 0 < xi < 100:
				Rem.mar[0].y = 4
				Rem.mar[0].x =  board_object.length - 4
				ko=0
				while Rem.mar[0].change('-') == 0:
					ko+=1
				for i in range(yi,yi+Rem.mar[0].length):
					for j in range(xi,xi+Rem.mar[0].width):
						board_matrix[i][j] = ' '
				overlayMatrix(board_object,Rem.mar[0],Rem.mar[0].x,4)
				board_object.start = 0
			elif 100 <= xi < 200:
				Rem.mar[0].y = 104
				Rem.mar[0].x = board_object.length - 4
				ko=0
				while Rem.mar[0].change('-') == 0:
					ko+=1
				for i in range(yi,yi+Rem.mar[0].length):
					for j in range(xi,xi+Rem.mar[0].width):
						board_matrix[i][j] = ' '
				overlayMatrix(board_object,Rem.mar[0],Rem.mar[0].x,104)
				board_object.start = 100
			elif 200 <= xi < 300:
				Rem.mar[0].y = 220
				Rem.mar[0].x =  board_object.length - 4
				ko=0
				while Rem.mar[0].change('-') == 0:
					ko+=1
				for i in range(yi,yi+Rem.mar[0].length):
					for j in range(xi,xi+Rem.mar[0].width):
						board_matrix[i][j] = ' '
				overlayMatrix(board_object,Rem.mar[0],Rem.mar[0].x,220)
				board_object.start = 200
			elif 300 <= xi < 400:
				Rem.mar[0].y = 304
				Rem.mar[0].x =  board_object.length - 4
				board_object.start = 300
				ko=0
				while Rem.mar[0].change('-') == 0:
					ko+=1
				for i in range(yi,yi+Rem.mar[0].length):
					for j in range(xi,xi+Rem.mar[0].width):
						board_matrix[i][j] = ' '
				overlayMatrix(board_object,Rem.mar[0],Rem.mar[0].x,304)
				board_object.start = 300
			elif 400 <= xi < 500:
				Rem.mar[0].y = 404
				Rem.mar[0].x =  board_object.length - 4
				board_object.start = 400
				ko=0
				while Rem.mar[0].change('-') == 0:
					ko+=1
				for i in range(yi,yi+Rem.mar[0].length):
					for j in range(xi,xi+Rem.mar[0].width):
						board_matrix[i][j] = ' '
				overlayMatrix(board_object,Rem.mar[0],Rem.mar[0].x,404)
				board_object.start = 400
			time.sleep(3)
			os.system('aplay sound/main_theme.wav&')
			return 1
		else:
			os.system('pkill aplay')
			os.system('aplay sound/evil_morty_theme.wav&')
			time.sleep(5)
			os.system('clear')
			print('GAME OVER' + '\n')
			print('SCORE: ' + str(self.score) + '\n')
			time.sleep(10)
			sys.exit()
	# time.sleep(0.3)


	# Check for the clash , if not overlay to the previous cords
	for i in range(x,x+item_object.length):
		for j in range(y,y+item_object.width):
			if board_matrix[i][j] != ' ':
				if board_matrix[i][j] != '^':
					overlayMatrix(board_object,item_object,prev_x,prev_y)
					for br in Rem.lis:
						if br.x+1 <= i <= br.x+2 and br.y <= j <= br.y+4:
							br.destroy(board_object,item_object)

							return 1
				else:
					overlayMatrix(board_object,item_object,prev_x,prev_y)
					for rodri in Rem.lenem:
						if rodri.y - 2 < y < rodri.y + 2 and rodri.liv == 1:
							Rem.remar.append(rodri)

				return 1
	return 0

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
		if hol[1] == y or hol[1] == y+2:
			overlayMatrix(board_object,item_object,prev_x,prev_y)
			item_object.dir*=-1

	for i in range(x,x+item_object.length):
		for j in range(y,y+item_object.width):
			if board_matrix[i][j] != ' ':
				if board_matrix[i][j] == '.' or board_matrix[i][j] == '[' or board_matrix[i][j] == ']':
					if Rem.mar[0].change('-')==0:
						board_object.lives-=1
					os.system('aplay death.wav&')
					# time.sleep(0.3)
				overlayMatrix(board_object,item_object,prev_x,prev_y)
				item_object.dir*=-1
				return 1
	return 0

