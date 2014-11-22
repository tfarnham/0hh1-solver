# Taylor Farnham
# November 22, 2014
# Solver for 0hh1.com puzzles

### INSTRUCTIONS
# Set 'n' to the game size
# Fill the starting condition into the gameboard
# 0 - Empty tile
# 1 - Red Tile
# 2 - Blue Tile
n = 10 # Make sure this is set to the grid dimension (n x n)
showAllSteps = True # Show all steps (True) or just solution (False)

import numpy
gameboard=numpy.zeros([n,n])

### Fill in your gameboard below

# gameboard[0]=[0,0,0,0]
# gameboard[1]=[0,0,0,0]
# gameboard[2]=[0,0,0,0]
# gameboard[3]=[0,0,0,0]

# gameboard[0]=[0,0,0,0,0,0]
# gameboard[1]=[0,0,0,0,0,0]
# gameboard[2]=[0,0,0,0,0,0]
# gameboard[3]=[0,0,0,0,0,0]
# gameboard[4]=[0,0,0,0,0,0]
# gameboard[5]=[0,0,0,0,0,0]

# gameboard[0]=[0,0,0,0,0,0,0,0]
# gameboard[1]=[0,0,0,0,0,0,0,0]
# gameboard[2]=[0,0,0,0,0,0,0,0]
# gameboard[3]=[0,0,0,0,0,0,0,0]
# gameboard[4]=[0,0,0,0,0,0,0,0]
# gameboard[5]=[0,0,0,0,0,0,0,0]
# gameboard[6]=[0,0,0,0,0,0,0,0]
# gameboard[7]=[0,0,0,0,0,0,0,0]

# gameboard[0]=[0,0,0,0,0,0,0,0,0,0]
# gameboard[1]=[0,0,0,0,0,0,0,0,0,0]
# gameboard[2]=[0,0,0,0,0,0,0,0,0,0]
# gameboard[3]=[0,0,0,0,0,0,0,0,0,0]
# gameboard[4]=[0,0,0,0,0,0,0,0,0,0]
# gameboard[5]=[0,0,0,0,0,0,0,0,0,0]
# gameboard[6]=[0,0,0,0,0,0,0,0,0,0]
# gameboard[7]=[0,0,0,0,0,0,0,0,0,0]
# gameboard[8]=[0,0,0,0,0,0,0,0,0,0]
# gameboard[9]=[0,0,0,0,0,0,0,0,0,0]

### Uncomment these lines for example

# gameboard[0]=[0,1,0,0,0,1,0,1,0,1]
# gameboard[1]=[0,0,0,1,1,0,0,0,1,0]
# gameboard[2]=[2,0,0,0,1,1,0,2,0,0]
# gameboard[3]=[0,0,0,0,0,0,0,0,0,0]
# gameboard[4]=[0,0,2,0,2,2,0,0,0,2]
# gameboard[5]=[0,0,0,0,0,0,0,0,1,0]
# gameboard[6]=[0,0,0,0,2,0,0,2,0,0]
# gameboard[7]=[0,0,0,1,0,0,0,2,1,0]
# gameboard[8]=[2,0,1,0,0,2,0,0,0,0]
# gameboard[9]=[0,0,1,0,2,0,0,0,0,1]

### Do not modify beneath this line ###

#Check if there are three in a row in each orientation
def checkUp(gameboard,y,x):
	if y-1 <0 or y-2<0:
		return False

	if gameboard[y][x]==gameboard[y-2][x] and gameboard[y][x]==gameboard[y-1][x]:
		return True
	else:
		return False
def checkVert(gameboard,y,x):
	if y-1<0 or y+1==len(gameboard):
		return False
	if gameboard[y][x]==gameboard[y-1][x] and gameboard[y][x]==gameboard[y+1][x]:
		return True
	else:
		return False
def checkDown(gameboard,y,x):
	if y+1 ==len(gameboard) or y+2 == len(gameboard):
		return False
	if gameboard[y][x]==gameboard[y+2][x] and gameboard[y][x]==gameboard[y+1][x]:
		return True
	else:
		return False
def checkRight(gameboard,y,x):
	if x+1==len(gameboard) or x+2==len(gameboard):
		return False
	if gameboard[y][x]==gameboard[y][x+1] and gameboard[y][x]==gameboard[y][x+2]:
		return True
	else:
		return False
def checkHoriz(gameboard,y,x):
	if x-1<0 or x+1==len(gameboard):
		return False
	if gameboard[y][x]==gameboard[y][x-1] and gameboard[y][x]==gameboard[y][x+1]:
		return True
	else:
		return False
def checkLeft(gameboard,y,x):
	if x-1<0 or x-2 <0:
		return False
	if gameboard[y][x]==gameboard[y][x-1] and gameboard[y][x]==gameboard[y][x-2]:
		return True
	else:
		return False

#Checks all three in a row criteria for a given point (y,x)
def checkThreeInLine(gameboard,y,x):

	return checkUp(gameboard,y,x) or checkVert(gameboard,y,x) or checkDown(gameboard,y,x) or checkRight(gameboard,y,x) or checkHoriz(gameboard,y,x) or checkLeft(gameboard,y,x)
#Iterates through all points to check for three in a row
#Fills square if opposite color would form three in a row
def checkThrees(gameboard):
	"""If position is undefined, test a color and see if violates three in a line. If so, set to other color. Then switch."""
	for x in range(0,n):
		for y in range(0,n):
			if gameboard[y][x]==0:
				#test with color 1
				gameboardTest=gameboard.copy()
				gameboardTest[y][x]=1
				if checkThreeInLine(gameboardTest,y,x):
					gameboard[y][x]=2
				else:
					gameboardTest[y][x]=2
					if checkThreeInLine(gameboardTest,y,x):
						gameboard[y][x]=1

#Checks to see if a row or column is full of one color
#Fills remaining squares with other color
def checkRow(gameboard,y):
	count1 = 0
	count2 = 0
	for col in gameboard[y]:
		if col ==1:
			count1 +=1
		elif col ==2:
			count2 +=1
	if count1 == n/2:
		for x in range(0,n):
			if gameboard[y][x] == 0:
				gameboard[y][x]=2
	elif count2 == n/2:
		for x in range(0,n):
			if gameboard[y][x] == 0:
				gameboard[y][x]=1		
def checkCol(gameboard,x):
	count1 = 0
	count2 = 0
	for row in gameboard[:,x]:
		if row ==1:
			count1 +=1
		elif row ==2:
			count2 +=1
	if count1 == n/2:
		for y in range(0,n):
			if gameboard[y][x] == 0:
				gameboard[y][x]=2
	elif count2 == n/2:
		for y in range(0,n):
			if gameboard[y][x] == 0:
				gameboard[y][x]=1		
#Iterates through all rows and columns to check for equality
def checkRowAndCol(gameboard):
	for index in range(0,n):
		checkRow(gameboard,index)
		checkCol(gameboard,index)

#Checks each row or column with two empty squares
#If filling empty squares makes it equal to another row/col, fills with opposite
def checkDistinctRow(gameboard):
	#for every row with two remaining, try setting it equal to [1,2], see if it fails
	gameboardTest=gameboard.copy()
	for rowIndex in range(0,n):
		if gameboardTest[rowIndex].tolist().count(0)==2:
			index1= gameboardTest[rowIndex].tolist().index(0)
			index2=gameboardTest[rowIndex][index1+1:].tolist().index(0)+index1+1
			#set 1,2=1,2 if it collides, switch. then switch
			gameboardTest[rowIndex][index1]=1
			gameboardTest[rowIndex][index2]=2
			for eachrow in range(0,n):
				if (gameboardTest[rowIndex]==gameboardTest[eachrow]).all() and not(eachrow==rowIndex):
					gameboard[rowIndex][index1]=2
					gameboard[rowIndex][index2]=1
					return True

			gameboardTest[rowIndex][index1]=2
			gameboardTest[rowIndex][index2]=1
			for eachrow in range(0,n):
				if (gameboardTest[rowIndex]==gameboardTest[eachrow]).all() and not(eachrow==rowIndex):
					gameboard[rowIndex][index1]=1
					gameboard[rowIndex][index2]=2
					return True
def checkDistinctCol(gameboard):
	#for every row with two remaining, try setting it equal to [1,2], see if it fails
	gameboardTest=gameboard.copy()
	for rowIndex in range(0,n):
		if gameboardTest[:,rowIndex].tolist().count(0)==2:
			index1= gameboardTest[:,rowIndex].tolist().index(0)
			index2=gameboardTest[:,rowIndex][index1+1:].tolist().index(0)+index1+1
			#set 1,2=1,2 if it collides, switch. then switch
			gameboardTest[index1][rowIndex]=1
			gameboardTest[index2][rowIndex]=2
			for eachrow in range(0,n):
				if (gameboardTest[:,rowIndex]==gameboardTest[:,eachrow]).all() and not(eachrow==rowIndex):
					gameboard[index1][rowIndex]=2
					gameboard[index2][rowIndex]=1
					return True

			gameboardTest[index1][rowIndex]=2
			gameboardTest[index2][rowIndex]=1
			for eachrow in range(0,n):
				if (gameboardTest[:,rowIndex]==gameboardTest[:,eachrow]).all() and not(eachrow==rowIndex):
					gameboard[index1][rowIndex]=1
					gameboard[index2][rowIndex]=2
					return True

#Checks if the puzzle has been solved (no empty squares remain)
def isSolved(gameboard):
	for y in range(0,n):
		for x in range(0,n):
			if gameboard[y][x]==0:
				return False
	return True


def getSolution(gameboard,showAllSteps):
	iterationCount=1
	print "Start"
	print gameboard
	gameboardOld=numpy.zeros([n,n])
	while not(isSolved(gameboard)) and not((gameboardOld==gameboard).all()):
		gameboardOld=gameboard.copy()
		checkThrees(gameboard)
		checkRowAndCol(gameboard)
		if (gameboard == gameboardOld).all():
			checkDistinctRow(gameboard)
			checkDistinctCol(gameboard)

		if showAllSteps:
			print "Iteration ", iterationCount	
			print gameboard
		iterationCount+=1

getSolution(gameboard,showAllSteps)
print "Solution"
print gameboard
