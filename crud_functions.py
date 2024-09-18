import sqlite3


connection = sqlite3.connect('database.db')
cursor = connection.cursor()



async def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL);
''')
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES(?, ?, ?)', (f"Продукт {i}", f"Описание {i}", i*100))
    connection.commit()

async def get_all_products():

    cursor.execute('SELECT * FROM Products')
    result = cursor.fetchall()
    return result


# connection.close()
