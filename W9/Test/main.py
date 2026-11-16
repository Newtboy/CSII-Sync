from logic import *

def main(): # {
	app = QApplication([])
	window = Logic()
	window.setFixedSize(window.genWidth(), window.genHeight())
	window.show()
	app.exec()
# }

if (__name__ == "__main__"): # {
	main()