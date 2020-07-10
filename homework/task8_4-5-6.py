"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class OfficeEquipment:
    def __init__(self, producer, model_name, weight, color,
                 length, width, height):
        self._check_input(weight, length, width, height)
        self.producer = producer
        self.model_name = model_name
        self.weight = weight
        self.color = color
        self.sizes = {'length': length, 'width': width, 'height': height}
        self._items_stock = 0

    @classmethod

    def _check_input(cls, weight, length, width, height):

        check_list = [weight, length, width, height]

        for check in check_list:
            if not isinstance(check, int):
                raise ValueError(f"{check} не является int")

    def office_equip(self, new_items):

        if not isinstance(new_items, int):
            raise ValueError(f"{new_items} не является int")

        self._items_stock += new_items

    def transfer_office(self, transfer):
        if not isinstance(transfer, int):
            raise (f"{transfer} не является int")

        self._items_stock -= transfer

    def __str__(self):
        return f'{self.__class__.__name__}: {self.producer},' \
               f'{self.model_name}, {self.color}, {self.weight}кг,\n'\
               f'параметры:{self.sizes},\nколичество:{self._items_stock}шт'

class Printer(OfficeEquipment):
    def __init__(self, producer, model_name, weight, color,
                 length, width, height, minute_print=None):
        super().__init__(producer, model_name, weight, color,
                     length, width, height)
        self.minute_print = minute_print

class Scaner(OfficeEquipment):
    def __init__(self, producer, model_name, weight, color,
                 length, width, height, minute_prints=None):
        super().__init__(producer, model_name, weight, color,
                     length, width, height)
        self.minute_print = minute_prints

class Xerox(OfficeEquipment):
    def __init__(self, producer, model_name, weight, color,
                 length, width, height, minute_copy=None):
        super().__init__(producer, model_name, weight, color,
                     length, width, height)
        self.minute_copy = minute_copy

a = Scaner('HP', "2400", 5, "black", 70, 40, 20)
a.office_equip(2)
print(a)
a.transfer_office(1)
print(a)
