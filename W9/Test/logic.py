from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *
from gui import Ui_mainWindow

class Logic(QMainWindow, Ui_mainWindow): # {
	def __init__(self):
		super().__init__()

		self.setupUi(self)
		self.tax = 0.1
		self.buttonSubmit.clicked.connect(self.submit)
		self.buttonClear.clicked.connect(self.clear)

	def genWidth(self):
		return self.width()
	# }
	def genHeight(self):
		return self.height()
	# }
	def submit(self):
		foodTxt = (self.inputFood.text());
		dessertTxt = self.inputDessert.text();
		drinkTxt = self.inputDrink.text();
		try: # {
			drinkAmt = float(drinkTxt)
			foodAmt = float(foodTxt)
			dessertAmt = float(dessertTxt)
			if (self.radio10.isChecked()):  # {
				tipPer = 0.1
			elif (self.radio15.isChecked()):  # {
				tipPer = 0.15
			else:
				tipPer = 0.2
			subTot = (foodAmt + dessertAmt + drinkAmt)
			taxAmt = subTot * self.tax
			tipAmt = (subTot + taxAmt) * tipPer
			total = subTot + taxAmt + tipAmt
			self.labelOutput.setFont(QFont("Consolas", 10))
			self.labelOutput.setText(
				f"{'SUMMARY':^23}\n\n"
				f"{'Food:':<15}${float(foodTxt):>7.2f}\n"
				f"{'Drink:':<15}${float(drinkTxt):>7.2f}\n"
				f"{'Dessert:':<15}${float(dessertTxt):>7.2f}\n"
				f"{'Tax:':<15}${taxAmt:>7.2f}\n"
				f"{'Tip:':<15}${tipAmt:>7.2f}\n\n"
				f"{'TOTAL:':<15}${total:>7.2f}"
			)
		except ValueError: # {
			self.labelOutput.setText("All inputs should be numeric, e.g. 10.23, not $10.23")
			return



	def clear(self):
		self.inputDrink.clear()
		self.inputDessert.clear()
		self.inputFood.clear()
		self.radio10.setChecked(True)
		self.labelOutput.clear()
	# }

	pass