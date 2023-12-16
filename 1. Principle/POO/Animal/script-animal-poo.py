class Animal:
    def __init__(self):
        pass
            
    def enter_dates(self):
        name = str(input("Enter name of the animal: "))
        colour = str(input("Enter colour of the animal: "))
        
        self.name = name
        self.colour = colour
    
    def show_dates(self):
        print(f"Name of the animal: {self.name}")
        print(f"Colour of the animal: {self.colour}")       


animal_1 = Animal()
animal_1.enter_dates()
animal_1.show_dates()