import math

# Концепції:
# 1-Класи і об'єкти: Я визначив клас Calculator, який містить властивості та методи для створення об'єктів калькулятора.
#    Наприклад, calculator = Calculator(selected_language) створює об'єкт calculator на основі класу Calculator.

# 2-Інкапсуляція: Я використав приватні властивості та методи класу Calculator, такі як self.result, self.history,
#    інші методи та властивість self.language, для приховування деталей реалізації від користувача класу.
#    Користувач має доступ лише до граничного інтерфейсу, який я визначив.

# 3-Наслідування: відсутні

# 4-Поліморфізм: У коді використовую метод calculate, який може виконувати різні операції з числами в залежності від оператора,
#    введеного користувачем. Це можна розглядати як приклад поліморфізму, оскільки метод calculate працює з різними типами операцій.

class Calculator:
    """Клас, який представляє собою простий калькулятор."""

    def __init__(self, language='ukrainian'):
        """Ініціалізація об'єкта калькулятора.

        Args:
            language (str): Обрана мова. За замовчуванням 'ukrainian'.
        """
        self.result = None
        self.history = []
        self.language = language  # Змінна language для вибору мови (за замовчуванням - українська).

    def set_language(self, language):
        """Встановлює обрану мову.

        Args:
            language (str): Обрана мова.
        """
        self.language = language

    def get_language(self):
        """Повертає обрану мову.

        Returns:
            str: Обрана мова.
        """
        return self.language

    def get_operator_prompt(self):
        """Повертає текстовий запит для введення виразу користувачем.

        Returns:
            str: Текстовий запит.
        """
        if self.language == 'english':
            return "Enter an expression (e.g., '2 + 2' or 'exit'): "
        elif self.language == 'ukrainian':
            return "Введіть вираз (наприклад, '2 + 2' або 'вихід'): "
        else:
            return "Enter an expression (e.g., '2 + 2' or 'exit'): "

    def get_continue_prompt(self):
        """Повертає текстовий запит для продовження виконання програми.

        Returns:
            str: Текстовий запит.
        """
        if self.language == 'english':
            return "Do you want to continue (yes/no)? "
        elif self.language == 'ukrainian':
            return "Бажаєте продовжити (так/ні)? "
        else:
            return "Do you want to continue (yes/no)? "

    def calculate(self, num1, operator, num2):
        """Виконує обчислення на основі введених чисел та оператора.

        Args:
            num1 (float): Перше число.
            operator (str): Оператор.
            num2 (float): Друге число.

        Returns:
            float or str: Результат обчислення або повідомлення про помилку.
        """
        try:
            num1 = float(num1)
            num2 = float(num2)

            if operator == '+':
                self.result = num1 + num2
            elif operator == '-':
                self.result = num1 - num2
            elif operator == '*':
                self.result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    return "Помилка: Не можна ділити на нуль!" if self.language == 'ukrainian' else "Error: Cannot divide by zero!"
                self.result = num1 / num2
            elif operator == '^':
                self.result = num1 ** num2
            elif operator == '√':
                if num1 < 0:
                    return "Помилка: Від'ємне число під коренем!" if self.language == 'ukrainian' else "Error: Negative number under the square root!"
                self.result = math.sqrt(num1)
            elif operator == '%':
                if num2 == 0:
                    return "Помилка: Ділення на нуль!" if self.language == 'ukrainian' else "Error: Division by zero!"
                self.result = num1 % num2
            else:
                return "Помилка: Невірний оператор!" if self.language == 'ukrainian' else "Error: Invalid operator!"

            return self.result
        except ValueError:
            return "Помилка: Невірний формат числа!" if self.language == 'ukrainian' else "Error: Invalid number format!"

    def check_operator(self, operator):
        """Перевіряє правильність оператора.

        Args:
            operator (str): Оператор.

        Returns:
            bool: True, якщо оператор правильний, інакше False.
        """
        return operator in ('+', '-', '*', '/')

    def add_to_history(self, expression, result):
        """Додає вираз та результат в історію обчислень.

        Args:
            expression (str): Вираз.
            result (float): Результат обчислення.
        """
        self.history.append((expression, result))

    def show_history(self):
        """Виводить історію обчислень."""
        if not self.history:
            print("Історія обчислень порожня." if self.language == 'ukrainian' else "Calculation history is empty.")
        else:
            print("Історія обчислень:" if self.language == 'ukrainian' else "Calculation history:")
            for idx, (expr, res) in enumerate(self.history, start=1):
                print(f"{idx}. {expr} = {res}")

    def user_input(self):
        """Запитує вираз користувача та повертає його.

        Returns:
            str: Вираз користувача.
        """
        expression = input(self.get_operator_prompt())
        return expression

    def perform_calculation(self, expression):
        """Виконує обчислення та виводить результат.

        Args:
            expression (str): Вираз користувача.
        """
        try:
            num1, operator, num2 = map(str.strip, expression.split())

            if self.check_operator(operator):
                result = self.calculate(num1, operator, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Результат: {result}")
                    self.add_to_history(expression, result)
            else:
                print("Помилка: Невірний оператор!" if self.language == 'ukrainian' else "Error: Invalid operator!")
        except ValueError:
            print("Помилка: Невірний формат виразу!" if self.language == 'ukrainian' else "Error: Invalid expression format!")

    def main_loop(self):
        """Головний цикл програми."""
        while True:
            expression = self.user_input()

            if expression.lower() == 'вихід' or expression.lower() == 'exit':
                break

            self.perform_calculation(expression)

            self.show_history()

            next_operation = input(self.get_continue_prompt())
            if next_operation.lower() != 'так' and next_operation.lower() != 'yes':
                break

        print("Програма завершена." if self.language == 'ukrainian' else "Program terminated.")

def run_lab2():
    """Функція для виконання програми."""
    print("Виберіть мову (українська або англійська):")
    selected_language = input("Choose a language (ukrainian or english): ").lower()

    while selected_language not in ['ukrainian', 'english']:
        print("Неправильно вибрана мова. Будь ласка, виберіть українську або англійську.")
        print("Invalid language selection. Please choose ukrainian or english.")
        selected_language = input("Choose a language (ukrainian or english): ").lower()

    calculator = Calculator(selected_language)
    calculator.main_loop()

if __name__ == "__main__":
    run_lab2()