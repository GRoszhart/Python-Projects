class Preparing():
    
    def prepare(self):
        print("Preparing your pizza!")
        
class Baking():
    
    def bake(self):
        print("Baking your pizza!")
        
class Delivering():
    
    def deliver(self):
        print("Delivering your pizza!")
        
class PizzaTime():
    
    def __init__(self):
        self.preparing = Preparing()
        self.baking = Baking()
        self.delivering = Delivering()
        
    def process(self):
        self.preparing.prepare()
        self.baking.bake()
        self.delivering.deliver()
        
pizza= PizzaTime()
pizza.process()