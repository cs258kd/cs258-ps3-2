# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, a number in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row 
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7 
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
# 
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

blank = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

hard2= [[8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]]

illeg2=[[0,0,0,0,0,0,0,0,0],
        xrange(9),
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]


def check_sudoku(grid):
    def check_sudoku_row(grid):
        seen = 0
        for e in row:
            mask = 1 << e
            if e == 0:
                continue
            if (mask & seen):
                return False
            seen = seen | mask
        return True
        
    try:
        if len(grid) != 9:
            return None
        for i in xrange(0, 9):
            row = grid[i]
            #print 'check init row:', row, 'type: ', type(row)
            if type(row) is not list:
                return None
            if len(row) != 9:
                return None
            for e in row:
		if type(e) is not int:
			return None
                if(e < 0) or (e > 9):
                    return None
        for row in grid:
            if not check_sudoku_row(row):
                return False
	for i in xrange(0, 9):
            row = [grid[j][i] for j in xrange(0,9)]
            if not check_sudoku_row(row):
                return False
        # unswirl grid (row[0] = upper left quad, row[1] = middle upper quad
        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                row = grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]
                if not check_sudoku_row(row):
                    return False
        return True
    except:
        # Some kind of type problem or other issue
        return None

print check_sudoku(ill_formed) # --> None
print check_sudoku(illeg2)     # --> None
print check_sudoku(valid)      # --> True
print check_sudoku(invalid)    # --> False
print check_sudoku(easy)       # --> True
print check_sudoku(hard)       # --> True
print check_sudoku(hard2)      # --> True
print check_sudoku(blank)      # --> True

import copy

def print_gridhex(grid, str):
	print "%s = [" % str
	for row in grid:
		print "[%03x, %03x, %03x, %03x, %03x, %03x, %03x, %03x, %03x]," %  (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
	print "]"

def solve_sudoku_step(grid, marks, bitcount, depth):
	def mark_update(marks, grid, x, y, skip_x, skip_y, new_mark):
		mark = marks[y][x]
		cell = grid[y][x]
		if cell != 0:
			mark = 1 << (cell - 1)
		if x != skip_x or y != skip_y:
			this_mark = mark & (~new_mark)
			marks[y][x] = this_mark
			if this_mark == 0:
				return False
		else:
			marks[y][x] = new_mark
		return True
	def mark_neighbors(marks, grid, x, y, mark):
		for i in xrange(0, 9):
			if not mark_update(marks, grid, x, i, x, y, mark):
				#print '1 mark fail:', x,y,i,depth, marks, grid
				return False
			if not mark_update(marks, grid, i, y, x, y, mark):
				#print '2 mark fail:', x,y,i,depth, marks, grid
				return False
		base_y = (y / 3) * 3
		base_x = (x / 3) * 3
		for i in xrange(0, 3):
			for j in xrange(0, 3):
				if not mark_update(marks, grid, base_x+i, base_y+j, x, y, mark):
					#print '3 mark fail:', x,y,i,j,depth, marks, grid
					return False
		return True

	# Generate marks[][] showing what values are legal at each pos
	if depth == 0:
		marks = [];
		for y in xrange(0, 9):
			marks.append([])
			for x in xrange(0, 9):
				marks[y].append(0x1ff)
		for y in xrange(0, 9):
			for x in xrange(0, 9):
				cell = grid[y][x]
				if cell == 0:
					continue
				mark = 1 << (cell - 1)
				if not mark_neighbors(marks, grid, x, y, mark):
					return False


	# Find a cell that is 0 without a lot of choices
	min_count = 20
	save_xy = [0,0]
	for y in xrange(0, 9):
		for x in xrange(0, 9):
			if grid[y][x] == 0:
				count = bitcount[marks[y][x]]
				if(count < min_count):
					save_xy = [x, y]
					min_count = count
					if count == 1:
						break
		if min_count == 1:
			break

	if min_count >= 1 and min_count <= 9:
		x = save_xy[0]
		y = save_xy[1]
		cell = grid[y][x]
		for v in xrange(1, 10):
			mark = 1 << (v - 1)
			grid[y][x] = v
			if (marks[y][x] & mark) == 0:
				continue
			save_marks = copy.deepcopy(marks)
			ret = mark_neighbors(marks, grid, x, y, mark)
			if ret:
				ret = solve_sudoku_step(grid, marks, bitcount, depth+1)
			if type(ret) is list:
				return ret
			marks = save_marks
		grid[y][x] = 0
		return False

	ret = check_sudoku(grid)
	if ret is not True:
		print 'Check: ', grid, ' but marks:', marks
		assert False
		return False
	#print 'end solve_sudoku depth:', depth, 'grid:', grid
	return grid


def solve_sudoku(grid):
	if check_sudoku(grid) is None:
		return None
	#print_gridhex(grid, "grid")
	bitcount = {}
	for i in xrange(0, 512):
		count = 0
		for j in xrange(0, 9):
			if (i & (1 << j)):
				count += 1
		bitcount[i] = count
	return solve_sudoku_step(grid, [], bitcount, 0)


print 'solving ill_formed'
print solve_sudoku(ill_formed)
print 'solving valid'
print solve_sudoku(valid)

print 'solving invalid'
print solve_sudoku(invalid)
print 'Now doing easy'
print solve_sudoku(easy)
print 'Now doing hard'
print solve_sudoku(hard)
print 'Now doing blank'
print solve_sudoku(blank)

print 'Now doing hard2'
print solve_sudoku(hard2)

