# y down, x across
# y, x pairs
grid = [
	[0, 0, 0,  0, 0, 0,  7, 2, 0],
	[0, 8, 9,  0, 0, 1,  0, 0, 0],
	[0, 0, 0,  0, 0, 8,  0, 0, 0],

	[0, 0, 0,  1, 7, 5,  0, 0, 0],
	[7, 0, 0,  9, 3, 4,  0, 6, 2],
	[9, 0, 0,  2, 8, 6,  0, 0, 0],

	[0, 0, 0,  0, 0, 0,  0, 0, 4],
	[0, 7, 1,  0, 0, 0,  0, 0, 5],
	[0, 0, 0,  5, 1, 0,  0, 0, 0],
	]



def main():
	printGrid()
	solveGrid()
	printGrid()

def solveGrid():
	find = find_empty()
	# if grid is filled
	if not find:
        	return True
	else:
       		y, x = find

	# start plugging in possible numbers
	for i in range(1, 10):
		if isPossible(y, x, i):
			grid[y][x] = i
			# recurse and if it works (all spaces can be filled), return true
			if solveGrid():
				return True

			# if it doesn't work, return false
			grid[y][x] = 0

	return False



# iterate through grid and retun first empty pos  (y, x)
def find_empty():
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                return (y, x)

    return None


def isPossible(y, x, n):
	# check row
	for i in range(9):
		if grid[y][i] == n:
			return False
	# check column
	for i in range(9):
		if grid[i][x] == n:
			return False
	# check um "current box" lol
	boxY = y - y % 3
	boxX = x - x % 3
	for i in range(boxY, boxY + 3):
		for j in range(boxX, boxX + 3):
			if n == grid[i][j]:
				return False
	return True


def printGrid():
	for i in range(9):
		print(grid[i])
	print()

main()
