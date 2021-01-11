# Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


num_dict = {"One": "Один",
            "Two": "Два",
            "Three": "Три",
            "Four": "Четыре"}

file_to_translate = open("file_translate.txt", "r")
file_to_translate_1 = open("file_translate_2.txt", "w")
lines = file_to_translate.readlines()

for line in lines:
    num_list = line.split("-")
    file_to_translate_1.write(f"{num_dict[num_list[0]]} - {num_list[1]}")

