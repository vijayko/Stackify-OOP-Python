from Coffee import Coffee
class BrewingUnit:
	def brew(self, selection, groundCoffee, quantity):
		coffee = Coffee(selection, quantity)
		return coffee

		