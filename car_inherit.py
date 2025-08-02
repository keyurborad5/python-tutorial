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
    def __str__(self): # Magic Method or dunder methods
        # Method overriding
        # This method is already defined in the parent class (Car)
        # But we are overriding it to provide a specific string representation for ElectricCar
        return f" It is an ElectricCar (model={self.model}, year={self._year}, color={self._color}, for_sale={self._for_sale}, cost={self.cost})"
class HybridCar(Car):
    pass
class GasCar(Car):
    pass