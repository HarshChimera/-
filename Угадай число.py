import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            guess = int(input("Введи свое число: "))
            attempts += 1

            if guess < number_to_guess:
                print("Слишком низко! Попробуй еще раз.")
            elif guess > number_to_guess:
                print("Слишком высоко! Попробуй еще раз.")
            else:
                print(f"Поздравляю! Ты угадал число {number_to_guess} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введи целое число.")

if __name__ == "__main__":
    guess_the_number()

