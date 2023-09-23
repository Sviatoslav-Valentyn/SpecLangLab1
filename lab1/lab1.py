import math
result = None

# Завдання 9: Історія обчислень
history = []

while True:
    # Завдання 1: Введення користувача
    expression = input("Введіть вираз: ") #(або 'вихід' для виходу)

    #Вихід з програми, якщо користувач ввів "вихід"
    if expression.lower() == 'вихід':
        break

    try:
        num1, operator, num2 = map(str.strip, expression.split())

        # Завдання 2: Перевірка оператора
        if operator not in ('+', '-', '*', '/', '^', '√', '%'):
            print("Error: Невірний оператор!")
            continue

        # Завдання 6: Десяткові числа
        num1 = float(num1)
        num2 = float(num2)

        # Обчислення результату
        if operator == '+':
            result = num1 + num2 # Завдання 3: Обчислення
        elif operator == '-':
            result = num1 - num2 # Завдання 3: Обчислення
        elif operator == '*':
            result = num1 * num2 # Завдання 3: Обчислення
        elif operator == '/':
            if num2 == 0 or num1 == 0:        # Завдання 5: Обробка помилок
                print("Error: Не можна ділити на нуль!")
                continue
            result = num1 / num2
            
        # Завдання 7: Додаткові операції
        elif operator == '^':
            result = num1 ** num2
        elif operator == '√':
            result = math.sqrt(num1)
        elif operator == '%':
            result = num1 % num2

        # Виведення результату
        print(f"Результат: {result}")

         # Завдання 9: Історія обчислень
        history.append((expression, result))
        
        # Завдання 9: Історія обчислень
        print("Історія обчислень:")
        for expr, res in history:
            print(f"{expr} = {res}")
        
        # Завдання 4: Повторення обчислень
        next_operation = input("Бажаєте продовжити (так/ні)? ")
        if next_operation.lower() != 'так':
            break

    except ValueError:
        print("Error: Невірний формат!")

print("Я виключаюсь")