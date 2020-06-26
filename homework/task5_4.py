"""
 Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

rus_symbols = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре"
}
new_symbols = []
with open("task_4_doc.txt", "r", encoding="UTF-8") as text:
    new_list = text.read().split('\n')
    for new in new_list:
        item = new.split('-')
        new_symbols.append(rus_symbols[item[0]] + '-' + item[1])
    print(new_symbols)

with open("task_4_newdoc.txt", "w", encoding="UTF-8") as new_text:
    for el in new_symbols:
        new_text.write(f"{el}\n")




