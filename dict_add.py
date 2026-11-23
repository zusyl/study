dict_test = {}
print ('введи название фильма и присвой  ему рейтинг, как закончишь напиши "стоп"')
while True:
    key = input('напиши название фильма или напиши -стоп ').lower().strip()
    if key == 'стоп':
        break
    try:
        value = int(input('напиши рейтинг фильма от 1 до 10 '))
    except ValueError:
        print('ошибка! ты ввел не цифры. вводи заново рейтинг')
        continue
    dict_test[key] = value
print('вот твой рейтинг фильмов:')
for movie, rating in dict_test.items():
    print(f"Фильм: {movie} - Рейтинг: {rating}")
