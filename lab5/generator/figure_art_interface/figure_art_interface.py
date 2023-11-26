from abc import ABC, abstractmethod
from generator.figures.figure import Figure
from generator.figures.figures_3d.cube import Cube
from generator.figures.figures_2d.square import Square
from generator.colors.colors import textFileSaver


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Generate3DFigureCommand(Command):
    def __init__(self, figure_interface):
        self.figure_interface = figure_interface

    def execute(self):
        print(self.figure_interface.generate3dFigure())


class SetSizeCommand(Command):
    def __init__(self, figure_interface, new_size):
        self.figure_interface = figure_interface
        self.new_size = new_size

    def execute(self):
        self.figure_interface.setSize(self.new_size)


class SetColorCommand(Command):
    def __init__(self, figure_interface, new_color):
        self.figure_interface = figure_interface
        self.new_color = new_color

    def execute(self):
        self.figure_interface.setColor(self.new_color)


class FigureArtInterface(Figure):
    def __init__(self):
        super().__init__()
        self.type = "cube"
        self.left_padding = 5
        self.top_padding = 5
        self.bottom_padding = 5
        self.commands = {
            1: Generate3DFigureCommand(self),
            2: SetSizeCommand(self, 0),
            3: SetColorCommand(self, "")
        }

    def setType(self, type):
        self.type = type

    def setPaddings(self, left_padding, top_padding, bottom_padding):
        self.left_padding = left_padding
        self.top_padding = top_padding
        self.bottom_padding = bottom_padding

    def setPrimaryData(self):
        size = int(input("Розмір фігури: "))
        self.setSize(size)

        color = input(
            "Колір фігури (blue, green, red, magenta, yellow, white, cyan): ")
        self.setColor(color)

        type = input("Тип фігури (пропустити для типу за замовчуванням): ")
        if len(type):
            self.setType(type)

    def generateWithLeftPadding(self, text):
        lines = text.split('\n')
        padded_lines = [f"{' ' * self.left_padding}{line}" for line in lines]
        return '\n'.join(padded_lines)

    def generateWithTopPadding(self, text):
        space = self.top_padding * '\n'
        padded_lines = space + text
        return padded_lines

    def generateWithBottomPadding(self, text):
        space = self.bottom_padding * '\n'
        padded_lines = text + space
        return padded_lines

    def generateWithPaddings(self, text):
        return self.generateWithBottomPadding(self.generateWithTopPadding(self.generateWithLeftPadding(text)))

    def generate3dFigure(self):
        if self.type == 'куб':
            cube = Cube()
            cube.setSize(self.size)
            cube.setColor(self.color)
            return self.generateWithPaddings(cube.generateFigure())
        return super().generateFigure()

    def generate2dFigure(self):
        if self.type == 'куб':
            square = Square()
            square.setSize(self.size)
            square.setColor(self.color)
            return self.generateWithPaddings(square.generateFigure())
        return super().generateFigure()

    def saveToFile2d(self):
        filename = input("Введіть ім'я файлу перед збереженням: ")
        textFileSaver(
            filename, self.generate2dFigure())

    def saveToFile3d(self):
        filename = input("Введіть ім'я файлу перед збереженням: ")
        textFileSaver(
            filename, self.generate3dFigure())

    @staticmethod
    def show_menu():
        print("Виберіть пункт меню")
        print("1 - Згенерувати 3D фігуру")
        print("2 - Встановити розмір")
        print("3 - Встановити колір (blue, green, red, magenta, yellow, white, cyan)")
        print("4 - Встановити тип (куб)")
        print("5 - Встановити відступи")
        print("6 - Отримати 2D версію фігури")
        print("7 - Зберегти у файл (3D)")
        print("8 - Зберегти у файл (2D)")
        print("0 - Вихід")

    def loopMenu(self):
        while True:
            self.show_menu()
            menu_choice = int(input("Ключ меню: "))
            if (menu_choice == 1):
                print(self.generate3dFigure())
            elif (menu_choice == 2):
                new_size = int(input("Введіть новий розмір: "))
                self.setSize(new_size)
            elif (menu_choice == 3):
                new_color = input("Введіть новий колір: ")
                self.setColor(new_color)
            elif (menu_choice == 4):
                new_type = input("Введіть новий тип: ")
                self.setType(new_type)
            elif (menu_choice == 5):
                left_padding = int(input("Введіть лівий відступ: "))
                top_padding = int(input("Введіть верхній відступ: "))
                bottom_padding = int(input("Введіть нижній відступ: "))
                self.setPaddings(left_padding, top_padding, bottom_padding)
            elif (menu_choice == 6):
                print(self.generate2dFigure())
            elif (menu_choice == 7):
                self.saveToFile3d()
            elif (menu_choice == 8):
                self.saveToFile2d()
            else:
                break

    def launch(self):
        self.setPrimaryData()
        print(self.generate3dFigure())
        self.loopMenu()


if __name__ == "__main__":
    interface = FigureArtInterface()
    interface.launch()