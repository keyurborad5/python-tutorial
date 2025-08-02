from car_class import Car

class ElectricCar(Car):
    def __init__(self, model, color,year, for_sale, cost):
        super().__init__(model,year, color, for_sale)
        # THe above line is similar to:
        # Car.__init__
        # Which menas we are calling the constructor of the parent class (Car) 
        # #to initialize the common attributes.
        self.cost = cost
        # So benifits of using super is 
        #you so nnot need to type again 
        # self.model, self.year, self.color, self.for_sale etc.
class HybridCar(Car):
    pass
class GasCar(Car):
    pass