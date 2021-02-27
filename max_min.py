# Создайте текстовый файл с целыми числами -> 
# Найти максимальное и минимальное число и записать в другой файл.
f = open ('chisla.txt', 'r')
a = f.read().split()
print (a)
max_chislo=max(a)
min_chislo=min(a)
print (max_chislo, min_chislo)