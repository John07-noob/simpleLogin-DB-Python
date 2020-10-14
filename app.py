import loginFUN
from loginFUN import User, printMenu, inputNum


printMenu()
user = inputNum("Insert number only: ")
if user == 1:
    username = input("Put Username: ")
    password = input("Put Pasword: ")
    info = User(username, password)
    loginFUN.login(info)
elif user == 2:
    username = input("Put Username: ")
    password1 = inputNum("Put Pasword: ")
    password2 = inputNum("Put Again: ")
    if password1 == password2:
        info = User(username, password1)
        loginFUN.signup(info)
        print("DONE")
    else:
        print("Password don't match")
else:
    print("Fuck You")