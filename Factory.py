class Vehicle(object):
    model = ""
    
    def get_model(self):
        return self.model
    
class Truck(Vehicle):
    model = "Silverado"

class Sedan(Vehicle):
    model = "Impala"

class Suv(Vehicle):
    model = "Suburban"

class VehicleFactory(Vehicle):
    
    def create_vehicle(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()
    
vehicle_obj = VehicleFactory()
vehicles = ["truck", "sedan", "suv"]

for v in vehicles:
    print (vehicle_obj.create_vehicle(v).get_model())