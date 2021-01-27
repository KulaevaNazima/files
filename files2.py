# Создайте файл users.txt. 
# Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt.
users = open ('/home/nazima/users.txt', 'w')
login = input ("Введите свой логин: ")
pas = input ("Введите свой пароль: ")
users.writelines (login)
users.writelines (pas)
users.close ()
users = open ('/home/nazima/users.txt', 'r')
print (users.read ())