import math

def circle(n1):
	n1 = float(n1)
	if (n1 <= 0): # {
		raise TypeError()
	return math.pi * n1**2
# }
def square(n1):

	n1 = float(n1)
	if (n1 <= 0):  # {
		raise TypeError()
	return n1**2;
	# }

# }
def rectangle(n1,n2):

	n1 = float(n1)
	n2 = float(n2)
	if (n1 <= 0 or n2 <= 0):  # {
		raise TypeError()
	return n1*n2
# }

def triangle(n1,n2):
	n1 = float(n1)
	n2 = float(n2)
	if (n1 <= 0 or n2 <= 0): # {
		raise TypeError()
	return 0.5*(n1*n2)
# }
