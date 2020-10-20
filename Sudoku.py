__author__ = "Oceanlight"

# y down, x across
# y, x pairs
# zeroes represent empty spaces
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
	if input("Press enter to continue; press any other key to run the demo puzzle.\n") == "":
		print("Enter the 9 rows of your puzzle.\n - Put 9 numbers on every row, separating them with spaces.\n - Use a 0 for every empty space.")
		# get every row of puzzle
		for i in range(len(grid)):
			print(f"row {i + 1}:")
			# ensure that user enters rows with appropriate length
			while(True):
				grid[i] = getIntArray()
				if len(grid[i]) == len(grid):
					break
	print()
	printGrid()
	solveGrid()
	printGrid()


# map array of space separated strings to array of ints
# if invalid input, recurse to eet input again
def getIntArray():
	try:
		newRow = input().split()
		newRowInt = list(map(int, newRow))
		# ensure that user is imputing valid sudoku numbers
		for i in newRowInt:
			if i > 9 or i < 0:
				print("enter integers from 0 to 9")
				return getIntArray()

		return newRowInt
	except:
		return getIntArray()


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


# iterate through grid and retun first empty position
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
	# check "current box"
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

