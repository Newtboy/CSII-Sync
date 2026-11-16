from tkinter import *

class Gui: # {
	def __init__(self, window):
		self.window = window

		self.names:dict = {}

		self.frame_one = Frame(self.window)
		self.input_name = Entry(self.frame_one, width = 20)
		self.button_save = Button(self.frame_one, text="SAVE",command=self.submit)
		self.input_name.pack(side="left")
		self.button_save.pack(side="left")
		self.frame_one.pack()

		self.frame_two = Frame(self.window, pady=10)
		self.label_name = Label(self.frame_two, text="Smith")
		self.label_name.pack()
		self.frame_two.pack()

		self.frame_three = Frame(self.window)
		self.radio_answer = IntVar()
		self.radio_answer.set(1)
		self.radio_yes = Radiobutton(self.frame_three, text="Yes", variable=self.radio_answer, value=1)
		self.radio_no = Radiobutton(self.frame_three, text="No", variable=self.radio_answer, value=2, command=self.radio)
		self.radio_yes.pack(side="left")
		self.radio_no.pack(side="left")
		self.frame_three.pack()

	def submit(self):
		name = self.input_name.get()
		status=self.radio_answer.get()
		if (name != "" and not name.isdigit() and len(name) < 20): # {
			if (status == 1): # {
				self.label_name.config(text=f"Hello {name}, you selected 1")
			else:
				self.label_name.config(text=f"Hello {name}, you selected no")
			self.names[name] = self.names.get(name, 0) + 1
			print(self.names)
		else:
			self.label_name.config(text=f"{name} is not valid.")
		self.input_name.delete(0, END)

	def radio(self):
		self.button_save.config(bg="red")