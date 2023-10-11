import random, collections, time, sys, copy
import pygame as pg
from BFS import bfs
pg.font.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 10
Time = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

LIST_BACKGROUND = [pg.transform.scale(pg.image.load("assets/background/" + str(i) + ".jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT)) for i in range(10)]

BOARD_ROW = 9 #7
BOARD_COLUMN = 14 #12
NUM_CARD_ON_BOARD = 21
NUM_SAME_CARD = 4

CARD_WIDTH = 50
CARD_HEIGHT = 55

MARGIN_X = (SCREEN_WIDTH - CARD_WIDTH * BOARD_COLUMN) // 2
MARGIN_Y = (SCREEN_HEIGHT - CARD_HEIGHT * BOARD_ROW) // 2


NUM_CARD = 33
LIST_CARD = [0] * (NUM_CARD + 1)
for i in range(1, NUM_CARD + 1): LIST_CARD[i] = pg.transform.scale(pg.image.load("assets/images/section" + str(i) + ".png"), (CARD_WIDTH, CARD_HEIGHT))

GAME_TIME = 240
HINT_TIME = 20

#time bar
TIME_BAR_WIDTH = 300
TIME_BAR_HEIGHT = 30
TIME_BAR_POS = ((SCREEN_WIDTH - TIME_BAR_WIDTH) // 2, (MARGIN_Y - TIME_BAR_HEIGHT) // 2 + 15)
TIME_ICON = pg.transform.scale(pg.image.load("assets/images/section36.png"), (CARD_WIDTH, CARD_HEIGHT))

MAX_LEVEL = 5

LIVES_IMAGE = pg.transform.scale(pg.image.load("assets/images/section35.png"), (CARD_WIDTH, CARD_HEIGHT))

FONT_COMICSANSMS = pg.font.SysFont('comicsansms', 50)
FONT_TIMENEWROMAN = pg.font.SysFont('timesnewroman', 50)

# start screen
START_SCREEN_BACKGOUND = pg.transform.scale(pg.image.load("assets/background/3.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))



def main():
	pg.init()
	global level, lives
	level = 1
	lives = 3
	# startScreen()
	while level <= MAX_LEVEL:
	  random.shuffle(LIST_BACKGROUND)
	  gameRunning()
	  level += 1
	  pg.time.wait(1000)

def gameRunning():
	global level, lives

	background = LIST_BACKGROUND[0] # get random background
	board = getRandomBoard() # get ramdom board of game

	mouseX, mouseY = 0, 0
	firstSelected = None # store index i, j of first card selected
	clickedCards = [] # store index cards clicked
	hint = getHint(board)

	lastGetPoint = time.time()
	startTime = time.time()
	bonusTime = 0

	while True:
		screen.blit(background, (0, 0)) # set background
		Time.tick(FPS)

		drawBoard(board)
		drawTimeBar(startTime, bonusTime)
		drawLives(lives)

		drawClickedCard(board, clickedCards)
		mouseClicked = False

		if time.time() - startTime > GAME_TIME + bonusTime: 
			lives -= 1 
			if lives == 0:	level = MAX_LEVEL + 1 # game over
			return
		
		if time.time() - lastGetPoint > HINT_TIME: drawHint(hint)

		for event in pg.event.get():
			if event.type == pg.QUIT: pg.quit(), sys.exit()
			if event.type == pg.MOUSEMOTION:
				mouseX, mouseY = event.pos
			if event.type == pg.MOUSEBUTTONDOWN:
				mouseX, mouseY = event.pos
				mouseClicked = True
			
			if event.type == pg.KEYUP:
				if event.key == pg.K_n: # use key n to hack game
					try:
						card1I, card1J = hint[0][0], hint[0][1]
						card2I, card2J = hint[1][0], hint[1][1]
						board[card1I][card1J] = 0
						board[card2I][card2J] = 0
						bonusTime += 1
						updateLevelDifficul(board, level, card1I, card1J, card2I, card2J)

						if isLevelComplete(board):
							drawBoard(board)
							pg.display.update()
							return
						if not(board[card1I][card1J] != 0 and bfs(board, card1I, card1J, card2I, card2J)):
							hint = getHint(board)
					except: print(-1)

		cardI, cardJ = getIndexAtMouse(mouseX, mouseY)
		if cardI != None and cardJ != None and board[cardI][cardJ] != 0:
			drawBorderCard(board, cardI, cardJ)
			
			if mouseClicked:
				mouseClicked = False
				clickedCards.append((cardI, cardJ))
				drawClickedCard(board, clickedCards)
				if firstSelected == None: firstSelected = (cardI, cardJ)
				else:
					path = bfs(board, firstSelected[0], firstSelected[1], cardI, cardJ)
					if path:
						board[firstSelected[0]][firstSelected[1]] = 0
						board[cardI][cardJ] = 0
						drawPath(path)

						bonusTime += 1
						lastGetPoint = time.time()
						# if level > 1, upgrade difficulty by moving cards 
						updateLevelDifficul(board, level, firstSelected[0], firstSelected[1], cardI, cardJ)
						if isLevelComplete(board):
							drawBoard(board)
							pg.display.update()
							return
						# if hint got by player
						if not(board[hint[0][0]][hint[0][1]] != 0 and bfs(board, hint[0][0], hint[0][1], hint[1][0], hint[1][1])):
							hint = getHint(board)

					firstSelected = None
					clickedCards = []
		pg.display.flip()

def getRandomBoard():
	listIndexCard = list(range(1, NUM_CARD + 1))
	random.shuffle(listIndexCard)
	listIndexCard = listIndexCard[:NUM_CARD_ON_BOARD] * NUM_SAME_CARD
	random.shuffle(listIndexCard)
	board = [[0 for _ in range(BOARD_COLUMN)]for _ in range(BOARD_ROW)]
	k = 0
	for i in range(1, BOARD_ROW - 1):
		for j in range(1, BOARD_COLUMN - 1):
			board[i][j] = listIndexCard[k]
			k += 1
	return board

def getLeftTopCoords(i, j): # get left top coords of card from index i, j
	x = j * CARD_WIDTH + MARGIN_X
	y = i * CARD_HEIGHT + MARGIN_Y
	return x, y

def getCenterCoords(i, j): # get center coords of card from index i, j
	x, y = getLeftTopCoords(i, j)
	return x + CARD_WIDTH // 2, y + CARD_HEIGHT // 2

def getIndexAtMouse(x, y): # get index of card at mouse clicked from coords x, y
	if x < MARGIN_X or x > SCREEN_WIDTH - MARGIN_X or y < MARGIN_Y or y > SCREEN_HEIGHT - MARGIN_Y:
		return None, None
	return (y - MARGIN_Y) // CARD_HEIGHT, (x - MARGIN_X) // CARD_WIDTH

def drawBoard(board):
	for i in range(1, BOARD_ROW - 1):
		for j in range(1, BOARD_COLUMN - 1):
			if board[i][j] != 0:
				screen.blit(LIST_CARD[board[i][j]], getLeftTopCoords(i, j))

def drawClickedCard(board, clickedCards):
	for i, j in clickedCards:
		x, y = getLeftTopCoords(i, j)
		darkImage = LIST_CARD[board[i][j]].copy()
		darkImage.fill((60, 60, 60), special_flags = pg.BLEND_RGB_SUB)
		screen.blit(darkImage, (x, y))

def drawBorderCard(board, i, j):
	x, y = getLeftTopCoords(i, j)
	pg.draw.rect(screen, (0, 0, 255),(x - 1, y - 3, CARD_WIDTH + 4, CARD_HEIGHT + 4), 2)

def drawPath(path):
	for i in range(len(path) - 1):
		startPos = (getCenterCoords(path[i][0], path[i][1]))
		endPos = (getCenterCoords(path[i + 1][0], path[i + 1][1]))
		pg.draw.line(screen, 'red', startPos, endPos, 4)
		pg.display.update()
	pg.time.wait(400)

def getHint(board):
	hint = [] # stories two tuple
	cardLocation = collections.defaultdict(list)
	for i in range(BOARD_ROW):
		for j in range(BOARD_COLUMN):
			if board[i][j] != 0:
				cardLocation[board[i][j]].append((i, j))
	for i in range(BOARD_ROW):
		for j in range(BOARD_COLUMN):
			if board[i][j] != 0:
				for o in cardLocation[board[i][j]]:
					if o != (i, j) and bfs(board, i, j, o[0], o[1]):
						hint.append((i, j))
						hint.append(o)
						return hint
	return []

def drawHint(hint):
	for i, j in hint:
		x, y = getLeftTopCoords(i, j)
		pg.draw.rect(screen, (0, 255, 0),(x - 1, y - 2, CARD_WIDTH + 4, CARD_HEIGHT + 4), 2)

def drawTimeBar(startTime, bonusTime):
	screen.blit(TIME_ICON, (TIME_BAR_POS[0] + TIME_BAR_WIDTH + 10, TIME_BAR_POS[1] - 10))
	pg.draw.rect(screen, 'white', (TIME_BAR_POS[0], TIME_BAR_POS[1], TIME_BAR_WIDTH, TIME_BAR_HEIGHT), 2)
	timeOut = 1 - (time.time() - startTime - bonusTime) / GAME_TIME # ratio between remaining time and total time
	innerPos = (TIME_BAR_POS[0] + 2, TIME_BAR_POS[1] + 2) # add border 2
	innerSize = (TIME_BAR_WIDTH * timeOut - 4, TIME_BAR_HEIGHT - 4) # sub border
	pg.draw.rect(screen, 'green', (innerPos, innerSize))

def isLevelComplete(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] != 0: return False
	return True

def updateLevelDifficul(board, level, card1I, card1J, card2I, card2J):
	if level == 2: #all card move up
		for j in (card1J, card2J):
			newColumn = [0]
			for i in range(BOARD_ROW):
				if board[i][j] != 0:
					newColumn.append(board[i][j])
			while(len(newColumn) < BOARD_ROW): newColumn.append(0)
			for k in range(BOARD_ROW):
				board[k][j] = newColumn[k]
	if level == 3: #all card move down
		for j in (card1J, card2J):
			newColumn = []
			for i in range(BOARD_ROW):
				if board[i][j] != 0:
					newColumn.append(board[i][j])
			while(len(newColumn) < BOARD_ROW - 1): newColumn = [0] + newColumn
			newColumn.append(0)
			for k in range(BOARD_ROW):
				board[k][j] = newColumn[k]
	if level == 4: #all card move left
		for i in (card1I, card2I):
			newRow = [0]
			for j in range(BOARD_COLUMN):
				if board[i][j] != 0:
					newRow.append(board[i][j])
			while(len(newRow) < BOARD_COLUMN): newRow.append(0)
			for k in range(BOARD_COLUMN):
				board[i][k] = newRow[k]
	if level == 5: #all card move right
		for i in (card1I, card2I):
			newRow = []
			for j in range(BOARD_COLUMN):
				if board[i][j] != 0:
					newRow.append(board[i][j])
			while(len(newRow) < BOARD_COLUMN - 1): newRow = [0] + newRow
			newRow.append(0)
			for k in range(BOARD_COLUMN):
				board[i][k] = newRow[k]

def drawLives(lives):
	screen.blit(LIVES_IMAGE, (10, 10))
	livesCount = FONT_COMICSANSMS.render(str(lives), True, 'white')
	liveCountRect = livesCount.get_rect()
	screen.blit(livesCount, (70, 0, 50, 55))

def startScreen():
	while True:
		Time.tick(FPS)
		screen.blit(START_SCREEN_BACKGOUND, (0, 0))
		newGameText = FONT_TIMENEWROMAN.render("NEW GAME", True, 'white')
		newGameRect = newGameText.get_rect()
		newGameRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
		screen.blit(newGameText, newGameRect)
		pg.draw.rect(screen, 'white', newGameRect, 4)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
		pg.display.flip()

def resetBoard(board):
	currentCard = []
	for i in range(BOARD_ROW):
		for j in range(BOARD_COLUMN):
			if board[i][j]: currentCard.append(board[i][j])
	tmp = currentCard[:]
	while tmp != currentCard:
		random.shuffle(currentCard)
	k = 0
	for i in range(BOARD_ROW):
		for j in range(BOARD_COLUMN):
			if board[i][j]:
				board[i][j] = currentCard[k]
				k += 1
	return board

if __name__ == '__main__':
	main()



