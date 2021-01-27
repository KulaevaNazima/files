#Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, 
#то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. 
#Подсказка: используйте ключевое слово in.
file = open ('/home/nazima/text.txt', 'w')
file.writelines("""We are, we are togerther boooletproof""")
file.close ()
file = open ('/home/nazima/text.txt', 'r')
letter= "w"
for line in file.readlines ():
	if letter in line:
		print ("Да, в тексте есть W")
	else:
		print ("Нет, в тексте нет w")
file.close ()