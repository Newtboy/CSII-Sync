
class Animal: # {
	def __init__(self, arms: int, legs: int):
		self.arms = arms
		self.legs = legs

	def getLimbs(self) -> int: # {
		return self.legs + self.arms
	# }

def main(): # {
	a = Animal(3, 3)
	print(a.getLimbs())

if (__name__ == "__main__"): # {
	main()