from CoffeeException import CoffeeException
from CoffeeBean import CoffeeBean
from CoffeeSelection import CoffeeSelection
from CoffeeMachine import CoffeeMachine



import traceback
if __name__ == "__main__":
	beans = dict()
	myCoffeeBean = CoffeeBean("My favorite filter coffee bean", 1000)
	beans[CoffeeSelection.FILTER_COFFEE] = myCoffeeBean

	machine = CoffeeMachine(beans)

	try: 
		espresso = machine.brewCoffee(CoffeeSelection.ESPRESSO)
		print(espresso)
	except CoffeeException as e: 
		print("Error occured!")
		traceback.print_exc()
