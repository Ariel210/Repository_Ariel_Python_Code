import mysql.connector

def mysql_python():
    # Creating conector
    conexion = mysql.connector.connect(
        host = "localhost",
        user = str(input("Enter user name: ")),
        password = input("Enter password: "),
        database = 'ejercicio_ventas_producto'
    )

    
    
    # Creating cursor in Python
    print("`\nDatabases and tables.....")
    cursor = conexion.cursor()
    cursor.execute("SHOW DATABASES")
    
    for database in cursor:
        print(database)
    
    print("\nTables...")
    cursor.execute("SHOW TABLES")
    for tables in cursor:
        print(tables)
mysql_python()
