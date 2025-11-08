import sqlite3

def create_db():
    conn = sqlite3.connect('bot.db')
    curr = conn.cursor()
    curr.execute("""
CREATE TABLE IF NOT EXISTS users(
    id integer primary key autoincrement,
    full_name VARCHAR(90),
    username VARCHAR(50),
    telegram_id INT UNIQUE,
    date DATE
    )
""")
    
    curr.execute("""
CREATE TABLE IF NOT EXISTS categores(
    id integer primary key autoincrement,
    name VARCHAR(90) UNIQUE,
    date DATE
    )
""")

    curr.execute("""
CREATE TABLE IF NOT EXISTS products(
    id integer primary key autoincrement,
    name VARCHAR(90),
    price INT,
    image VARCHAR(200),
    category VARCHAR(50),
    date DATE
    )
""")
    conn.commit()
    conn.close()


def insert_user(full_name, username, telegram_id, date):
    try:
        conn = sqlite3.connect('bot.db')
        curr = conn.cursor()
        query = "INSERT INTO users(full_name, username, telegram_id, date) VALUES(?, ?, ?, ?)"
        curr.execute(query, (full_name, username, telegram_id, date))
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print(e)
        return False
    finally:
        conn.close()


def insert_category(name, date):
    conn = sqlite3.connect('bot.db')
    curr = conn.cursor()
    query = "INSERT INTO categores(name, date) VALUES(?, ?)"
    curr.execute(query, (name, date))
    conn.commit()
    conn.close()
        

def read_category():
    conn = sqlite3.connect('bot.db')
    curr = conn.cursor()
    query = "SELECT name FROM categores"
    data = curr.execute(query, ).fetchall()
    return data


def read_category_detail(name):
    conn = sqlite3.connect('bot.db')
    curr = conn.cursor()
    query = "SELECT name FROM categores WHERE name = ?"
    data = curr.execute(query, (name, )).fetchone()
    if data:
        return True
    return False


def delete_category(name):
    conn = sqlite3.connect('bot.db')
    curr = conn.cursor()
    query = "DELETE FROM categores WHERE name = ?"
    curr.execute(query, (name, ))
    conn.commit()
    conn.close()


def update_category(new_name, old_name):
    conn = sqlite3.connect('bot.db')
    curr = conn.cursor()
    query = "UPDATE categores SET name = ? WHERE name = ?"
    curr.execute(query, (new_name, old_name))
    conn.commit()
    conn.close()


# add pro

def insert_product(name, price, image, category, date):
    conn = sqlite3.connect('bot.db')
    curr = conn.cursor()
    query = "INSERT INTO products(name, price, image, category, date) VALUES(?, ?, ?, ?, ?)"
    curr.execute(query, (name, price, image, category, date))
    conn.commit()
    conn.close()


def read_product(category):
    conn = sqlite3.connect('bot.db')
    curr = conn.cursor()
    query = "SELECT name FROM products WHERE category = ?"
    data = curr.execute(query, (category, )).fetchall()
    if data:
        return data
    return False


# print(read_product('Jahon adabiyoti'))