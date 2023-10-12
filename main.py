import random, collections, time, sys, copy
import pygame as pg
from BFS import bfs
pg.font.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60
Time = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

LIST_BACKGROUND = [pg.transform.scale(pg.image.load("assets/background/" + str(i) + ".jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT)) for i in range(10)]

BOARD_ROW = 9 #7
BOARD_COLUMN = 14 #12
NUM_TILE_ON_BOARD = 21
NUM_SAME_TILE = 4

TILE_WIDTH = 50
TILE_HEIGHT = 55                                                                                            
MARGIN_X = (SCREEN_WIDTH - TILE_WIDTH * BOARD_COLUMN) // 2
MARGIN_Y = (SCREEN_HEIGHT - TILE_HEIGHT * BOARD_ROW) // 2

NUM_TILE = 33
LIST_TILE = [0] * (NUM_TILE + 1)
for i in range(1, NUM_TILE + 1): LIST_TILE[i] = pg.transform.scale(pg.image.load("assets/images/section" + str(i) + ".png"), (TILE_WIDTH, TILE_HEIGHT))
list_tile[5]

# GAME_TIME = 240
# HINT_TIME = 20

# #time bar
# TIME_BAR_WIDTH = 300
# TIME_BAR_HEIGHT = 30
# TIME_BAR_POS = ((SCREEN_WIDTH - TIME_BAR_WIDTH) // 2, (MARGIN_Y - TIME_BAR_HEIGHT) // 2 + 15)
# TIME_ICON = pg.transform.scale(pg.image.load("assets/images/section36.png"), (TILE_WIDTH, TILE_HEIGHT))

# MAX_LEVEL = 5

# LIVES_IMAGE = pg.transform.scale(pg.image.load("assets/images/section35.png"), (TILE_WIDTH, TILE_HEIGHT))

# FONT_COMICSANSMS = pg.font.SysFont('comicsansms', 50)
# FONT_TIMENEWROMAN = pg.font.SysFont('timesnewroman', 50)

# # start screen
# START_SCREEN_BACKGOUND = pg.transform.scale(pg.image.load("assets/background/3.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))



def main():
	pg.init()
	level = 1
	lives = 3
	# start_screen()
	# while level <= MAX_LEVEL:
	random.shuffle(LIST_BACKGROUND)
	playing(level, lives)
	  # level += 1
	  # pg.time.wait(1000)
	# end_screen()

def playing(level, lives):

	background = LIST_BACKGROUND[0] # get random background
	board = get_random_board() # get ramdom board of game

	# mouse_x, mouse_y = 0, 0
	# clicked_tiles = [] # store index cards clicked
	# hint = get_hint(board)

	# last_time_get_point = time.time()
	# start_time = time.time()
	# bouns_time = 0

	while True:
		screen.blit(background, (0, 0)) # set background
		Time.tick(FPS)
		draw_board(board)
		# draw_lives(lives)

		# draw_clicked_tiles(board, clicked_tiles)
		# mouse_clicked = False

		# # check time
		# if time.time() - start_time > GAME_TIME + bouns_time: 
		# 	lives -= 1 
		# 	if lives == 0: level = MAX_LEVEL + 1 # game over
		# 	return
		
		# if time.time() - last_time_get_point > HINT_TIME: draw_hint(hint)
		# # check event
		for event in pg.event.get():
			if event.type == pg.QUIT: pg.quit(), sys.exit()
		# 	if event.type == pg.MOUSEMOTION:
		# 		mouse_x, mouse_y = event.pos
		# 	if event.type == pg.MOUSEBUTTONDOWN:
		# 		mouse_x, mouse_y = event.pos
		# 		mouse_clicked = True
		# 	if event.type == pg.KEYUP:
		# 		if event.key == pg.K_k: # use key k to hack game
		# 				tile1_i, tile1_j = hint[0][0], hint[0][1]
		# 				tile2_i, tile2_j = hint[1][0], hint[1][1]
		# 				board[tile1_i][tile1_j] = 0
		# 				board[tile2_i][tile2_j] = 0
		# 				bouns_time += 1
		# 				update_difficulty(board, level, tile1_i, tile1_j, tile2_i, tile2_j)

		# 				if is_level_complete(board): return

		# 				if not(board[tile1_i][tile1_j] != 0 and bfs(board, tile1_i, tile1_j, tile2_i, tile2_j)):
		# 					hint = get_hint(board)
		# 					while not hint:
		# 						pg.time.wait(100)
		# 						reset_board(board)
		# 						hint = get_hint(board)
		# #update
		# tile_i, tile_j = get_index_at_mouse(mouse_x, mouse_y)
		# if tile_i != None and tile_j != None and board[tile_i][tile_j] != 0:
		# 	draw_border_tile(board, tile_i, tile_j)
		# 	if mouse_clicked:
		# 		mouse_clicked = False
		# 		clicked_tiles.append((tile_i, tile_j))
		# 		draw_clicked_tiles(board, clicked_tiles)
		# 		if len(clicked_tiles) > 1: # 2 cards was clicked 
		# 			path = bfs(board, clicked_tiles[0][0], clicked_tiles[0][1], tile_i, tile_j)
		# 			if path:
		# 				# delete the same card
		# 				board[clicked_tiles[0][0]][clicked_tiles[0][1]] = 0
		# 				board[tile_i][tile_j] = 0
		# 				draw_path(path)

		# 				bouns_time += 1
		# 				last_time_get_point = time.time() # count time hint
		# 				# if level > 1, upgrade difficulty by moving cards 
		# 				update_difficulty(board, level, clicked_tiles[0][0], clicked_tiles[0][1], tile_i, tile_j)
		# 				if is_level_complete(board):
		# 					return
		# 				# if hint got by player
		# 				if not(board[hint[0][0]][hint[0][1]] != 0 and bfs(board, hint[0][0], hint[0][1], hint[1][0], hint[1][1])):
		# 					hint = get_hint(board)
		# 					while not hint:
		# 						pg.time.wait(100)
		# 						reset_board(board)
		# 						hint = get_hint(board)
		# 			#reset
		# 			clicked_tiles = []
		pg.display.flip()

def get_random_board():
	list_index_card = list(range(1, NUM_TILE + 1)) #21
	random.shuffle(list_index_card)
	list_index_card = list_index_card[:NUM_TILE_ON_BOARD] * NUM_SAME_TILE #84
	random.shuffle(list_index_card)
	board = [[0 for _ in range(BOARD_COLUMN)]for _ in range(BOARD_ROW)]
	k = 0
	for i in range(1, BOARD_ROW - 1):
		for j in range(1, BOARD_COLUMN - 1):
			board[i][j] = list_index_card[k]
			k += 1
	return board

def get_left_top_coords(i, j): # get left top coords of card from index i, j
	x = j * TILE_WIDTH + MARGIN_X
	y = i * TILE_HEIGHT + MARGIN_Y
	return x, y

def get_center_coords(i, j): # get center coords of card from index i, j
	x, y = get_left_top_coords(i, j)
	return x + TILE_WIDTH // 2, y + TILE_HEIGHT // 2

def get_index_at_mouse(x, y): # get index of card at mouse clicked from coords x, y
	if x < MARGIN_X or x > SCREEN_WIDTH - MARGIN_X or y < MARGIN_Y or y > SCREEN_HEIGHT - MARGIN_Y:
		return None, None
	return (y - MARGIN_Y) // TILE_HEIGHT, (x - MARGIN_X) // TILE_WIDTH

def draw_board(board):
	for i in range(1, BOARD_ROW - 1):
		for j in range(1, BOARD_COLUMN - 1):
			if board[i][j] != 0:
				screen.blit(LIST_TILE[board[i][j]], get_left_top_coords(i, j))

def draw_clicked_tiles(board, clicked_tiles):
	for i, j in clicked_tiles:
		x, y = get_left_top_coords(i, j)
		darkImage = LIST_TILE[board[i][j]].copy()
		darkImage.fill((60, 60, 60), special_flags = pg.BLEND_RGB_SUB)
		screen.blit(darkImage, (x, y))

def draw_border_tile(board, i, j):
	x, y = get_left_top_coords(i, j)
	pg.draw.rect(screen, (0, 0, 255),(x - 1, y - 3, TILE_WIDTH + 4, TILE_HEIGHT + 4), 2)

def draw_path(path):
	for i in range(len(path) - 1):
		start_pos = (get_center_coords(path[i][0], path[i][1]))
		end_pos = (get_center_coords(path[i + 1][0], path[i + 1][1]))
		pg.draw.line(screen, 'red', start_pos, end_pos, 4)
		pg.display.update()
	pg.time.wait(400)

def get_hint(board):
	hint = [] # stories two tuple
	tiles_location = collections.defaultdict(list)
	for i in range(BOARD_ROW):
		for j in range(BOARD_COLUMN):
			if board[i][j]:
				tiles_location[board[i][j]].append((i, j))
	for i in range(BOARD_ROW):
		for j in range(BOARD_COLUMN):
			if board[i][j]:
				for o in tiles_location[board[i][j]]:
					if o != (i, j) and bfs(board, i, j, o[0], o[1]):
						hint.append((i, j))
						hint.append(o)
						return hint
	return []

def draw_hint(hint):
	for i, j in hint:
		x, y = get_left_top_coords(i, j)
		pg.draw.rect(screen, (0, 255, 0),(x - 1, y - 2, TILE_WIDTH + 4, TILE_HEIGHT + 4), 2)

def draw_time_bar(start_time, bouns_time):
	screen.blit(TIME_ICON, (TIME_BAR_POS[0] + TIME_BAR_WIDTH + 10, TIME_BAR_POS[1] - 10))
	pg.draw.rect(screen, 'white', (TIME_BAR_POS[0], TIME_BAR_POS[1], TIME_BAR_WIDTH, TIME_BAR_HEIGHT), 2)
	timeOut = 1 - (time.time() - start_time - bouns_time) / GAME_TIME # ratio between remaining time and total time
	innerPos = (TIME_BAR_POS[0] + 2, TIME_BAR_POS[1] + 2) # add border 2
	innerSize = (TIME_BAR_WIDTH * timeOut - 4, TIME_BAR_HEIGHT - 4) # sub border
	pg.draw.rect(screen, 'green', (innerPos, innerSize))

def is_level_complete(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] != 0: return False
	return True

def update_difficulty(board, level, tile1_i, tile1_j, tile2_i, tile2_j):
	if level == 2: #all card move up
		for j in (tile1_j, tile2_j):
			new_column = [0]
			for i in range(BOARD_ROW):
				if board[i][j] != 0:
					new_column.append(board[i][j])
			while(len(new_column) < BOARD_ROW): new_column.append(0)
			for k in range(BOARD_ROW):
				board[k][j] = new_column[k]
	if level == 3: #all card move down
		for j in (tile1_j, tile2_j):
			new_column = []
			for i in range(BOARD_ROW):
				if board[i][j] != 0:
					new_column.append(board[i][j])
			while(len(new_column) < BOARD_ROW - 1): new_column = [0] + new_column
			new_column.append(0)
			for k in range(BOARD_ROW):
				board[k][j] = new_column[k]
	if level == 4: #all card move left
		for i in (tile1_i, tile2_i):
			new_row = [0]
			for j in range(BOARD_COLUMN):
				if board[i][j] != 0:
					new_row.append(board[i][j])
			while(len(new_row) < BOARD_COLUMN): new_row.append(0)
			for k in range(BOARD_COLUMN):
				board[i][k] = new_row[k]
	if level == 5: #all card move right
		for i in (tile1_i, tile2_i):
			new_row = []
			for j in range(BOARD_COLUMN):
				if board[i][j] != 0:
					new_row.append(board[i][j])
			while len(new_row) < BOARD_COLUMN - 1: new_row = [0] + new_row
			new_row.append(0)
			for k in range(BOARD_COLUMN):
				board[i][k] = new_row[k]

def draw_lives(lives):
	screen.blit(LIVES_IMAGE, (10, 10))
	lives_count = FONT_COMICSANSMS.render(str(lives), True, 'white')
	live_count_rect = lives_count.get_rect()
	screen.blit(lives_count, (70, 0, 50, 55))

def start_screen():
	while True:
		Time.tick(FPS)
		screen.blit(START_SCREEN_BACKGOUND, (0, 0))
		new_game_text = FONT_TIMENEWROMAN.render("NEW GAME", True, 'white')
		new_game_rect = new_game_text.get_rect()
		new_game_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
		screen.blit(new_game_text, new_game_rect)
		pg.draw.rect(screen, 'white', new_game_rect, 4)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
		pg.display.flip()

def reset_board(board):
	current_tiles = []
	for i in range(BOARD_ROW):
		for j in range(BOARD_COLUMN):
			if board[i][j]: current_tiles.append(board[i][j])
	tmp = current_tiles[:]
	while tmp == current_tiles:
		random.shuffle(current_tiles)
	k = 0
	for i in range(BOARD_ROW):
		for j in range(BOARD_COLUMN):
			if board[i][j]:
				board[i][j] = current_tiles[k]
				k += 1
	return board

if __name__ == '__main__':
	main()