number_list_4 = []

while True:
        try:
                number = int(input("Enter number to the list: "))
                number_list_4.append(number)
                print(number_list_4)
        
        except:
                print("Incorrect data type!")
                break
print("Complete number list: ", number_list_4)
