
def print_grid(grid, str):
	print "%s = [" % str
	for row in grid:
		print "        [%d,%d,%d,%d,%d,%d,%d,%d,%d]," %  (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
	print "]"

def my_check_sudoku(grid):
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
            if type(row) is not list:
                return None
            if len(row) != 9:
                return None
            for e in row:
                if type(e) is not int:
                        return None
                if(e < 0) or (e > 9):
                    return None
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

def my_solve_sudoku_step(grid, marks, bitcount, depth):
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
                                ret = my_solve_sudoku_step(grid, marks, bitcount, depth+1)
                        if type(ret) is list:
                                return ret
                        marks = save_marks
                grid[y][x] = 0
                return False

        ret = my_check_sudoku(grid)
        if ret is not True:
                print 'Check: ', grid, ' but marks:', marks
                assert False
                return False
        #print 'end solve_sudoku depth:', depth, 'grid:', grid
        return grid


def my_solve_sudoku(grid):
        if my_check_sudoku(grid) is None:
                return None
        bitcount = {}
        for i in xrange(0, 512):
                count = 0
                for j in xrange(0, 9):
                        if (i & (1 << j)):
                                count += 1
                bitcount[i] = count
        return my_solve_sudoku_step(grid, [], bitcount, 0)



import random
import copy

def test_sud_onegrid(grid, exp_check, exp_soln):
	# Copy grid, make sure it's solvable
	ret = my_check_sudoku(grid)
	if ret is not exp_check and (exp_check >= 0):
		print 'Initial check grid:', grid, ', ret:',ret,'is not', exp_check
		assert False
	new_grid = copy.deepcopy(grid)
	print "Calling solve_sudoku"
	ret = solve_sudoku(new_grid)
	print "Sudoku solved"
	if ret is not False and ret is not True and type(ret) is not list:
		print 'solve_sudoku ret:', ret
		assert False
	if ret is False and (exp_soln <= 0):
		return False		# Solver failed, and that's OK
	if ret and (exp_soln == False):
		# Solver succeeded but I think it should have failed
		print 'Test solve_sudoku solved: ', grid, ', I expected not'
		assert False
	if my_check_sudoku(ret) is not True:
		print 'Checking grid:', grid, ' check is not True'
		assert False
	assert check_sudoku(ret) is True
	for y in xrange(0, 9):
		for x in xrange(0, 9):
			cell = ret[y][x]
			if cell == 0:
				print 'x,y is 0', x, y, ret[y]
				assert False
			if grid[y][x] != 0:
				if cell != grid[y][x]:
					print 'x,y', x,y, 'ret is',ret[y],'but orig grid was', grid[y]
					assert False
	return True


def test_sud_solver(num_tests):
	random.seed(1234)		# Make it repeatable
	bad_elems = ( (0,1,2,3,4,5,6,7,8), (1,2,None), None, "hello", "0", 10, -5, 2**40, True, False, 3.5, [], '', xrange(9), range(8), range(10), [ 1, 2, 3 ] )
	print 'bad_elems: ', bad_elems
	for i in xrange(num_tests):
		# Create a valid grid filled with 0's
		grid = []
		for y in xrange(0, 9):
			grid.append([])
			for x in xrange(0, 9):
				grid[y].append(0)
		assert my_check_sudoku(grid) is True
		num_changed = 0
		force_good = random.random() < 0.50
		if random.random() < 0.50:
			# Fill grid with random numbers 1-9
			print 'Randomizing', i
			num_to_flip = random.randint(1, 70)	# 70!!
			for j in xrange(num_to_flip):
				y = random.randint(0, 8)
				x = random.randint(0, 8)
				cell = grid[y][x]
				if cell == 0:
					grid[y][x] = random.randint(1, 9)
					if my_check_sudoku(grid) is not True and force_good:
						grid[y][x] = 0
					else:
						num_changed += 1
		#print 'num_changed:', num_changed, 'grid is now:', grid
		priv_grid = copy.deepcopy(grid)
		my_check = my_check_sudoku(priv_grid)
		print_grid(priv_grid, 'Calling my solver:')
		my_soln = my_solve_sudoku(priv_grid)
		print 'my_soln:', my_soln
		print test_sud_onegrid(grid, my_check, type(my_soln) is list)
		# Do bad queue testing
		y = random.randint(0, 8)
		x = random.randint(0, 8)
		bad_num = random.randint(1, len(bad_elems)) - 1
		bgrid = copy.deepcopy(grid)
		rep = -1
		insert = -1
		poppos = -1
		if random.random() < 0.50:
			# add or delete an item in the row
			if random.random() < 0.50 :
				insert = random.randint(0, 9)
				bgrid[y].insert(bad_num, insert)
			else:
				poppos = x
				bgrid[y].pop(x)
		else:
			rep = bad_elems[bad_num]
			bgrid[y][x] = rep
			print 'Set x,y', x, y, ' to:', rep, bgrid[y][x]
			print 'bgrid[y]:', bgrid[y]
		bgrid_copy = copy.deepcopy(bgrid)
		ch = check_sudoku(bgrid)
		if ch is not None:
			print 'check_sudoku ret:', ch,' Bad grid: ', bgrid
			print 'x,y:', x, y, 'insert:', insert, 'bad_num', bad_num, 'pop:', poppos, 'rep:', rep
			assert False
		ch = solve_sudoku(bgrid)
		if ch is not None:
			print 'solve_sudoku:', bgrid, 'ret:', ch
			assert ch is None

		if random.random() < 0.9:
			bgrid = copy.deepcopy(grid)

		# And replace a row with a bad_elem
		bad_num = random.randint(0, len(bad_elems)-1)
		if random.random() < 0.50:
			# Add or delete a row
			if random.random() < 0.50 :
				bgrid.insert(y, grid[random.randint(0,8)])
			else:
				bgrid.pop(y)
		else:
			bgrid[y] = bad_elems[bad_num]
		ch = check_sudoku(bgrid)
		if ch is not None:
			print 'check_sudoku2 ret:', ch,' Bad grid: ', bgrid
			assert False
		
		ch = solve_sudoku(bgrid)
		if ch is not None:
			print 'solve_sudoku2:', bgrid, 'ret:', ch
			assert ch is None
	return True
	

print test_sud_solver(500)


