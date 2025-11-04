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


# for i in read_category():
#     print(i[0])