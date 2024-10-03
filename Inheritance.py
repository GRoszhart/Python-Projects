#Week 3 Assignment
#Inheritance of Pizza Related Things

class Pizza:
    def __init__(self, name, size, toppings):
        self.name = name
        self.size = size
        self.toppings = toppings
        
class PepperoniPizza(Pizza):
    def __init__(self, size):
        toppings = ["tomato sauce","mozzerella cheese","pepperoni"]
        super().__init__(self, size, toppings)
        
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def remove_topping(self, topping):
        self.toppings.remove(topping)
        
class CheesePizza(Pizza):
    def __init__(self, size):
        toppings = ["tomato sauce","mozzerella cheese","parmesan cheese"]
        super().__init__(self, size, toppings)
    
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def remove_topping(self, topping):
        self.toppings.remove(topping)
        
class SausagePizza(Pizza):
    def __init__(self, size):
        toppings = ["tomato sauce","mozzerella cheese","sausage"]
        super().__init__(self, size, toppings)
        
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def remove_topping(self, topping):
        self.toppings.remove(topping)
        
myPizza = SausagePizza("large")
myPizza.remove_topping("sausage")

myOtherPizza = PepperoniPizza("small")
myOtherPizza.add_topping("green pepper")

print("I ordered two pizzas: one with",str(myPizza.toppings[0]),"and",str(myPizza.toppings[1]),
      "and one with\n",str(myOtherPizza.toppings[0]),",",str(myOtherPizza.toppings[1]),
      ",",str(myOtherPizza.toppings[2]),", and",str(myOtherPizza.toppings[3]))