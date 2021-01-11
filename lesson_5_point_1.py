# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.



my_sting = input(str("Enter something additional - \n"))
my_file_1 = open("Test text file.txt", "a+"  )
my_file_1.write(my_sting)
my_file_1.close()
