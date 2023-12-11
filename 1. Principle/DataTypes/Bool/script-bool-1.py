def exercise_1_bool():
    name = str(input("Enter word: "))
    name_validation = True
    my_name = 'ariel'

    if name == my_name:
        return print(name_validation)
    else:
        return print(False)
exercise_1_bool()