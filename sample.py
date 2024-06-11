import mysql.connector

try:
    # Establish connection to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hadhi202@",
        database="attendance_system"
    )
    # Print a message indicating successful connection
    print("Connected to MySQL database!")
    # Optionally, print connection details
    print(mydb)
except mysql.connector.Error as err:
    # Handle connection errors
    print(f"Error connecting to MySQL: {err}")
