import random

# Символи ASCII-арту
characters = {
    'a': [
        "  AA  ",
        " A  A ",
        " AAAAA",
        " A  A ",
        " A  A "
    ],
    'b': [
        " BBB  ",
        " B  B ",
        " BBBB ",
        " B  B ",
        " BBB  "
    ],
    'c': [
        " CCCC ",
        " C    ",
        " C    ",
        " C    ",
        " CCCC "
    ],
    'e': [
        " EEEE ",
        " E    ",
        " EEEE ",
        " E    ",
        " EEEE "
    ],
    'g': [
        " GGGG ",
        " G    ",
        " G GG ",
        " G  G ",
        " GGGG "
    ],
    'i': [
        " III ",
        "  I  ",
        "  I  ",
        "  I  ",
        " III "
    ],
    'r': [
        " RRR  ",
        " R  R ",
        " RRR  ",
        " R R  ",
        " R  R "
    ],
    's': [
        " SSSS ",
        " S    ",
        " SSSS ",
        "    S ",
        " SSSS "
    ],
    'y': [
        " Y  Y ",
        "  YY  ",
        "   Y  ",
        "   Y  ",
        "   Y  "
    ]
}

def run_lab4():
    """
    Основна функція для виконання завдань лабораторної роботи 4.
    """
    # Завдання 8: Варіанти кольорів
    color_option = input("Виберіть опцію кольорів (чорно-білий/відтінки сірого): ").lower()

    # Завдання 1: Введення користувача
    input_text = input("Введіть слово або фразу для ASCII-арту: ")

    # Завдання 5: Вирівнювання тексту
    alignment = input("Виберіть вирівнювання (ліво, центр, право): ").lower()
    if alignment not in ['ліво', 'центр', 'право']:
        alignment = 'ліво'

    # Завдання 3: Розміри Art-у
    width = int(input("Введіть ширину ASCII-арту: "))
    height = int(input("Введіть висоту ASCII-арту: "))

    def generate_ascii_art(input_text, characters, alignment, width, height, color_option):
        """
        Функція для генерації ASCII-арту.

        :param input_text: Введений текст для ASCII-арту.
        :param characters: Символи для генерації ASCII-арту.
        :param alignment: Вирівнювання тексту ('ліво', 'центр', 'право').
        :param width: Ширина ASCII-арту.
        :param height: Висота ASCII-арту.
        :param color_option: Опція кольорів ('чорно-білий', 'відтінки сірого').

        :return: Список рядків ASCII-арту.
        """
        lines = []

        if alignment == 'центр':
            lines.append(input_text.center(width))
        elif alignment == 'право':
            lines.append(input_text.rjust(width))
        else:
            lines.append(input_text.ljust(width))

        for i in range(5):
            line = ""
            for char in input_text:
                if char.lower() in characters:
                    line += characters[char.lower()][i]
                else:
                    line += " " * 6  # Пробіли, якщо символ не знайдено
                line += " "  # Додатковий пробіл між буквами

            if color_option == 'чорно-білий':
                line = "\033[30m" + line + "\033[0m"  # Чорний колір тексту
            elif color_option == 'відтінки сірого':
                line = "\033[90m" + line + "\033[0m"  # Сірий колір тексту

            lines.append(line)

        return lines

    def display_ascii_art(art):
        """
        Функція для відображення ASCII-арту.

        :param art: Список рядків ASCII-арту.
        """
        for line in art:
            print(line)

    def save_ascii_art_to_file(art):
        """
        Функція для збереження ASCII-арту у файл.

        :param art: Список рядків ASCII-арту.
        """
        filename = input("Введіть ім'я файлу: ")
        with open(filename, 'w') as file:
            for line in art:
                file.write(line + '\n')

    def preview_ascii_art(art):
        """
        Функція для попереднього перегляду ASCII-арту.

        :param art: Список рядків ASCII-арту.
        """
        print("Попередній перегляд ASCII-арту:")
        for line in art:
            print(line)

    # Генерація ASCII-арту
    art = generate_ascii_art(input_text, characters, alignment, width, height, color_option)

    # Відображення ASCII-арту
    display_ascii_art(art)

    # Збереження у файл
    save_option = input("Бажаєте зберегти ASCII-арт у файл? (так/ні): ").lower()
    if save_option == 'так':
        save_ascii_art_to_file(art)

    # Попередній перегляд ASCII-арту
    preview_option = input("Бажаєте побачити попередній перегляд ASCII-арту? (так/ні): ").lower()
    if preview_option == 'так':
        preview_ascii_art(art)

if __name__ == "__main__":
    run_lab4()