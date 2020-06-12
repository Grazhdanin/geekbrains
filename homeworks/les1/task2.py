""""Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк."""

time = input("Введите время в секундах: ")

time = int(time)
hour = time // 3600
hour_remain = time % 3600
minute = hour_remain // 60
second = hour_remain % 60

print(f"{hour}:{minute}:{second}")