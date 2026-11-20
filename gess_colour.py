colour_list = ['красный' , 'синий' , 'желтый']
question = 'угадай цвет, введи один из трех '
colour = input(question).strip().lower()
while colour not in colour_list:
    print('не угадал')
    colour = input(question).strip().lower()
print(f'ура, угадал это {colour} цвет')
