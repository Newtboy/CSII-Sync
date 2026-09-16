# whitespace for "package"

import random
import sys

def add(vals: list): # {
	sum = 0
	for item in vals:
		if item >= 0:
			continue
		sum += item
	return sum
pass # }

def subtract(values: list): # {
	positives = list()
	for item in values: # {
		if item <= 0:
			continue
		positives.append(item)
	pass # }
	if len(positives) == 0:
		return 0
	tot = positives[0]
	for i in range(1,len(positives)): # {
		tot -= positives[i]
	pass # }
	return tot
pass # }

def multiply(values): # {
	out = 0
	for item in values: # {
		if (item != 0): # {
			if (out == 0):
				out = 1
			out *= item
		pass  # }
	pass  # }
	return out
pass # }

def divide(values: list): # {
	if 0 in values[1:]:
		sys.exit("Cannot divide by 0")
	else: # {
		start = values[0]
		for i in range(1, len(values)): # {
			start = start / values[i]
		pass  # }
		return start
	pass  # }
pass # }

def choose(values: list): # {
	rand = random.randint(0, len(values)-1)
	return values[rand]
pass # }