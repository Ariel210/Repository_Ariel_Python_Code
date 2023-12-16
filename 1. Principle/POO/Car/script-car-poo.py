class Car:
        def __init__(self, colour, brand):
            self.colour = colour
            self.brand = brand
        
        def dates_car(self):
            print(f"Mark's car: {self.brand}")
            print(f"Colour's car: {self.colour}")

# Instance
car_1 = Car("Red", "Mercedes")
car_1.dates_car()