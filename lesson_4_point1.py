# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

# method one inside project

from sys import argv


# method using argv

def salary_calculation1(count_hrs, price_per_hr, bonus):
    salary = (count_hrs * price_per_hr) + bonus
    print(salary)
    return salary


file_path, count_hrs, price_per_hr, bonus = argv

print(salary_calculation1(int(count_hrs), int(price_per_hr), int(bonus)))

print(argv)
