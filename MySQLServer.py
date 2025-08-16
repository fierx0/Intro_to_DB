import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL Server (update user & password to your own)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",              # replace with your MySQL username
            password="yourpassword"   # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection properly
        if cursor is not None:
            cursor.close()
