import random

# Завдання 1: Введення користувача
input_text = input("Введіть слово або фразу для ASCII-арту: " )

# Завдання 2: Набір символів
characters = "@#*%+=-:. "

# Завдання 3: Розміри Art-у
width = int(input("Введіть ширину ASCII-арту: "))
height = int(input("Введіть висоту ASCII-арту: "))

# Завдання 5: Вирівнювання тексту
alignment = input("Виберіть вирівнювання (ліво, центр, право): ").lower()
if alignment not in ['ліво', 'центр', 'право']:
    alignment = 'ліво'

# Завдання 4: Функція генерації Art-у
def generate_ascii_art(input_text, characters, width, height, alignment):
    lines = []
    for _ in range(height):
        line = ""
        for _ in range(width):
            line += random.choice(characters)
        lines.append(line)

    if alignment == 'центр':
        centered_lines = [line.center(width) for line in lines]
        return centered_lines
    elif alignment == 'право':
        right_aligned_lines = [line.rjust(width) for line in lines]
        return right_aligned_lines
    else:
        return lines

# Завдання 6: Відображення мистецтва
art = generate_ascii_art(input_text, characters, width, height, alignment)
for line in art:
    print(line)

# Завдання 7: Збереження у файл
save_option = input("Бажаєте зберегти ASCII-арт у файл? (так/ні): ").lower()
if save_option == 'так':
    filename = input("Введіть ім'я файлу: ")
    with open(filename, 'w') as file:
        for line in art:
            file.write(line + '\n')

# Завдання 9: Функція попереднього перегляду
def preview_ascii_art(art):
    print("Попередній перегляд ASCII-арту:")
    for line in art:
        print(line)

# Виклик функції попереднього перегляду
preview_option = input("Бажаєте побачити попередній перегляд ASCII-арту? (так/ні): ").lower()
if preview_option == 'так':
    preview_ascii_art(art)

# Завдання 8: Варіанти кольорів (чорно-білий, відтінки сірого)
color_option = input("Виберіть опцію кольорів (чорно-білий/відтінки сірого): ").lower()
if color_option == 'відтінки сірого':
    grayscale_characters = "@%#*+=-:. "
    grayscale_art = generate_ascii_art(input_text, grayscale_characters, width, height, alignment)
    for line in grayscale_art:
        print(line)