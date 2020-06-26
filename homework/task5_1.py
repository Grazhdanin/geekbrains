"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

text = open("doc_text.txt", "w", encoding="UTF-8")

while True:
    line = input("Введите данные: ")
    text.write(f"{line} \n")

    if not line:
        break
text.close()