import random
import string


def generate_password(length=8, use_digits=True, use_special=True):
    # Создание базового набора символов, в котором все буквы английского алфавита
    characters = string.ascii_letters

    # Добавление цифр, если это указано
    if use_digits:
        characters += string.digits

    # Добавление спец. символом, если это указано
    if use_special:
        characters += string.punctuation

    # Генерация пароля со случайно выбранными символами из characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Запрос длины пароля у пользователя
password_length = int(input("Введите длину пароля: "))
use_digits = input("Использовать цифры? (да/нет): ").lower() == 'да'
use_special = input("Использовать специальные символы? (да/нет): ").lower() == 'да'

# Генерация и вывод пароля
password = generate_password(password_length, use_digits, use_special)
print("Сгенерированный пароль:", password)

