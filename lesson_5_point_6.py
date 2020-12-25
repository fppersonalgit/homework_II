# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему.

my_lessons = {}
lessons_file = open("my_lessons.txt", "r")
for line in lessons_file:
    name, stats = line.split(":")
    name_sum = sum(map(int, "".join([i for i in stats if i == " " or i.isdigit()]),split()))
    my_lessons[name] = name_sum

print(my_lessons)

