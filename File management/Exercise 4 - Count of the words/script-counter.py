import os

with open ('File management/Exercise 4 - Count of the words/ariel-script4.txt', 'w') as file_script_counter:
    count = 0
    while True:
        words = str(input("Enter word: "))
        if len(words) <= 5:
            file_script_counter.write(words + '\n' + str(len(words)))
            print("Word: -->", words)
            count += 1
            print("Count: -->", count)
        else:
            break
#print("Removing txt file....")
#os.remove('File management/Exercise 4 - Count of the words/ariel-script4.txt')