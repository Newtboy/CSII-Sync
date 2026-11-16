import tkinter # for SOME reason if I don't import this, "tkinter." doesn't work???
from tkinter import Frame, Label, Entry, Radiobutton, IntVar, Button
import csv

# for SOME GODFORSAKEN REASON MAIN JUST OcCaSiOnAlLy DOESN'T SEE THIS CLASS
# WHAT THE HELL WHY DOES IT DO THAT? WHY DOES IT GO AWAY SOMETIMES? WHY DID WRITING THIS COMMENT FIX IT??????????
class MyGUI: # {
	def __init__(self, window): # {
		self.window = window
		self.txt="Please fill out all values"

		self.panel1 = Frame(self.window)
		self.panel2 = Frame(self.window)
		self.panel3 = Frame(self.window)
		self.panel4 = Frame(self.window)
		self.panel5 = Frame(self.window)

		self.p1Label = Label(self.panel1, text="Name")
		self.p1Field = Entry(self.panel1)
		self.p1Label.pack(side="left", padx=10)
		self.p1Field.pack(side="left")

		self.panel1.pack(side="top", anchor="w", pady=10)

		self.p2Label = Label(self.panel2, text="Age  ")
		self.p2Field = Entry(self.panel2)
		self.p2Label.pack(side="left", padx=10)
		self.p2Field.pack(side="left")
		self.panel2.pack(side="top",anchor="w",pady=10)

		self.p3Label = Label(self.panel3, text="Status")
		self.radio = IntVar()
		self.radio.set(-1)
		self.radio_o1 = Radiobutton(self.panel3, text="Student", variable=self.radio, value=1)
		self.radio_o2 = Radiobutton(self.panel3, text="Staff", variable=self.radio, value=2)
		self.radio_o3 = Radiobutton(self.panel3, text="Both", variable=self.radio, value=3)
		self.p3Label.pack(side="left")
		self.radio_o1.pack(side="left")
		self.radio_o2.pack(side="left")
		self.radio_o3.pack(side="left")
		self.panel3.pack(pady=10)

		self.saveB = Button(self.panel4, text="SAVE", command=self.__submit)
		self.saveB.pack()
		self.panel4.pack(pady=10)

		self.p5txt = Label(self.panel5, text=self.txt)
		self.p5txt.pack()
		self.panel5.pack(pady=10)
		self.p1Field.focus_set()

	def __submit(self):
		try: # {
			txt = self.p2Field.get()
			n = int(txt)
			if (n < 0): # {
				raise ValueError()
			n *= 10
			with open("data.csv", "a", newline="") as f:  # {
				writer = csv.writer(f)
				# name, age, status
				name = self.p1Field.get().strip()
				writer.writerow([name if not name == "" else "Anonymous", n, self.__statusName()])
			self.p1Field.delete(0, tkinter.END)
			self.p2Field.delete(0, tkinter.END)
			self.radio.set(-1)
			self.p5txt.config(text="")
			self.p1Field.focus_set()
		except Exception: # {
			self.p5txt.config(text="Enter correct age value.")

	def __statusName(self):
		if (self.radio.get() == 1): # {
			return "Student"
		# }
		elif (self.radio.get() == 2): # {
			return "Staff"
		# }
		elif (self.radio.get() == 3): # {
			return "Both"
		# }
		else:
			return "NA"