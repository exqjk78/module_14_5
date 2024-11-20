import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
     id integer PRIMARY KEY,
     title text NOT NULL,
     description text ,
     price integer NOT NULL);
     """)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')

    for i in range(1, 5):
        cursor.execute("SELECT * FROM Products WHERE title = ?", (f'Продукт {i}',))
        product = cursor.fetchone()

        if product is None:
            cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                           (f'Продукт {i}', f'Описание {i}', i * 100))

def get_all_products():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products

def add_user(username, email, age):
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
    connection.commit()

def is_included(username):
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    user = cursor.execute(f"SELECT * FROM Users WHERE username = ?", (username,))
    if user.fetchone() is None:
        return False
    else:
        return True

connection.commit()
connection.close()