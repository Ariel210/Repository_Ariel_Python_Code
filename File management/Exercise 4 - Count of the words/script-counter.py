with open ('File management/Exercise 4 - Count of the words/ariel-script4.doc', 'w') as file_script_counter:
    while True:
        word = str(input("Enter word: "))
        if len(word) <= 5:
            file_script_counter.write(word)
            print(word)
        else:
            break