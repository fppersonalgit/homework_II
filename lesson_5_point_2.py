# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_file = open("file_2.txt", "r")
content = my_file.readlines()
print(len(content))

for word in content:
    print(len(word.split()))
