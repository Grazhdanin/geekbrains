"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def user_data(name, surname, year, city, email, telephone):
    return print(f"{name}, {surname}, {year}, {city}, {email}, {telephone}")
user_data(name="Sergey", surname="Samoylov", year=1994, city="Moscow", email="sergo@mail.ru", telephone=8-932-0)



