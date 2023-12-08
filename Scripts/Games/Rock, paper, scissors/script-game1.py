def game1_python():
    while True:
        print("Welcome to my 1st Game !")
        elements_list = ['Rock', 'Paper', 'Scissors']
        
        for element in elements_list:
            print(f"Elements in the lista: {element}")
        
        option_player = str(input("Enter one option for Player: "))
        option_pc = str(input("Enter one option for PC: "))
        
        if option_player in elements_list[0] and option_pc in elements_list[1]:
            print("Pc Won!")
        elif option_pc in elements_list[0] and option_player in elements_list[1]:
            print("Player Won!")
        else:
            print("Equals !")
            break
game1_python()

