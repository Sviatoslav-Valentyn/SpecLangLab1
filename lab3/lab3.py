import pyfiglet
from art import *
from termcolor import colored

# Завдання 1: Введення користувача
def get_user_input():
    user_input = input("Введіть слово або фразу, яку ви хочете перетворити в ASCII-арт: ")
    return user_input

# Завдання 3: Вибір шрифту
def select_font():
    print("Доступні шрифти:")
    print("1. standard")
    print("2. slant")
    print("3. script")
    font_choice = input("Виберіть номер шрифту (1/2/3): ")
    
    fonts = ["standard", "slant", "script"]
    if font_choice in ['1', '2', '3']:
        return fonts[int(font_choice) - 1]
    else:
        print("Невірний вибір шрифту. Виберіть номер зі списку.")
        return select_font()

# Завдання 4: Колір тексту
def select_color():
    print("Доступні кольори:")
    print("1. Червоний")
    print("2. Синій")
    print("3. Зелений")
    color_choice = input("Виберіть номер кольору (1/2/3): ")
    
    colors = ["red", "blue", "green"]
    if color_choice in ['1', '2', '3']:
        return colors[int(color_choice) - 1]
    else:
        print("Невірний вибір кольору. Виберіть номер зі списку.")
        return select_color()

# Завдання 7: Розмір ARTу
def select_size():
    width = int(input("Введіть ширину ASCII-арту: "))
    height = int(input("Введіть висоту ASCII-арту: "))
    return width, height

# Завдання 8: Вибір символів
def select_characters():
    characters = input("Введіть символи, які ви хочете використовувати (наприклад, '@#$%'): ")
    return characters

# Завдання 6: Збереження у файл
def save_to_file(ascii_art):
    file_name = input("Введіть ім'я файлу для збереження (з розширенням .txt): ")
    try:
        with open(file_name, 'w') as file:
            file.write(ascii_art)
        print(f"ASCII-арт збережено у файлі {file_name}")
    except Exception as e:
        print(f"Помилка при збереженні файлу: {str(e)}")

# Завдання 5: Форматування виводу
def format_output(ascii_art, width, height):
    # Вирівнюємо ASCII-арт у центрі екрану
    lines = ascii_art.split('\n')
    formatted_art = []
    for line in lines:
        formatted_line = line.center(width)
        formatted_art.append(formatted_line)
    
    # Змінюємо висоту ASCII-арту
    formatted_art = formatted_art[:height]
    
    return '\n'.join(formatted_art)

# Завдання 9: Функція попереднього перегляду
def preview_ascii_art(ascii_art):
    print("Попередній перегляд ASCII-арту:")
    print(ascii_art)

if __name__ == "__main__":
    input_text = get_user_input()
    
    font = select_font()
    color = select_color()
    width, height = select_size()
    characters = select_characters()
    
    # Використовуємо бібліотеку pyfiglet для генерації ASCII-арту
    ascii_art = pyfiglet.figlet_format(input_text, font=font)
    
    # Завдання 8: Вибір символів (заміна символів на вказаний)
    for old_char, new_char in zip(ascii_art, characters):
        ascii_art = ascii_art.replace(old_char, new_char)
    
    # Завдання 5: Форматування виводу
    formatted_ascii_art = format_output(ascii_art, width, height)
    
    # Використовуйте termcolor для додавання кольорів до ASCII-арту:
    colored_ascii_art = colored(formatted_ascii_art, color)
    
    # Завдання 9: Функція попереднього перегляду
    preview_ascii_art(colored_ascii_art)
    
    save_choice = input("Зберегти ASCII-арт у файл? (так/ні): ")
    if save_choice.lower() == 'так':
        save_to_file(colored_ascii_art)