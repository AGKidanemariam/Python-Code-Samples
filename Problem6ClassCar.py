# Abraham Kidanemariam
# 11/10/24
# Problem 6: Modify a car class to include type and manufacturer, and update the fullspecs method.

class Car:
    def __init__(self, model, year, color, car_type, manufacturer):
        """Initializes the car attributes."""
        self.model = model
        self.year = year
        self.color = color
        self.car_type = car_type
        self.manufacturer = manufacturer

    def get_model(self):
        """Returns the model of the car."""
        return self.model

    def get_year(self):
        """Returns the year of the car."""
        return self.year

    def get_color(self):
        """Returns the color of the car."""
        return self.color

    def get_type(self):
        """Returns the type of the car."""
        return self.car_type

    def get_manufacturer(self):
        """Returns the manufacturer of the car."""
        return self.manufacturer

    def fullspecs(self):
        """Returns all specs of the car in a single string."""
        return f"{self.model} {self.year} {self.color} {self.car_type} by {self.manufacturer}"

# Creating instances and testing the class
car1 = Car("Sports", 2012, "Blue", "Convertible", "Toyota")
car2 = Car("Sedan", 2020, "Black", "SUV", "Honda")

# Print results to test methods
print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())
