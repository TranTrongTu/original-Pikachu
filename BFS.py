<<<<<<< HEAD
def bfs(board, card1I, card1J, card2I, card2J):
	def backtrace(parent, card1I, card1J, card2I, card2J):
		start = (card1I, card1J, 0, 'noDirection')
		end = None
		for node in parent:
			if node[:2] == (card2I, card2J): end = node
		path = [end]
		while path[-1] != start:
			path.append(parent[path[-1]])
		path.reverse()
		for p in path:
			p = p[:2]
		return path

	if board[card1I][card1J] != board[card2I][card2J]: return []
	n = len(board)
	m = len(board[0])

	import queue
	visited = set()
	visited.add((card1I, card1J, 0, 'noDirection'))
	parent = {}
	q = queue.Queue()
	q.put((card1I, card1J, 0, 'noDirection')) # indexI, indexJ, number of turns, direction

	while not q.empty():
		i, j, numTurn, direction = q.get()
		if (i, j) != (card1I, card1J) and (i, j) == (card2I, card2J): # founded the way
			return backtrace(parent, card1I, card1J, card2I, card2J)
		directions = {(i - 1, j) : 'up', (i + 1, j) : 'down', (i, j + 1) : 'right', (i, j - 1) : 'left'}
		for idxI, idxJ in directions:
			nextDirection = directions[(idxI, idxJ)]
			if idxI >= 0 and idxI < n and idxJ >= 0 and idxJ < m and (board[idxI][idxJ] == 0 or (idxI, idxJ) == (card2I, card2J)):
				if direction == 'noDirection' or (direction == nextDirection and (idxI, idxJ, numTurn, nextDirection) not in visited):
					q.put((idxI, idxJ, numTurn, nextDirection))
					visited.add((idxI, idxJ, numTurn, nextDirection))
					parent[(idxI, idxJ, numTurn, nextDirection)] = (i, j, numTurn, direction)
				elif direction != nextDirection and numTurn < 2 and (idxI, idxJ, numTurn + 1, nextDirection) not in visited:
					q.put((idxI, idxJ, numTurn + 1, nextDirection))
					visited.add((idxI, idxJ, numTurn + 1, nextDirection))
					parent[(idxI, idxJ, numTurn + 1, nextDirection)] = (i, j, numTurn, direction)
=======
def bfs(board, card1I, card1J, card2I, card2J):
	def backtrace(parent, card1I, card1J, card2I, card2J):
		start = (card1I, card1J, 0, 'noDirection')
		end = None
		for node in parent:
			if node[:2] == (card2I, card2J): end = node
		path = [end]
		while path[-1] != start:
			path.append(parent[path[-1]])
		path.reverse()
		for p in path:
			p = p[:2]
		return path

	if board[card1I][card1J] != board[card2I][card2J]: return []
	n = len(board)
	m = len(board[0])

	import queue
	visited = set()
	visited.add((card1I, card1J, 0, 'noDirection'))
	parent = {}
	q = queue.Queue()
	q.put((card1I, card1J, 0, 'noDirection')) # indexI, indexJ, number of turns, direction

	while not q.empty():
		i, j, numTurn, direction = q.get()
		if (i, j) != (card1I, card1J) and (i, j) == (card2I, card2J): # founded the way
			return backtrace(parent, card1I, card1J, card2I, card2J)
		directions = {(i - 1, j) : 'up', (i + 1, j) : 'down', (i, j + 1) : 'right', (i, j - 1) : 'left'}
		for idxI, idxJ in directions:
			nextDirection = directions[(idxI, idxJ)]
			if idxI >= 0 and idxI < n and idxJ >= 0 and idxJ < m and (board[idxI][idxJ] == 0 or (idxI, idxJ) == (card2I, card2J)):
				if direction == 'noDirection' or (direction == nextDirection and (idxI, idxJ, numTurn, nextDirection) not in visited):
					q.put((idxI, idxJ, numTurn, nextDirection))
					visited.add((idxI, idxJ, numTurn, nextDirection))
					parent[(idxI, idxJ, numTurn, nextDirection)] = (i, j, numTurn, direction)
				elif direction != nextDirection and numTurn < 2 and (idxI, idxJ, numTurn + 1, nextDirection) not in visited:
					q.put((idxI, idxJ, numTurn + 1, nextDirection))
					visited.add((idxI, idxJ, numTurn + 1, nextDirection))
					parent[(idxI, idxJ, numTurn + 1, nextDirection)] = (i, j, numTurn, direction)
>>>>>>> b4ad1b8a753ee39e5edc5f4d9156196a0efd2257
	return []