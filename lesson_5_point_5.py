# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.


numbers_user_enter = input(str(f"Enter numbers and add _ between numbers:\n"))


my_sum_file = open("my_sum_file.txt", "+w")
my_sum_file.write(numbers_user_enter)
my_sum_file.close()

my_sum_file = open("my_sum_file.txt", "+r")
sum_calculation = my_sum_file.readline()
sum_calculation_fixed = map(int, sum_calculation.split())
print  (sum(sum_calculation_fixed))





