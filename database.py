# Создайте database.txt файл с несколькими логинами и паролями. 
# Затем попросите пользователя войти или зарегистрироваться. Спросите его логин и пароль. 
# Если такой логин уже есть скажите ему что логин уже существует и предложите войти спросив пароль. 
# Если такого логина неоказалось среди уже существющих продолжайте регистрацию. 
# Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.
doc = open ('/home/nazima/Документы/database.txt', 'r')
print ("Пожалуйста, войдите или зарегистрируйтесь")
print ("Регистрация")
login= input ("Введите свой логин: ")
for lines in doc.readlines():
	if login in lines:
		print ("Такой логин уже существует")
		pas = input ("Для входа в систему введите свой пароль: ")
		if pas in lines:
			print ("Вы успешно вошли в систему!")
		else:
			print ("Вы неправильно ввели пароль")
		break

	if login != lines:
		pas1 = input ("Введите свой пароль: ")
		pas2=  input ("Повторите свой пароль: ")
		if pas1 == pas2:
			doc=open ('/home/nazima/Документы/database.txt', 'a')
			doc.write ('\nЛогин:' + pas1)
			doc.write ('\nПароль: ' + login)
			#a = doc.writelines (pas1)
			#a = doc.writelines (login)
			print ("Вы успешно зарегистрировались!")
			break

doc.close ()
#outfile.write("\n".join(itemlist)) 

#t = open ('/home/nazima/Документы/database.txt', 'a')
#while True:
