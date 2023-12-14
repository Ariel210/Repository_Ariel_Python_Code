def sum_lists():
    list_number_1 = [1,2,3]
    list_number_2 = [1,2,3]
    
    print([sum(numbers) for numbers in zip(list_number_1,list_number_2)])  
sum_lists()