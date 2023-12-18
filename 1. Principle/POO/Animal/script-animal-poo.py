class Animal:
    def __init__(self):
        pass
            
    def enter_dates(self):
        name = str(input("Enter name of the animal: "))
        colour = str(input("Enter colour of the animal: "))
        
        self.name = name
        self.colour = colour
    
    def show_dates(self):
        print(f"Name of the Dog: {self.name}")
        print(f"Colour of the Dog: {self.colour}")       

# Heredity
class Dog(Animal):
    def show_dates_dog(self):
        print("Guau !")


# Instance
mi_dog_1 = Dog()
mi_dog_1.enter_dates()
mi_dog_1.show_dates()
mi_dog_1.show_dates_dog()