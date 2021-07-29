"""
package org.thoughts.on.java.coffee;

public class CoffeeException extends Exception {

	public CoffeeException() {
		super();
	}

	public CoffeeException(String message, Throwable cause,
			boolean enableSuppression, boolean writableStackTrace) {
		super(message, cause, enableSuppression, writableStackTrace);
	}

	public CoffeeException(String message, Throwable cause) {
		super(message, cause);
	}

	public CoffeeException(String message) {
		super(message);
	}

	public CoffeeException(Throwable cause) {
		super(cause);
	}

}


"""

class CoffeeException(Exception):
	def __init__(self, message):
		self.message = message
		super().__init__(self.message)

	