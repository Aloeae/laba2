from datetime import datetime

def calculate_age():
    while True:
        #Запрос даты рождения в формате день.месяц.год
        bd = input("Введите вашу дату рождения (дд.мм.гггг): ")
        
        try:
            #Преобразование строки в дату
            birth_date = datetime.strptime(bd, "%d.%m.%Y")
            
            #Текущая дата
            today = datetime.today()
            
            #Проверка, что дата рождения не в будущем
            if birth_date > today:
                print("Введена дата рождения в будущем врмени. Введите верную дату рождения.")
                continue
            
            #Вычисление возраста
            age = today.year - birth_date.year
            
            #Проверка, был ли уже день рождения в этом году
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
                
            return age
        
        except ValueError:
            #Обработка ошибки неправильного формата даты
            print("Неверный формат. Введите дату в формате дд.мм.гггг.")
            


user_age = calculate_age()
#Если возраст оканчивается на 1
if user_age % 10 == 1:
    print(f"Ваш возраст: {user_age} год")
    
#Если возраст оканчивается на 2, 3, 4   
elif user_age % 10 == 2 or user_age % 10 == 3 or user_age % 10 == 4:
    print(f"Ваш возраст: {user_age} года")

#Остальные возраста     
else:
    print(f"Ваш возраст: {user_age} лет")
