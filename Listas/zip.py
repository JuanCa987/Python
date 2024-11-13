"""zip es una funcion que toma dos listas y devuelve una lista con los elementos de las dos listas juntos"""

user = ["Juan", "Pedro", "Lucy"]
password = ("1234", "qwerty", "contra")
login_date = ["2022-01-01", "2021-12-31", "2020-12-31"]

user_password = zip(user, password, login_date)

for key,value in user_password.items():
    print(key + ' : ' + value)