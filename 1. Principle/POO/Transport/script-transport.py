class Transport:
    def __init__(self, nombre):
        self.nombre = nombre
        self.wheels = int(input("Enter wheels for transport: "))
    
class Bicycle(Transport):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def show_dates_bycicle(self):
        print(f"I'm {self.nombre}")
        if self.wheels == 2:
            print("Correct! I have two wheels")
        else:
            print("Incorrect! ")
            
# Instance
my_bicycle_1 = Bicycle('My bicycle number 1')
my_bicycle_1.show_dates_bycicle()