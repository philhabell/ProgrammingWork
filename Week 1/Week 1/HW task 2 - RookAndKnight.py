
def makeBoard(size):
	board=[]
	for i in range(size):
		board.append([])
		for j in range(size):
			board[-1].append(False)
	return board

def displayBoard(b):
	divider=("+---"*len(b))+"+"
	for row in b:
		print divider
		print "|"+"|".join({True:" X ",False:"   "}[i] for i in row)+"|"
	print divider

def setAppend(s,i):
	""" Add i to s unless i is already in s """
	if not i in s: s.append(i)

def inBoard(p,size):
	""" if point is valid for a board of given size, return True. Else return False """
	if 0<=p[0]<size and 0<=p[1]<size:
		return True
	else:
		return False

def pointShift(p,r,c):
	""" Return position of cell r,c away from given point p """
	return (p[0]+r,p[1]+c)

def appendIfInBounds(s,p,size):
	""" If point p is within the bounds of a board of given size, append to s unless it's already there """
	if inBoard(p,size):
		setAppend(s,p)

def queenSees(pos,size):
	""" Return a list of all squares "In view" of a queen in position pos on a board of size"""
	inView=[]
	#Row and column
	for i in range(size):
		#Column
		setAppend(inView,(i,pos[1]))
		#Row
		setAppend(inView,(pos[0],i))
		#Diagonals
		for r in [-1,1]:
			for c in [-1,1]:
				appendIfInBounds(inView, pointShift(pos,r*i,c*i), size)
	#Take out position of queen so she doesn't see herself...
	inView.remove(pos)
	return inView #outputs the list of queen positions 

def rookSees(pos,size):
	inView=[]
	#checks the horazontal for other rooks
	for i in range(size):
		setAppend(inView,(i,pos[1]))
		setAppend(inView,(pos[0],i))
	inView.remove(pos) # removes itself from list
	return inView #outputs the list of rook positions 

def knightSees(pos,size):
	inView=[]
	#lists on positions of knights 
	listA=[2,2,1,1,-1,-1,-2,-2]
	listB=[1,-1,2,-2,2,-2,1,-1]
	#loops through the list outputting knights to the inView list
	for i in range(size):
		appendIfInBounds(inView, pointShift(pos,listA[i],listB[i]),size)
		i += 2
	return inView #sends list to be outputted

def hasQueen(board, points):
	""" Returns True if any of the given points on the given board contain a queen """
	for p in points:
		if board[p[0]][p[1]]:
			return True
	return False

def cloneBoard(b,size):
	""" Make a copy of a board.Boards are objects (lists are objects) so a=b just makes them refer to the same object..."""
	c=makeBoard(size) #clone
	for i in range(size):
		for j in range(size):
			c[i][j]=b[i][j]
	return c
	
def fillBoardRecursion(board,row,size,piece):
	""" Given a board completed to given row, try all possible positions for next row and continue """
	if row==size:
		#Base case
		return board
	else:
		for col in range(size):
			if piece == "knight":
				#If we put a queen here, would it "see" another?
				if not hasQueen(board,knightSees((row,col),size)):
					b=cloneBoard(board,size)
					b[row][col]=True
					result= fillBoardRecursion(b,row+1,size,piece)
					if result!=False:
						return result
			elif piece == "queen":
				if not hasQueen(board,queenSees((row,col),size)):
					b=cloneBoard(board,size)
					b[row][col]=True
					result= fillBoardRecursion(b,row+1,size,piece)
					if result!=False:
						return result
			elif piece == "rook":
				if not hasQueen(board,rookSees((row,col),size)):
					b=cloneBoard(board,size)
					b[row][col]=True
					result= fillBoardRecursion(b,row+1,size,piece)
					if result!=False:
						return result
		return False #Failed at this point, so return False

boardSize = 8
print "Queen:"
b=makeBoard(boardSize)
b=fillBoardRecursion(b,0,boardSize,"queen")
displayBoard(b)
print "\n \nRook:"
b=makeBoard(boardSize)
b=fillBoardRecursion(b,0,boardSize,"rook")
displayBoard(b)
print  "\n \nKnigh:"
b=makeBoard(boardSize)
b=fillBoardRecursion(b,0,boardSize,"knight")
displayBoard(b)

""" #this allows user to what piece they want
def start():
	piece = raw_input ("Enter Piece: ")
	if piece == "queen" or "rook" or "knight":
		b=makeBoard(boardSize)
		b=fillBoardRecursion(b,0,boardSize,piece)
		displayBoard(b)
	else:
		start()
"""