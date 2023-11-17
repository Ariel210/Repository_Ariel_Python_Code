import mysql.connector

def mysql_python():
    # Creating conector
    conexion = mysql.connector.connect(
        host = "localhost",
        user = str(input("Enter user name: ")),
        password = input("Enter password: ")
    )

    
    
    print("`\nDatabases.....")
    # Creating cursor in Python
    cursor = conexion.cursor()
    cursor.execute("SHOW DATABASES")
    
    for database in cursor:
        print(database)
mysql_python()
