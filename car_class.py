class Car:

    # Class Variable
    # This variable is shared by all instances of the class
    number_of_wheels = 4
    number_of_cars = 0  # Class variable to keep track of the number of Car instances
    # Calling CConstructor method.
    # We need constructor to make an object of this class.
    def __init__(self,model,year,color, for_sale):
        self.model= model
        self.year= year
        self.color= color
        self.for_sale= for_sale
        ## Increment the class variable each time a new Car instance is created
        Car.number_of_cars += 1

    def drive(self):
        print(f"The {self.model} is driving.")
    
    def stop(self):
        print(f"The {self.model} has stopped.")