user_pass = {"Vuyani" : "vuya@2021", "Atheelah" : "maroon17", "Ikraam" : "carsthemovies", "Nathan": "blue101","Amanda" : "@manda20"}
user = input("Please Enter Username :")
password = input("Please Enter Password : ")

def user_search(username, _password, _dict):
    if username in _dict:
        if _password == _dict[username]:
            return 1
        else:
            return 0
    else:
        return -1

x = int(user_search(user, password, user_pass))
print(' ')
if x == 1:
    print("Your details are incorrect")
elif x == 0:
    print("Incorrect password")
elif x == -1:
    print("Username doesnt exist")

