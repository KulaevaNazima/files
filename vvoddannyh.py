# 2. Создайте текстовый файл -> 
# Записать в него построчно данные, которые вводит пользователь
# Окончание ввода должен принимать пустую строку
a = open ('dannye.txt', 'a')
text= input ("Ввведит данные: ")
a.writelines (f'{text}\n')