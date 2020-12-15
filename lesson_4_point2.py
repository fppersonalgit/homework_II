# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка
# использовать генератор.


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res_list = [number for i, number in enumerate(my_list) if i > 0 and my_list[i] > my_list[i - 1]]

res_list_option2 = [num1 for num1, num2 in zip(my_list[1:], my_list[:-1]) if num1 > num2]

print(res_list_option2)

