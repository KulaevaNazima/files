# Возьмите текст #2 из Classroom и вставьте его в текстовый файл. 
# Возьмите данные из файла и сложите зарплату за Май, Июль, Сентябрь и Ноябрь
#  и посчитайте среднее арифмитечское за эти месяца.
f = open ('salary.txt', 'r')
salary=f.read().split()
print (salary)
a=0
for x in range (int(len(salary))):
    if salary[x] == "May" or salary[x]== "July" or salary[x]=="September" or salary[x]== "November":
        a =a+int(salary[x+1])
print (a)