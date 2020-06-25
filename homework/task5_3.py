"""
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников
"""

small = []
with open("task_3_doc.txt", "r", encoding="UTF-8") as text:

    for line in text:

        str_list = line.split(" ")
        var1 = int(str_list[1])
        var2 = int(str_list[2])
        var3 = int(str_list[3])
        average_salary = (var1 + var2 + var3) / 3

        print(f"Cредняя зарлпата: {str_list[0]} - {average_salary} ")

        if var1 < 20000 and var2 < 20000 and var3 < 20000:
            small.append(str_list[0])
print(f"Список сотрудников, у которых оклад меньше 20000:\n{small}")
