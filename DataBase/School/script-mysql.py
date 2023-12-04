import mysql.connector
import getpass

school_conexion = mysql.connector.connect(
    host = "localhost",
    user = str(input("Enter user name: ")),
    #password = input("Enter password: ")
    password = getpass.getpass("Enter Password: ")
)

# Creating cursor
cursor = school_conexion.cursor()

# Defining school database
print("School Database in use....")
school_database = 'ejercicio_colegio'
cursor.execute(f"USE {school_database}")

# Teachers Table
print("Teacher Table...")
cursor.execute('DESCRIBE profesor')
describe_cursor = cursor.fetchall()
for data in describe_cursor:
    print(data)