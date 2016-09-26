#!/usr/bin/env python

global_goal = 'b12345678'

'''
Dictionaries for user inputs
'''
UP 		= 1
DOWN 	= 2
LEFT 	= 3
RIGHT 	= 4

BLANK_TILE = 'b'

func_dict = {	"setState"		:set_state,
				"randomizeState":randomize_state,
				"printState"	:print_state,
				"move"			:move,
				"solve"			:solve,
				"maxNodes"		:max_nodes}

alg_dict = {	"A-star"		:A_star,
				"beam"			:beam}

heur_dict = {	"h1"			:misplaced_tiles
				"h2"			:manhattan_distance}

move_dict = { 	"up"			:UP
				"down"			:DOWN
				"left"			:LEFT
				"right"			:RIGHT}

'''
trav_nd 	: used to keep track of visited nodes
ord_queue 	: queue of unvisited nodes
'''
class state_tree(object):

	def __init__(self, grid):
		ord_queue()
		curr_node = node(grid)

	def set_state(self, state):
		self.grid = state

	def randomize_state(self, n):
		return #TODO

'''
prev 	: used to get the last state. Used to obtain the g value (cost of traversed path)
h_weight: represents the value assigned by the h function
'''
class node(object):

	def __init__(self, grid):
	self.grid 	= grid
	prev 		= None


'''
Helpers
'''
def verify_grid(grid):
	return True #TODO

def print_statistics(stats):
	print "statistics" #TODO


def get_poss_moves(position):
	poss_moves = []
	if position >= 6:
		poss_moves.append(UP)
	if position <= 2:
		poss_moves.append(DOWN)
	if (position + 1) % 3 == 0:
		poss_moves.append(LEFT)
	if (position + 3) % 3 == 0:
		poss_moves.append(RIGHT)
	return poss_moves

def move(grid, position):
	blank_ind 	= grid.index(BLANK_TILE)
	new_grid	= grid[:]

	if position		== UP:
		tmp = new_grid[blank_ind-3]
		new_grid[blank_ind-3] = BLANK_TILE
		new_grid[blank_ind] = tmp

	elif position 	== DOWN :
		tmp = new_grid[blank_ind+3]
		new_grid[blank_ind+3] = BLANK_TILE
		new_grid[blank_ind] = tmp

	elif position 	== LEFT :
		tmp = new_grid[blank_ind-1]
		new_grid[blank_ind-1] = BLANK_TILE
		new_grid[blank_ind] = tmp


	elif position 	== RIGHT:
		tmp = new_grid[blank_ind+1]
		new_grid[blank_ind+1] = BLANK_TILE
		new_grid[blank_ind] = tmp
	return new_grid

'''
Algorithms
'''

#Use two heuristics to best approx where to go
#f = g + h
def A_star(H, start = curr_state ,goal = global_goal):
	global heur_dict

	try:
		H_func 		= heur_dict[H]
	except(KeyError e):
		raise e



#Keep only most likely branches
def beam(k, start = curr_state ,goal = global_goal):
	breath

'''
Heuristic Functions
'''
def misplaced_distance(grid, goal = global_goal):
	distance = 0
	for i in range(len(grid)):
		if grid[i] is not goal[i];
			distance += 1
	return distance

def manhattan_distance(grid, goal = global_goal):
	distance = 0
	for i in range(len(grid)):
		g_i = grid.index(goal[i])
		dist_x 		= abs(g_i % 3 - i % 3)
		dist_y 		= abs(g_i / 3 - i / 3)
		distance 	+= dist_x + dist_y
	return distance

'''
Commandline functions
'''
def set_state(grid):
	if verify_grid(grid):
		curr_state = state_tree(grid)
	else:
		raise ImportError

def randomize_state(moves):


def print_state():


def move(direction):
	move_state


def solve(args_in):
	global alg_dict

	alg, args 	= args_in.split(' ', 1 )
	try:
		stats 		= alg_dict[alg](args)
	except(KeyError e):
		raise e
	print_statistics(stats)


def max_nodes(max_amt_nodes)
	global MAX_NODES

	try:
		MAX_NODES = int(max_amt_nodes)
	except (ValueError v):
		raise v


if __name__ == '__main__':
	global func_dict

	input_var = raw_input('Enter a command: ')

	try:
		if ' ' in input_var
			fn_name, args = input_var.split(' ', 1 )
			func_dict[fn_name](args)
		else:
			func_dict[input_var]()
	except(KeyError e):
		print("Invalid Argument")
	except(ValueError v):
		print("Invalid Argument")
	print (input_var)