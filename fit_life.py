# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_IN_LITRI = 1000


user_name = input('Здравствуйте! Введите, пожалуйста, ваше имя: ')
user_age = int(input('Сколько вам полных лет?: '))
user_weight = float(input('Введите, пожалуйста, '
                          'ваш вес (в кг., используя точку): '))
user_height = float(input('Введите, пожалуйста, '
                          'ваш рост (в метрах, используя точку): '))

bmi = round(user_weight / user_height ** 2, 1)
water_needed = round(WATER_PER_KG * user_weight / ML_IN_LITRI, 1)

print()
print(f'Здравствуйте, {user_name}!')
print(f'Возраст: {user_age}, ИМТ: {bmi},'
      f' Рекомендованная суточная норма воды в литрах: {water_needed}')
print('Расчет окончен. Будьте здоровы!')
