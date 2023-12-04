number_list_2 = [0,1,2,3,4,5,6,7,8,9,10]

for number in number_list_2:
    print(f"Number: {number}")
    if number % 2 == 0:
        print("This number is divisible by two: {}".format(number))