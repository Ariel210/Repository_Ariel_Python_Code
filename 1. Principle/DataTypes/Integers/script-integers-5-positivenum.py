def exercise_5_integers(number_5):
    if number_5 >= 0:
        print("Positive Number")
    else:
        print("Negativa Number")
    return number_5

number_5 = int(input("Enter one number: "))
print(f"Number is: {exercise_5_integers(number_5)}")