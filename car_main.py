# Here we have created a module named car_class.py
# This module contains a class definition for Car
# We can import this class in another script to create car objects
from car_class import Car
from car_inherit import ElectricCar, HybridCar, GasCar

def main():

    #************ Object Orienting Programming (OOP) ***************####
    # car1 = Car("BMW", 2020, "Black", True)
    # car2 = Car("Audi", 2021, "White", False)
    # car3 = Car("Au", 2021, "Whi", False)
    # car4 = Car("rrdi", 2021, "Wyellote", False)
    # car5 = Car("ford", 2021, "Red", False)


    # # print(car1.model)
    # # print(car1.year)
    # # print(car1.color)
    # # print(car1.for_sale)
    # car1.drive()
    # car1.stop()
    # # Accessing class variable
    # print(f"Number of wheels of car1 are: {car1.number_of_wheels}")  # Accessing class variable

    # # print(car2.model)
    # # print(car2.year)
    # # print(car2.color)
    # # print(car2.for_sale)
    # car2.drive()
    # car2.stop()
    # print(f'number of cars created: {Car.number_of_cars}')  # Accessing class variable
    ##************************END OOPs Concept *************************####
    #************ Iheritance **********************************####
    ecar1 = ElectricCar("Tesla Model S", 20002, "Red", True, 99000)
    hcar1= HybridCar("Toyota Prius", 2020, "Blue", False)
    gcar1 = GasCar("Ford Mustang", 2019, "Black", True)
    ecar1.drive()
    print(ecar1.color)
    print(ecar1.cost)
    hcar1.drive()
    gcar1.drive()
    print(f'number of cars created: {Car.number_of_cars}')  # Accessing class variable

if __name__ == "__main__":
    main()  # This will call the main function if this script is run directly