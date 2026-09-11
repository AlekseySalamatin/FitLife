# Проект FitLife - MVP версия 2.0
WATER_PER_KG = 30
ML_IN_LITRI = 1000
MIN_NORM = 19.5
MAX_NORM = 22.9
MIN_AGE = 18
MAX_AGE = 80
MIN_WEIGHT = 30
MAX_WEIGHT = 300
MIN_HEIGHT = 1.5
MAX_HEIGHT = 2

print('Здравствуйте!')
while True:
    user_name = input('Введите, пожалуйста, ваше имя: ')
    if user_name.strip() != '':
        break
    print('Имя должно содержать символы.')

while True:
    try:
        user_age = int(input('Ваш возраст (полных лет): '))
        if MIN_AGE <= user_age <= MAX_AGE:
            break
        print(f'Возраст для корректного расчёта должен быть '
              f'от {MIN_AGE} до {MAX_AGE} лет.')
    except ValueError:
        print('Возраст должен быть целым числом, написанным цифрами.')

while True:
    try:
        user_weight = float(input('Введите, пожалуйста, '
                            'ваш вес (в кг.): ').replace(',', '.'))
        if MIN_WEIGHT <= user_weight <= MAX_WEIGHT:
            break
        print(f'Вес для корректного расчёта должен быть '
              f'от {MIN_WEIGHT} до {MAX_WEIGHT} кг.')
    except ValueError:
        print('Вес должен быть написан цифрами.')

while True:
    try:
        user_height = float(input('Введите, пожалуйста, '
                            'ваш рост (в метрах): ').replace(',', '.'))
        if MIN_HEIGHT <= user_height <= MAX_HEIGHT:
            break
        print(f'Рост для корректного расчёта должен быть '
              f'от {MIN_HEIGHT} до {MAX_HEIGHT} метров.')
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
