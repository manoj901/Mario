from board import Board
from wall import Walls
from pipes import Pipes
from bricks import Bricks
from holes import Holes
from stair import Stair
from brickcords import Rem
from enemy import Enemy
from flagy import *
from bullets import Bullets
import os
import sys
import time
import tty
from input import Get, input_to
from clouds import *
from flag import *
from mario import *

brd = Board(19,600)
Walls.placeWalls(brd)
l = brd.length
Brick_coordinates = [[12,28,1],[12,40,1],[12,56,1],[12,48,1],[12,52,2],[12,44,1],[6,48,1],[12,264,1],[12,268,1],[12,272,2],[6,276,1],[6,280,1],[6,284,1],[6,288,1],[6,292,1],[6,304,1],[6,308,1],[6,312,1],[6,316,1],[12,316,1],[12,324,1],[12,328,1],[12,338,1],[12,348,1],[12,358,1],[6,348,1],[12,370,1],[6,374,1],[6,378,1],[6,381,1],[6,393,1],[6,397,1],[6,401,1],[6,405,1],[12,397,1],[12,401,1],[12,522,1],[12,526,1],[12,530,1],[12,534,1]]
Pipe_coordinates = [[brd.length-8,68],[brd.length-8,110],[brd.length-8,152],[brd.length-8,200],[l-8,510],[l-8,550]]
Holes_coordinates = [[brd.length-2,248],[brd.length-2,290],[l-2,486],[l-2,488]]
Stair_coordinates = [[brd.length-4,418],[brd.length-4,422],[brd.length-4,426],[brd.length-4,430],[brd.length-6,422],[l-6,426],[l-6,430],[l-8,426],[l-8,430],[l-10,430],[brd.length-4,454],[brd.length-4,450],[brd.length-4,446],[brd.length-4,442],[brd.length-6,450],[l-6,446],[l-6,442],[l-8,446],[l-8,442],[l-10,442],[l-4,466],[l-4,470],[l-4,474],[l-4,478],[l-4,482],[l-6,470],[l-6,474],[l-6,478],[l-6,482],[l-8,474],[l-8,478],[l-8,482],[l-10,478],[l-10,482],[l-4,492],[l-4,496],[l-4,500],[l-4,504],[l-6,492],[l-6,496],[l-6,500],[l-8,492],[l-8,496],[l-10,492],[l-4,554],[l-4,558],[l-4,562],[l-4,566],[l-4,570],[l-4,574],[l-6,558],[l-6,562],[l-6,566],[l-6,570],[l-6,574],[l-8,562],[l-8,566],[l-8,570],[l-8,574],[l-10,566],[l-10,570],[l-10,574],[l-12,570],[l-12,574],[l-14,574]]
Enem_coordinates = [[l-4,120],[l-4,208],[l-4,124,-1],[l-4,240],[l-4,255,-1],[l-4,270,1],[l-4,305],[l-4,310],[l-4,370,-1],[l-4,520]]
Cloud_coordinates = [[0,10],[0,75],[0,100],[0,150],[0,230],[0,350],[0,400],[0,450],[0,500],[0,550]]
for cord in Brick_coordinates:
	bricks = Bricks(2,4,cord[2])
	bricks.setPosition(cord[0],cord[1])
	bricks.placebrick(brd)
	Rem.lis.append(bricks)

for cord in Pipe_coordinates:
	bricks = Pipes(6,4)
	bricks.setPosition(cord[0],cord[1])
	bricks.placebrick(brd)

for cord in Holes_coordinates:
	bricks = Holes(2,4)
	bricks.setPosition(cord[0],cord[1])
	bricks.placebrick(brd)

for cord in Stair_coordinates:
	bricks = Stair(2,4)
	bricks.setPosition(cord[0],cord[1])
	bricks.placebrick(brd)

for cord in Cloud_coordinates:
	bricks = Clouds(4,6)
	bricks.setPosition(cord[0],cord[1])
	bricks.placebrick(brd)

pole = Flagpole(12,1)
pole.setPosition(brd.length-14,590)
pole.placebrick(brd)

flagt = Flagy(3,3,'flag')
flagt.setNewPosition(brd,brd.length-14,591)

mario_inix = brd.length -4
mario_iniy = 4
mario = Mario(2,4,'mario')
mario.setNewPosition(brd,mario_inix,mario_iniy)
Rem.mar.append(mario)
bul = []
lenem = []
for cord in Enem_coordinates:
	if len(cord)==2:
		enem = Enemy(2,2,'enem')
	else:
		enem = Enemy(2,2,'enem',cord[2])
	enem.setNewPosition(brd,cord[0],cord[1])
	lenem.append(enem)
	Rem.lenem.append(enem)

os.system('clear')
t = time.time()
Rem.tim.append(t)
print(brd.retBoardStr())
getch = Get()

os.system('aplay sound/main_theme.wav&')

while True:

	if 585 <= mario.y <= 590:
		bonus = int((150-(time.time()-t))//1)*30
		os.system('pkill aplay')
		os.system('aplay sound/flagpole.wav&')
		while True:
			if flagt.moveDown(brd)==1:
				break
			os.system('clear')
			print(brd.retBoardStr())
			time.sleep(0.1)
		os.system('aplay sound/stage_clear.wav&')
		os.system('clear')
		print("STAGE CLEARED!" + '\n')

		print("SCORE: " + str(brd.score+bonus) + '\n')
		sys.exit()

	input = input_to(getch)
	#input = input("Key:")
	for cord in bul:
		if cord.liv == 1:
			cord.moveRight(brd)
	for enem in lenem:
		if enem.liv==1:
			if enem.dir ==1:
				enem.moveRighti(brd)
			else:
				enem.moveLefti(brd)
	

	for enem in Rem.remar:
		if enem.liv==1:
			enem.destroy(brd)
			os.system('aplay sound/stomp.wav&')
			brd.score+=500
	#input = sys.stdin.read(1)
	os.system('clear')
	print(brd.retBoardStr())
	if input is not None:
		if input == 'h':
			if mario.lvl == 3:
				os.system('aplay sound/fireball.wav')
				for i in range(0,4):
					bula = Bullets(1,1,'b')
					bula.setNewPosition(brd,mario.x+1,mario.y+4)
					bul.append(bula)
					for cord in bul:
						if cord.liv == 1:
							cord.moveRight(brd)


		if input != 'w' and input!= 'q' and input!='e' and input!= 'h':
			mario.move(input,brd)
			time.sleep(0.05)
		if input == 'w':
			if mario.lvl == 1:
				os.system('aplay sound/small_jump.wav&')
			else:
				os.system('aplay sound/big_jump.wav&')
			for i in range(0,7):
				if mario.moveUp(brd) == 1:
					break
				for cord in bul:
					if cord.liv == 1:
						cord.moveRight(brd)

				for enem in lenem:
					if enem.liv==1:
						if enem.dir ==1:
							enem.moveRighti(brd)
						else:
							enem.moveLefti(brd)

				
				for enem in Rem.remar:
					if enem.liv==1:
						enem.destroy(brd)
						os.system('aplay sound/stomp.wav&')
						brd.score+=500
				#tty.setcbreak(sys.stdin.fileno())
				#inut = sys.stdin.read(1)
				#mario.move(inut,brd)
				time.sleep(0.05)
				os.system('clear')
				print(brd.retBoardStr())

		if input == 'e':
			if mario.lvl == 1:
				os.system('aplay sound/small_jump.wav&')
			else:
				os.system('aplay sound/big_jump.wav&')
			for i in range(0,6):
				mario.moveUp(brd)
				mario.moveRight(brd)
				for cord in bul:
					if cord.liv == 1:
						cord.moveRight(brd)
				for enem in lenem:
					if enem.liv==1:
						if enem.dir ==1:
							enem.moveRighti(brd)
						else:
							enem.moveLefti(brd)
				
				
				
				for enem in Rem.remar:
					if enem.liv==1:
						enem.destroy(brd)
						os.system('aplay sound/stomp.wav&')
						brd.score+=500
				os.system('clear')
				print(brd.retBoardStr())
				time.sleep(0.05)

		if input == 'q':
			if mario.lvl == 1:
				os.system('aplay sound/small_jump.wav&')
			else:
				os.system('aplay sound/big_jump.wav&')
			for i in range(0,7):
				mario.moveLeft(brd)
				mario.moveUp(brd)
				for cord in bul:
					if cord.liv == 1:
						cord.moveRight(brd)
				for enem in lenem:
					if enem.liv==1:
						if enem.dir ==1:
							enem.moveRighti(brd)
						else:
							enem.moveLefti(brd)

				

				for enem in Rem.remar:
					if enem.liv==1:
						enem.destroy(brd)
						os.system('aplay sound/stomp.wav&')
						brd.score+=500
				os.system('clear')
				print(brd.retBoardStr())
				time.sleep(0.05)

		


	while True:
		if mario.moveDown(brd) == 1:
			break
		for enem in lenem:

			for cord in bul:
				if cord.liv == 1:
					cord.moveRight(brd)
			if enem.liv==1:
				if enem.dir ==1:
					enem.moveRighti(brd)
				else:
					enem.moveLefti(brd)

		
		for enem in Rem.remar:
			if enem.liv==1:
				enem.destroy(brd)
				os.system('aplay sound/stomp.wav&')
				brd.score+=500
		#tty.setcbreak(sys.stdin.fileno())
		#inpu = sys.stdin.read(1)
		#mario.move(inpu,brd)
		os.system('clear')
		print(brd.retBoardStr())
		time.sleep(0.05)

	if input == 'l':
		os.system('clear')
		os.system('pkill aplay')
		sys.exit()



	#time.sleep(0.02)