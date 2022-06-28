import sqlite3

connection = sqlite3.connect('createdb1.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS done_tasks(price INT)')
connection.commit()


def insert(price: int):
    cursor.execute(
        'INSERT INTO done_tasks VALUES(?)', (price, )
    )
    connection.commit()


def fetchall():
    cursor.execute(
        'SELECT * FROM done_tasks'
    )
    earn_list = cursor.fetchall()
    return earn_list


def delete():
    cursor.execute(
        'DELETE FROM done_tasks'
    )
    connection.commit()


