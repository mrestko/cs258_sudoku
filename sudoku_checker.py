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
# - contains, in each of its 81 elements, an integer in the range 0..9
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

def well_formed(grid):
    if not isinstance(grid, list): return False
    if len(grid) != 9: return False
    for sub_list in grid:
        if not(isinstance(sub_list, list)): return False
        if len(sub_list) != 9: return False
    return True

def iter_cols(grid):
    for i in range(9):
        col  = []
        for row in grid:
            col.append(row[i])
        yield col

def iter_sub_boxes(grid):
	for i in range(0, 9, 3):
		for j in range(0, 9, 3):
			box = []
			for ii in range(0, 3):	
				for jj in range(0, 3):
					box.append(grid[i+ii][j+jj])
			yield box

def valid_collection(l):
    nums = [0] * 10
    for num in l:
        if num not in range(10): return False
        nums[num] += 1
    for num in nums[1:]:
        if num > 1: return False
    return True

def check_valid(grid):
    for row in grid:
        if not valid_collection(row): return False
    for col in iter_cols(grid):
        if not valid_collection(col): return False
	for sub in iter_sub_boxes(grid):
		if not valid_collection(sub): return False
    return True

def check_sudoku(grid):
    if not well_formed(grid): return None
    return check_valid(grid)

def full(grid):
	return 0 not in [num for row in grid for num in row]

def coord_next_empty(grid):
	for row_idx in range(9):
		for col_idx in range(9):
			if grid[row_idx][col_idx] == 0:
				return (row_idx, col_idx)

def get_col(grid, col):
	vals = []
	for row in range(9):
		vals.append(grid[row][col])
	return vals

def get_sub(grid, coords):
	c_row, c_col = coords
	# integer division and multiplication to compute
	# the start index of the sub box
	s_row = (c_row / 3) * 3
	s_col = (c_col / 3) * 3
	vals = []
	for i in range(3):
		for j in range(3):
			vals.append(grid[s_row + i][s_col + j])
	return vals

def valid_for_next_empty(grid):
	next_empty = coord_next_empty(grid)
	in_row = set(grid[next_empty[0]])
	in_col = set(get_col(grid, next_empty[1]))
	in_sub = set(get_sub(grid, next_empty))
	return set(range(1, 10)).difference(in_row, in_col, in_sub)

def rep_next(grid, val):
	'''Returns new grid with val replacing the first blank'''
	new = [row[:] for row in grid]
	for i in range(9):
		for j in range(9):
			if new[i][j] == 0:
				new[i][j] = val
				return new
def pp(grid):
	pretty = ""
	for i,row in enumerate(grid):
		if i % 3 == 0 and i != 0:
			pretty += "---+---+---\n"
		for j,col in enumerate(row):
			if j % 3 == 0 and j != 0:
				pretty += "|"
			pretty += str(col)
		pretty += "\n"
	print pretty

		
def solve_sudoku(grid):
	if not well_formed(grid): return None
	if full(grid): 
		check = check_valid(grid)
		return grid if check else check
	next_vals = valid_for_next_empty(grid)
	if next_vals == None: return False
	for val in next_vals:
		test = rep_next(grid, val)
		result = solve_sudoku(test)
		if result not in [False, None]: return result


print check_sudoku(ill_formed) # --> None
print check_sudoku(valid)      # --> True
print check_sudoku(invalid)    # --> False
print check_sudoku(easy)       # --> True
print check_sudoku(hard)       # --> True

print "----Testing Solve---"
print "solve_sudoku(ill_formed):"
print solve_sudoku(ill_formed)

print "----solving easy----"
pp(solve_sudoku(easy))
print "----solving hard----"
pp(solve_sudoku(hard))
