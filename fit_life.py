# Проект FitLife - MVP версия 2.0
WATER_PER_KG = 30
ML_IN_LITRI = 1000
MIN_NORM = 19.5
MAX_NORM = 22.9

print('Здравствуйте!')
while True:
    user_name = input('Введите, пожалуйста, ваше имя: ')
    if user_name.strip() != '':
        break
    else:
        print('Имя должно содержать символы.')

while True:
    try:
        user_age = int(input('Ваш возраст (полных лет): '))
        if 18 <= user_age <= 80:
            break
        else:
            print('Возраст для корректного расчёта должен быть '
                  'от 18 до 80 лет.')
    except ValueError:
        print('Возраст должен быть целым числом, написанным цифрами.')

while True:
    try:
        user_weight = float(input('Введите, пожалуйста, '
                            'ваш вес (в кг.): ').replace(',', '.'))
        if 30 <= user_weight <= 300:
            break
        else:
            print('Вес для корректного расчёта должен быть '
                  'от 30 до 300 кг.')
    except ValueError:
        print('Вес должен быть написан цифрами.')

while True:
    try:
        user_height = float(input('Введите, пожалуйста, '
                            'ваш рост (в метрах): ').replace(',', '.'))
        if 1.5 <= user_height <= 2:
            break
        else:
            print('Рост для корректного расчёта должен быть '
                  'от 1.5 до 2 метров.')
    except ValueError:
        print('Рост должен быть написан цифрами.')


bmi = round(user_weight / user_height ** 2, 1)
water_needed = round(WATER_PER_KG * user_weight / ML_IN_LITRI, 1)

print()
print(f'{user_name}')
print(f'Возраст: {user_age}')
print(f'ИМТ: {bmi}', end=' -- ')
if bmi < MIN_NORM:
    print('Вам рекомендуется набрать вес.')
if bmi > MAX_NORM:
    print('Вам рекомендуется сбросить вес.')
if MIN_NORM <= bmi <= MAX_NORM:
    print('Ваш вес в норме!')
print(f'Рекомендованная суточная норма воды в литрах: {water_needed}')
print('Расчет окончен. Будьте здоровы!')
