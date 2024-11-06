import random

# Инициализация пустой доски
board = [" " for _ in range(9)]


def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(player):
    # Проверка победных комбинаций
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def check_draw():
    return " " not in board


def player_move():
    while True:
        try:
            move = int(input("Введите номер клетки (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Клетка уже занята, выберите другую.")
        except (IndexError, ValueError):
            print("Неправильный ввод. Введите число от 1 до 9.")


def bot_move(level="easy"):
    if level == "easy":
        easy_bot_move()
    elif level == "hard":
        hard_bot_move()


def easy_bot_move():
    # Случайный ход
    move = random.choice([i for i in range(9) if board[i] == " "])
    board[move] = "O"


def hard_bot_move():
    best_score = float('-inf')
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"


def minimax(board, depth, is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def main():
    print("Добро пожаловать в игру Крестики-нолики!")
    print("Вы играете крестиками (X), бот — ноликами (O).")

    level = input("Выберите уровень сложности бота (easy/hard): ").strip().lower()
    while level not in ("easy", "hard"):
        level = input("Неправильный выбор. Выберите уровень сложности (easy/hard): ").strip().lower()

    while True:
        print_board()
        player_move()
        if check_winner("X"):
            print_board()
            print("Вы победили!")
            break
        elif check_draw():
            print_board()
            print("Ничья!")
            break

        bot_move(level)
        if check_winner("O"):
            print_board()
            print("Бот победил!")
            break
        elif check_draw():
            print_board()
            print("Ничья!")
            break


if __name__ == "__main__":
    main()

