from PyQt6.QtWidgets import *
import PyQt6

def main(): # {
	app = QApplication([])
	window = MainWindow()
	window.setGeometry(0,0,300,100)
	window.show()
	app.exec()

if (__name__ == "__main__"): # {
	main();