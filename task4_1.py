"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

name, production_hour, rate_hour, bonus = argv
try:
    production_hour = float(production_hour)
    rate_hour = float(rate_hour)
    bonus = float(bonus)
    wages = production_hour * rate_hour + bonus

    print(f'заработная плата сотрудника  {wages}')
except ValueError:
    print('You need to enter a number')




