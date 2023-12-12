import random

def game_random_game():
    while True:
        number = int(input("Enter one number: "))
        random_number = random.randint(0,5)

        if number == random_number:
            print(f"1st number: {number}")
            print(f"2nd number: {random_number}")
            print("Both numbers are equals !")
        else:
            print(f"1st number: {number}")
            print(f"2nd number: {random_number}")
            print("Diferents numbers !")
            break
game_random_game()