from gui import *
from tkinter import Tk

def main(): # {
	window = Tk()
	window.title("Tkinter GUI test")
	window.geometry("300x100")
	window.resizable(False, False)
	Gui(window)
	window.mainloop()

if (__name__ == "__main__"): # {
	main()