import random

#Возможные варианты игры с нумерацией
options = ['камень', 'ножницы', 'бумага']

#Функция для определения победителя
def winner(player_num, computer_num):
    #Если выборы совпадают
    if player_num == computer_num:
        return "Ничья!"
    
    #Условия выигрыша сторон
    if (player_num == 1 and computer_num == 2) or \
       (player_num == 2 and computer_num == 3) or \
       (player_num == 3 and computer_num == 1):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

#Основная игра
while True:
    
    #Выбор компьютера
    computer = random.randint(1, 3)  

    #Выбор игрока
    print("Выберите один из вариантов:")
    print("1. Камень")
    print("2. Ножницы")
    print("3. Бумага")
    print("Введите номер вашего выбора (или '0' для выхода): ")

    #Проверка правильности ввода
    while True:
        try:
            player = int(input())
            if player == 0:
                print("Игра окончена.")
                exit()
            elif player in [1, 2, 3]:
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 3.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите номер.")

    #Вывод выбора игрока и компьютера
    print(f"Вы выбрали: {options[player - 1]}")
    print(f"Компьютер выбрал: {options[computer - 1]}")

    #Определение и вывод победителя
    result = winner(player, computer)
    print(result)
    print()  
