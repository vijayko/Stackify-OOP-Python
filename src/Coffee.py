class Coffee: 
	def __init__(self, selection, quantity):
		self.selection = selection
		self.quantity = quantity

	def __repr__(self):
		return repr(self.selection.name + " is ready!")

	def getSelection(self):
		return selection
		
	def getQuantity(self):
		return self.quantity

	def setQuantity(self, newQuantity):
		self.quantity = newQuantity


