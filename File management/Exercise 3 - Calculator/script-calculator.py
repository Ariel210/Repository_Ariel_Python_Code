with open('File management/Exercise 3 - Calculator/ariel-script-calcultor.doc', 'w') as file_script_calculator:
    number_1 = int(input("Enter 1st number: "))
    number_2 = int(input("Enter 2nd number: "))
    
    sum = number_1 + number_2
    file_script_calculator.write(str(sum))
    print(sum)
