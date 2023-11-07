import os

with open ('Scripts/Generate doc File/ariel.doc', 'w') as dates:
    print("Creating doc file...")
    dates.write("Name: Ariel \n")
    dates.write("Surname: Izurieta")

print("Removing doc file...")
os.remove('Scripts/Generate doc File/ariel.doc')

