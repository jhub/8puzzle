#!/usr/bin/env python

global_goal = 'b12345678'

'''
Dictionaries for user inputs
'''

func_dict = {	"setState"		:set_state,
				"randomizeState":randomize_state,
				"printState"	:print_state,
				"move"			:move,
				"solve"			:solve,
				"maxNodes"		:max_nodes}

alg_dict = {	"A-star"		:A_star,
				"beam"			:beam}

heur_dict = {	"h1"			:misplaced_tiles
				"h2"			:}

class state(object):

	grid = None

	def __init__(self, layout):
		if verify_grid(layout):
			grid = layout
		else:
			raise ImportError

	def set_state(self, state):
		self.grid = state

	def randomize_state(self, n):
		return #TODO

'''
Helpers
'''
def verify_grid(grid):
	return True #TODO

def print_statistics(stats):
	print "statistics" #TODO

'''
Algorithms
'''
#Use two heuristics to best 
def A_star(H, start = curr_state ,goal = global_goal):
	global heur_dict

	try:
		H_func 		= heur_dict[H]
	except(KeyError e):
		raise e



#Keep only most likely branches
def beam(state_count, start = curr_state ,goal = global_goal):


'''
Heuristic Functions
'''
def misplaced_distance(state, goal = global_goal):


def Manhattan_distance(state, goal = global_goal):

'''
Commandline functions
'''
def set_state(state):
	if verify_grid(layout):
		grid = layout
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