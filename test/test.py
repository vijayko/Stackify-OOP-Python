import unittest
import sys 
sys.path.append('./../src/')
from CoffeeBean import CoffeeBean
from CoffeeMachine import CoffeeMachine
from CoffeeSelection import CoffeeSelection
from CoffeeException import CoffeeException
class TestCoffeeMachine(unittest.TestCase):
	def testEspresso(self):
		try: 
			# coffeeBean = CoffeeBean("My favorite espresso bean", 1000)
			beans = {}
			beans[CoffeeSelection.ESPRESSO] = CoffeeBean("My favorite espresso bean", 1000)
			beans[CoffeeSelection.FILTER_COFFEE] = CoffeeBean("My favorite espresso bean", 1000)

			machine = CoffeeMachine(beans)
			espresso = machine.brewCoffee(CoffeeSelection.ESPRESSO)

			self.assertEqual(CoffeeSelection.ESPRESSO, espresso.getSelection())
			self.assertEqual(28, espresso.getQuantity())
		except CoffeeException as e:
			print("there is an error!")

if __name__ == '__main__':
    unittest.main()