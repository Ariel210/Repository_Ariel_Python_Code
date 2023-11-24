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
    cursor = conexion.cursor()
    
    # Database in use
    database_use = 'ejercicio_ventas_producto'
    cursor.execute(f"USE {database_use}")
    
    
    
    # Databases All
    print("\nDatabases and tables.....")
    cursor.execute("SHOW DATABASES")
    
    for database in cursor:
        print(database)
    
    # Tables all
    print("\nTables...")
    cursor.execute("SHOW TABLES")
    for tables in cursor:
        print(tables, end=' ')
        
    print("\Columns Names - Product Table...")
    cursor.execute("SELECT * FROM producto")
    for i in cursor.column_names:
        print(i, end=' ')
mysql_python()
