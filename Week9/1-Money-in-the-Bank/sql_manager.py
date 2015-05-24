import sqlite3
from Client import Client
# from settings import DB_NAME, DB_SQL_STRUCTURE

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                email TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)
    conn.commit()


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password, email):
    insert_sql = "INSERT into clients (username, password) values (?, ?)"
    cursor.execute(insert_sql, (username, password, password))
    conn.commit()


def login(username, password):
    # prepared statements
    select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"

    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
    conn.commit()


def get_user_email(username):
    cursor.execute("""SELECT email
                        FROM clients
                        WHERE username = ?""", (username,))
    email = cursor.fetchone()
    return email[0]


def deposit(amount, logged_user):
    cursor.execute("""SELECT balance
                        FROM clients
                        WHERE username = ?""", (logged_user,))
    balance = cursor.fetchone()
    total = balance[0] + amount
    cursor.execute("""UPDATE clients
                        SET balance = ?
                        WHERE username = ?""", (total, logged_user))
    conn.commit()

def withdraw(amount, logged_user):
    cursor.execute("""SELECT balance
                        FROM clients
                        WHERE username = ?""", (logged_user,))
    balance = cursor.fetchone()
    total = balance[0]

    if total < amount:
        print("Invalid ammount")
    elif total == amount:
        cursor.execute("""UPDATE clients
                            SET balance = ?
                            WHERE username = ?""", (0, logged_user))
    else:
        cursor.execute("""UPDATE clients
                            SET balance = ?
                            WHERE username = ?""", (total - amount, logged_user))
    conn.commit()

def display(logged_user):
    cursor.execute("""SELECT balance
                        FROM clients
                        WHERE username = ?""", (logged_user,))
    balance = cursor.fetchone()[0]
    print(balance)
    return balance


# h = create_clients_table()
