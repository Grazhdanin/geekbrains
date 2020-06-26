"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

the_list = []
with open("task_2_doc.txt", "r", encoding="UTF-8") as str_list:
    for number, line in enumerate(str_list, 1):
        item = line.split(" ")
        the_list.append(item)
        print(f"В {number}-й строке {len(item)} слов(а)")
    print(f"Количество строк - {len(the_list)}")