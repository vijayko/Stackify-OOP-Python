from CoffeeException import CoffeeException
from Grinder import Grinder
from Configuration import Configuration
from GroundCoffee import GroundCoffee
from BrewingUnit import BrewingUnit
from CoffeeSelection import CoffeeSelection
from Coffee import Coffee

class CoffeeMachine:
	# self.beans = {}

	def __init__(self, beans):
		self.beans = beans
		self.grinder = Grinder()
		self.brewingUnit = BrewingUnit()

		self.configMap = dict()
		self.configMap[CoffeeSelection.ESPRESSO] = Configuration(8, 28)
		self.configMap[CoffeeSelection.FILTER_COFFEE] = Configuration(30, 480)

	def brewEspresso(self):
		config = self.configMap[CoffeeSelection.ESPRESSO]
		# grind the coffee beans
		# print(self.beans)
		if CoffeeSelection.ESPRESSO in self.beans.keys():
			groundCoffee = self.grinder.grind(self.beans[CoffeeSelection.ESPRESSO], config.getQuantityCoffee())
		# brew an espresso
			print("Coffee is brewing ...")
			return self.brewingUnit.brew(CoffeeSelection.ESPRESSO, groundCoffee, config.getQuantityWater())
		else: 
			raise CoffeeException("CoffeeSelection not supported")

	def brewFilterCoffee(self):
		config = self.configMap[CoffeeSelection.FILTER_COFFEE]
		# grind the coffee beans
		# print(self.beans)
		groundCoffee = self.grinder.grind(self.beans[CoffeeSelection.FILTER_COFFEE], config.getQuantityCoffee())
		# brew a filter coffee
		print("Coffee is brewing ...")
		return self.brewingUnit.brew(CoffeeSelection.FILTER_COFFEE, groundCoffee, config.getQuantityWater)

	def brewCoffee(self, selection):
		if selection is CoffeeSelection.FILTER_COFFEE:
			# print("FILTER_COFFEE is selected!")
			return self.brewFilterCoffee()

		elif selection is CoffeeSelection.ESPRESSO:
			# print("ESPRESSO is selected!")
			return self.brewEspresso()
		else: 
			raise CoffeeException("CoffeeSelection " + selection.name + " not supported")



"""

import java.util.Map;
public class CoffeeMachine {
private Map<CoffeeSelection, Configuration> configMap;
private Map<CoffeeSelection, CoffeeBean> beans;
private Grinder grinder;
private BrewingUnit brewingUnit;

public CoffeeMachine(Map<CoffeeSelection, CoffeeBean> beans) {
    this.beans = beans;
    this.grinder = new Grinder();
    this.brewingUnit = new BrewingUnit();

    // create coffee configuration
    this.configMap = new HashMap<CoffeeSelection, Configuration>();
    this.configMap.put(CoffeeSelection.ESPRESSO, new Configuration(8, 28));
    this.configMap.put(CoffeeSelection.FILTER_COFFEE, new Configuration(30, 480));
}


}

"""





"""
import org.thoughts.on.java.coffee.CoffeeException;
import java.utils.Map;
public class CoffeeMachine {
private Map<CoffeeSelection, CoffeeBean> beans;

public CoffeeMachine(Map<CoffeeSelection, CoffeeBean> beans) {
     this.beans = beans
}

public Coffee brewCoffee(CoffeeSelection selection) throws CoffeeException {
    Coffee coffee = new Coffee();
    System.out.println(“Making coffee ...”);
    return coffee;
}

"""