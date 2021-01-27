#Cоздайте текстовый файл python.txt и запишите в него текст #1 из Classroom:
#Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит
#букву “t” или “T”, то запишите его в список t_words = [ ]. После окончания списка,
#выведите на экран все полученные слова. Подсказка: используйте for.
python = open ('/home/nazima/python.txt', 'w')
python.writelines ("""PyThon is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, PyThon has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or Java.""")
python.close ()
python = open ('/home/nazima/python.txt', 'r')
letter1= "t"
letter2= "T"
for line in python.readlines ():
	for words in line.split ():
		t_words= []
		if letter1 in words:
			t_words.append (words)
			print (t_words)
		if letter2 in words:
			t_words.append (words)
			print (t_words)