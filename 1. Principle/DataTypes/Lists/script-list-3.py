number_list = []

while True:
    number = int(input("Enter number: "))
    if number % 2 == 0:
        print(f"Number: {number}")
        number_list.append(number)
    else:
        break
print(number_list)