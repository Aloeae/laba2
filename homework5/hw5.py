#Функция-генератор возвращает числа из диапазона
def get_number0():
    for num in range(30):
        #Проверка на нечтность
        if num % 2 != 0:  
            yield num

#Создание генератор
generator = get_number0()

#Инициализация счётчика
i=0

#Перебор значений генератора
for value in generator:
    i+=1
    if i == 1:
        first_value = value
    if i == 5:
        fifth_value = value
    last_value = value  

#Вывод результата
print(f"Первое нечетное число: {first_value}")
print(f"Пятое нечетное число: {fifth_value}")
print(f"Последнее нечетное число: {last_value}")
