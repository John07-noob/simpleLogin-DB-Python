import sqlite3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def printMenu():
    print("Choose an option:")
    print("1. login")
    print("2. sign up")
    print("")

def inputNum(number):
    while True:
        try:
            user_input = int(input(number))
        except ValueError:
            print("Only Number!")
            continue
        else:
            return user_input
            break

def cursor():
    return sqlite3.connect("data.db").cursor()

# CREATE TABLE
c = cursor()
c.execute('''CREATE TABLE IF NOT EXISTS data
            (username TEXT, password INTERGER)''')
c.connection.close()

def signup(info):
    c = cursor()
    with c.connection:
        c.execute('''INSERT INTO data VALUES
                    (?, ?)''', (info.username, info.password))
    c.connection.close()

def login(info):
    c = cursor()
    with c.connection:
        c.execute('''SELECT * FROM data
                    WHERE username = ?
                    AND password = ?
                    ''', (info.username, info.password))
    results = c.fetchall()
    if results:
        for i in results:
            print(f"Welcome Back {i[0]}")
            c.connection.close()
    else:
        print("Invalid Username or Password")
        c.connection.close()