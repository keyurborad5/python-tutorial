class Car:

    # Class Variable
    # This variable is shared by all instances of the class
    number_of_wheels = 4
    number_of_cars = 0  # Class variable to keep track of the number of Car instances
    # Calling CConstructor method.
    # We need constructor to make an object of this class.
    def __init__(self,model,year,color, for_sale):
        # attributes which has _ before them are private attributes
        self._model= model
        self._year= year
        self._color= color
        self._for_sale= for_sale
        ## Increment the class variable each time a new Car instance is created
        Car.number_of_cars += 1

    def drive(self):
        print(f"The {self._model} is driving.")

    def stop(self):
        print(f"The {self._model} has stopped.")

    # StaticMethod
    # Utility function that don not need acess to the class data
    @staticmethod
    def get_number_of_wheels():
        return Car.number_of_wheels
    
    @staticmethod
    def is_car_type(car):
        return isinstance(car, Car) 
    
    @classmethod
    # Class Method: Best used to access class variables
    def get_number_of_cars(cls):
        return cls.number_of_cars  # Accessing class variable using cls 
    
    # Magic Method or Dunder methods
    def __str__(self):
        return f"Car(model={self.model}, year={self._year}, color={self._color}, for_sale={self._for_sale})"       
    
    #Property Decoreator
    # This allows us to use getter and setter methods as properties
    @property
    def model(self):
        """Getter for model"""
        return self._model
    
    @model.setter
    def model(self, value):
        """Setter for model"""
        self._model = value
    
    @model.deleter
    def model(self):
        """Deleter for model"""
        del self._model 

    # Decoratoes
    #A function that is used to modify another function or method
    # without modifiying the base function or method.
    # Pass base function as an argument to the decorator
    
    ## Defining decorator function
    def add_alloy_wheels(func):# here need to pass the function as an argument
        def wrapper(*args, **kwargs): #Need this function to wrap the base function
            print("Adding alloy wheels...")
            func(*args, **kwargs)
        return wrapper
    

    @add_alloy_wheels # This decorator will be called whenever the below function is called
    #we can stack here multiple decorators
    # Original Function
    def get_new_wheels(self, new_wheels):
        print(f' We got you {new_wheels} new wheels')