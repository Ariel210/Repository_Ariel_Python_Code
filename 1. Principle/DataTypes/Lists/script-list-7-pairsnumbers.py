def exercise_7_pairs_numbers(numbers_list):
    while True:
        number = int(input("Enter one number: "))
        if number % 2 == 0:
            print(f"Number: {number}")
            numbers_list.append((number))
        else:
            break
    return numbers_list
numbers_list = []
print(f"Numbers Pairs List: {exercise_7_pairs_numbers(numbers_list)}")