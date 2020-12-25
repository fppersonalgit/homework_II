# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.


salary_l = []
staff_list = open("staff.txt", "r")
content = staff_list.readlines()

for i in content:
    staff, salary = i.split(",")
    salary = int(salary)
    salary_l.append(salary)

    if salary < 20000:
        print(staff)
    print(sum(salary_l) / len(salary_l))


#понять как запихнуть в словарь если полей много









