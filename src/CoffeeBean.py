class CoffeeBean:
	def __init__(self, name, quantity):
		self.__name = name
		self.__quantity = quantity

	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name

	def getQuantity(self):
		return self.__quantity

	def setQuantity(self, quantity):
		self.__quantity = quantity




"""
And the classes CoffeeBean and Coffee are simple POJOs (plain old Java objects) that only store a set of attributes without providing any logic.
public class CoffeeBean {
private String name;
private double quantity;

 public CoffeeBean(String name, double quantity) {
     this.name = name;
    this.quantity;
}
}
"""