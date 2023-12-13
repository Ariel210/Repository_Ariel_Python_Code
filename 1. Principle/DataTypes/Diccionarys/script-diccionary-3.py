def exercise_3_diccionary():
    diccionary_3 = {0:'Ariel',1:'Izurieta',3:'30',4:'Argentina'}
    
    for key in diccionary_3.keys():
        if key % 2 == 0:
            print(f"The Key {key} is pair")
        else:
            print(f"Other Key {key}")
exercise_3_diccionary()