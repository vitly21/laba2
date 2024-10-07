import random

def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def get_user_choice():
    choices = ['камень', 'ножницы', 'бумага']
    user_input = input("Введите 'камень', 'ножницы' или 'бумага' (или 'выход' для завершения): ").lower()
    
    if user_input in choices or user_input == 'выход':
        return user_input
    else:
        print("Некорректный ввод. Пожалуйста, попробуйте снова.")
        return get_user_choice()

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "Вы победили!"
    else:
        return "Компьютер победил!"

def play_game():
    print("Добро пожаловать в игру «Камень-ножницы-бумага»!")
    
    while True:
        user_choice = get_user_choice()
        if user_choice == 'выход':
            print("Спасибо за игру!")
            break

        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")

        result = winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    play_game()
