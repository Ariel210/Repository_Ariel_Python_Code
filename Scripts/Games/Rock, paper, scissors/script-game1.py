def game1_python():
    while True:
        print("Welcome to my 1st Game !")
        
        elements_list = ['Rock', 'Paper', 'Scissors']
        option_player = str(input("Enter one option for Player: "))
        option_pc = str(input("Enter one option for PC: "))
        
        print(f"\nElements: -> {elements_list}")
        print(f"Option for Player: {option_player}")
        print(f"Option for PC: {option_pc}")
        
        if option_player == 'Rock' and option_pc == 'Paper':
            print("Pc Won !")
        elif option_pc == 'Rock' and option_player == 'Paper':
            print("Player Won! ")
        elif option_player == 'Scissors' and option_pc == 'Paper':
            print("Player Won")
        else:
            print("Equals !") 
            break
game1_python()

