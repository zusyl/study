import time #добавлен модуль паузы
import random #добавлен модуль рандомного числа
def get_valid_number(question_text):
    """
    эта функция запрашивает у пользователя ввод до тех пор, пока
    он не напишет только цифры. Возвращает готовое число
    """
    while True:
        user_answer = input(question_text)
        if user_answer.isdigit():
            return int(user_answer)
        else:
            print("Ошибка! Вводи только цифры.")
            
            
def get_valid_age(question_text):
    """
    эта функция запрашивает возраст, проверяет его . Возвращает готовое число от 1 до 120
    """
    while True:
        age = get_valid_number(question_text)
        if 0 < age <= 120:
            return age
        else:
            print("Ошибка! Введи число от 1 до 120. ")
    
def fake_loading():
    """
    тут работает таймер
    """    
    wait_seconds = random.randint(10, 15)
    print("hard cacluiations!!! wait a moment.")
    for i in range(wait_seconds, 0, -1):
        print("\rfinisht after", i, "   ", end=" ")
        time.sleep(1)
    print()
    
def check_right(grid, y, x, visited):
    """
    проверка хода направо
    """
    max_x = len(grid[0])  # Ширина поля
    next_x = x + 1
    print('смотрю направо')    
    # Сначала проверяем с помощью твоей функции, не вышли ли за край по X
    if is_valid_coordinate(next_x, max_x):
        # Дополнительно можно проверить, свободна ли клетка (например, 0) и не посещали ли её
        if grid[y][next_x] == 0 and (y, next_x) not in visited:
            print('иду направо')
            return next_x
        else:
            print('Сюда нельзя. Тут мы были или тут стена')
    else:
            print('Сюда нельзя. Тут конец поля')
            
    return x  # Если нельзя двигаться, возвращаем старые координаты
            
def check_left(grid, y, x, visited):
    """
    проверка хода налево
    """
    max_x = len(grid[0])
    next_x = x - 1
    print('смотрю налево')
    
    if is_valid_coordinate(next_x, max_x):
        if grid[y][next_x] == 0 and (y, next_x) not in visited:
            print('иду налево')
            return next_x
        else:
            print('Сюда нельзя. Тут мы были или тут стена')
    else:
            print('Сюда нельзя. Тут конец поля')
            
    return x

def check_up(grid, y, x, visited):
    """
    проверка хода вверх
    """
    max_y = len(grid)     # Высота поля
    next_y = y - 1
    
    if is_valid_coordinate(next_y, max_y):
        if grid[next_y][x] == 0 and (next_y, x) not in visited:
            return next_y
            
    return y

def check_down(grid, y, x, visited):
    """
    проверка хода вниз
    """
    max_y = len(grid)
    next_y = y + 1
    
    if is_valid_coordinate(next_y, max_y):
        if grid[next_y][x] == 0 and (next_y, x) not in visited:
            return next_y
            
    return y
             
def is_valid_coordinate(value, max_value):
    """
    Проверяет, находится ли координата в пределах от 0 до max_value - 1.
    Возвращает True, если значение допустимо, иначе False.
    """
    if 0 <= value < max_value:
        return True
    else:
        return False
        
def print_maze(grid, current_y, current_x, visited):
    """
    печать лабиринта с учетом следов посещенных клеток
    """
    print("\033[H\033[J", end="")
    
    for r_idx, row in enumerate(grid):
        row_str = ""
        for c_idx, cell in enumerate(row):
            # 1. Если здесь стоит робот — рисуем звездочку
            if r_idx == current_y and c_idx == current_x:
                row_str += " * "
            # 2. Если это стена
            elif cell == 1:
                row_str += " █ "
            # 3. Если клетка уже была посещена (но это не текущая позиция робота)
            elif (r_idx, c_idx) in visited:
                row_str += " . "  # Здесь можно поставить другой символ, например ' . ' или ' + '
            # 4. Во всех остальных случаях (неизведанная дорога)
            else:
                row_str += "   "  # Пустое место для непосещенных клеток
                
        print(row_str)
    print("-" * 15)
