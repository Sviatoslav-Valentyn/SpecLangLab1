import unittest
from lab2 import Calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        calculator = Calculator()
        result = calculator.calculate(2, '+', 3)
        self.assertEqual(result, 5, "Додавання не працює для позитивних чисел")

        result = calculator.calculate(-2, '+', -3)
        self.assertEqual(result, -5, "Додавання не працює для від'ємних чисел")

    def test_subtraction(self):
        calculator = Calculator()
        result = calculator.calculate(5, '-', 3)
        self.assertEqual(result, 2, "Віднімання не працює для позитивних чисел")

        result = calculator.calculate(-3, '-', -1)
        self.assertEqual(result, -2, "Віднімання не працює для від'ємних чисел")

    def test_multiplication(self):
        calculator = Calculator()
        result = calculator.calculate(5, '*', 0)
        self.assertEqual(result, 0, "Множення не працює з нулем")

        result = calculator.calculate(5, '*', 3)
        self.assertEqual(result, 15, "Множення не працює для позитивних чисел")

        result = calculator.calculate(5, '*', -3)
        self.assertEqual(result, -15, "Множення не працює для від'ємних чисел")

    def test_division(self):
        calculator = Calculator()
        result = calculator.calculate(15, '/', 3)
        self.assertEqual(result, 5, "Ділення працює для позитивних чисел")

        result = calculator.calculate(15, '/', -3)
        self.assertEqual(result, -5, "Ділення не працює для від'ємних чисел")

        result = calculator.calculate(5, '/', 0)
        self.assertEqual(result, "Помилка: Не можна ділити на нуль!", "Помилка ділення на нуль не оброблена правильно")

    def test_error_handling(self):
        calculator = Calculator()
        result = calculator.calculate(3, '+', 'abc')
        self.assertEqual(result, "Помилка: Невірний формат числа!", "Помилка невірного формату числа не оброблена правильно")

        result = calculator.calculate('abc', '+', 3)
        self.assertEqual(result, "Помилка: Невірний формат числа!", "Помилка невірного формату числа не оброблена правильно")
        
        result = calculator.calculate(10, '/', 0)
        self.assertEqual(result, "Помилка: Не можна ділити на нуль!", "Помилка ділення на нуль не оброблена правильно")

        result = calculator.calculate(-25, '√', 0)
        self.assertEqual(result, "Помилка: Від'ємне число під коренем!", "Помилка обчислення кореня з від'ємного числа не оброблена правильно")

if __name__ == '__main__':
    unittest.main()
