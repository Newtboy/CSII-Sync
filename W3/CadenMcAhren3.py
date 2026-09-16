# package null.wizard.newtboy

import sys
import formulas

def main(): # {
	args = sys.argv
	if len(args) <= 1: # {
		sys.exit("Need to provide operator")
	# }
	elif len(args) <= 3: # {
		sys.exit("Need to provide at least two values")
	pass # }
	op = args[1]
	vals = []
	# Fuck you python fuck you python fuck you python
	for item in args[2:]:
		vals.append(float(item))
	# just gonna leave this here in case I need to rework validOps = ["add", "multiply", "divide", "subtract", "choose"]
	ans = 0.0
	if (op == "multiply"): # {
		ans = formulas.multiply(vals)
	# }
	elif (op == "divide"): # {
		ans = formulas.divide(vals)
	# }
	elif (op == "add"): # {
		ans = formulas.add(vals)
	# }
	elif (op == "subtract"): # {
		ans = formulas.subtract(vals)
	# }
	elif (op == "choose"): # {
		ans = formulas.choose(vals)
	# }
	else: # {
		sys.exit("Valid operator names (add, subtract, multiply, divide, choose")
	# }
	sys.exit(f"Answer = {ans:0.2f}")
pass # }


if __name__ == "__main__":
	main()
	# Insert Tchaikovsky's 1812 overture as I write this