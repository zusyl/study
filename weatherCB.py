range_word = ["солнечно", "снег", "дождь", "облачно"]
counter = 3
count = 0
weather = input("Какая сегодня погода? Солнечно/Снег/Дождь/Облачно ").strip().lower()
while weather not in range_word:
    count +=1
    print(f"не балуйся пиши про погоду. У тебя {counter} попытки. и уже использовано  {count} попыток")
    if count >= counter:
        print('вали неудачник')
        break
    weather = input("Какая сегодня погода? Солнечно/Снег/Дождь/Облачно ").strip().lower()
else:
    if weather == "солнечно":
        print('отличный день. иди гулять')
    elif weather == 'снег':
        print('не забудь шапку')
    elif weather == 'дождь':
        print('возьми зонт')
    else:
        print('да пофиг, все равно иди гулять')
    print(f'ты использовал {count} попыток')
