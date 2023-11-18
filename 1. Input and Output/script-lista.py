number_list = []

while True:
        try:
                number = int(input("Enter number to the list: "))
                number_list.append(number)
                print(number_list)
        
        except:
                print("Incorrect data type!")
                break
print("Complete number list: ", number_list)


