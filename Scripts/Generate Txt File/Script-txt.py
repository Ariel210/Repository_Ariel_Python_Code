import os

with open('Scripts/Generate Txt File/file.txt', 'w') as file_txt:
    print("Hola ariel")
    
print("Removing txt file...")
os.remove('Scripts/Generate Txt File/file.txt')